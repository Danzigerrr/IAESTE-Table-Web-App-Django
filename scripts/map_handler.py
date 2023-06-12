import folium
from iaeste_table.models import Offer
import pandas as pd
import os
from unidecode import unidecode


# Function to convert special letters to normal letters
def convert_special_letters(text):
    return unidecode(text)


def get_cities_dataframe():
    df = pd.read_csv('cities_locations.csv', delimiter=',', index_col=False)

    # Apply the function to the whole dataframe
    columns_to_convert = ['CountryLong', 'City', 'AccentCity']
    df[columns_to_convert] = df[columns_to_convert].applymap(convert_special_letters)
    return df


def get_city_location(df, offers):
    city_name = unidecode(offers[0].location_city.lower())
    country_name = unidecode(offers[0].location_country.lower())

    # look for the location of city where offer is located
    result_by_city = df.loc[((df['City'] == city_name) | (df['AccentCity'] == city_name))]

    num_rows, _ = result_by_city.shape  # more than one row can be in the result
    if not result_by_city.empty:
        if num_rows == 1:
            latitude, longitude = result_by_city['Latitude'], result_by_city['Longitude']
        else:
            # if more than one row is in the result, check the country of offer
            result_by_country = result_by_city.loc[(df['CountryLong'] == country_name)]
            if not result_by_country.empty:
                latitude, longitude = result_by_country.iloc[0]['Latitude'], result_by_country.iloc[0]['Longitude']
            else:
                latitude, longitude = result_by_city.iloc[0]['Latitude'], result_by_city.iloc[0]['Longitude']
    else:
        # if the city cannot be found, put the marker in the center of the country:
        get_country = df.loc[(df['CountryLong'] == country_name)]
        num_rows_country, _ = get_country.shape
        if num_rows_country == 1:
            latitude, longitude = get_country['Latitude(average)'], get_country['Longitude(average)']
        else:
            latitude, longitude = get_country.iloc[0]['Latitude(average)'], get_country.iloc[0]['Longitude(average)']

    lat = float(latitude)
    lon = float(longitude)

    # save the location of offer
    for offer in offers:
        offer.location_latitude = lat
        offer.location_longitude = lon
        offer.save()


def set_color_of_offer(offer_type):
    match offer_type:
        case "COBE":
            return "#bb5afd"
        case "FCFS":
            return "#fdfa5a"
        case "PreAC":
            return "#5afdb2"
        case "AC":
            return "#0099ff"
        case default:
            return "#FFFFFF"


def create_popup_html(offer_list, offer_count, url_from_request):
    # adjust the url to details
    url_split = url_from_request.split("/")
    url_details = "http://" + url_split[2] + '/' + url_split[3] + '/offers/'

    rows = ""
    for offer in offer_list:
        color = set_color_of_offer(offer.offer_type)

        row = "<tr>"
        row += '<td class="popupRow" style="background-color:' + color + ';"><span>' + offer.ref_no + '</span></td>'

        row += '<td class="popupRow" style="background-color:' + color + ';"><span>' + offer.offer_type + '</span></td>'

        button = '<form action="' + \
                 url_details + offer.ref_no + \
                 '" method="get" target="_blank"> <button type="submit">Details </button> </form> '
        row += '<td class="popupRow" style="background-color: ' + color + ';"> ' + button + '</td>'

        row += "</tr>"
        rows += row

    if offer_count == 1:
        numberOfOffersInfo = "offer"
    else:
        numberOfOffersInfo = "offers"

    popup_html_code = """<!DOCTYPE html>
        <html>
        <head>
    
        </head>
            <h4 class="tableTitle"> """ + str(offer_count) + ' ' + numberOfOffersInfo + \
                      ' in ' + offer_list[0].location_city + ", " + offer_list[0].location_country + """</h4>
            <table id="popupTable">
            <thead>
                  <tr>
                    <th id="RefNoHeader" class="tableHeader">RefNo</th>
                    <th id="OfferTypeHeader" class="tableHeader">Type</th>
                    <th id="DetailsHeader" class="tableHeader">Details</th>
                  </tr>
            </thead>
                <tbody>
                """ + rows + """
                </tbody>
            </table>
        </html>
        """
    popup = folium.Popup(folium.Html(popup_html_code, script=True, width=230))
    return popup


def count_frequencies_of_cities(allOffers):
    freq = {}
    for offer in allOffers:
        if offer.location_city in freq:
            freq[offer.location_city] += 1
        else:
            freq[offer.location_city] = 1

    return freq


def add_styles_to_map(html_string):
    style_string = """
        <style>

        .tableTitle{
            font-size:1.6em;
            text-align:center;
            font-weight: bolder;
        }

        .tableHeader{
            text-align: center;
            border: 1px solid;
            font-size: 1.3em;
        }

        .popupRow{
            border: 1px solid;
            padding: 0.3em;
            font-size: 1.1em;
        }

        #popupTable{
            text-align: center;
            margin: auto;
        }
        """
    html_string = html_string.replace("<style>", style_string)
    return html_string


def create_map_for_offers(url_from_request):
    city_freq = count_frequencies_of_cities(Offer.objects.all())

    map_with_offers = folium.Map(
        location=[14, 16],
        zoom_start=4,
    )

    cities_df = get_cities_dataframe()
    for city, counter in city_freq.items():
        offers_in_this_city = list(Offer.objects.filter(location_city=city))

        # check if the location is already saved in the database
        # if offers_in_this_city[0].location_latitude is None and offers_in_this_city[0].location_longitude is None:
        get_city_location(cities_df, offers_in_this_city)

        popup = create_popup_html(offers_in_this_city, len(offers_in_this_city), url_from_request)

        latitude, longitude = offers_in_this_city[0].location_latitude, offers_in_this_city[0].location_longitude

        if not (latitude == 0 and longitude == 0):
            folium.Marker(location=[latitude, longitude], popup=popup,
                          icon=folium.Icon(color='blue', icon='university', prefix='fa')).add_to(map_with_offers)

    map_as_html = map_with_offers.get_root().render()
    map_as_html = add_styles_to_map(map_as_html)

    return map_as_html
