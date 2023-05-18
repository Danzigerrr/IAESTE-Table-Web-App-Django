import folium
from iaeste_table.models import Offer
from geopy.geocoders import Nominatim


def get_coordinates_of_city(offers: list):
    # Specify the user_agent as your
    # app name it should not be none
    city = offers[0].location_city
    country = offers[0].location_country
    print("city: ")
    geolocator = Nominatim(user_agent="iaeste_table")
    location = geolocator.geocode(city + ', ' + country, timeout=2000)
    if location is None:
        return 0, 0
    for offer in offers:
        offer.location_latitude = location.latitude
        offer.location_longitude = location.longitude
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
    # Creating an empty dictionary
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
        location=[13, 16],
        zoom_start=2,
    )

    for city, counter in city_freq.items():
        offers_in_this_city = list(Offer.objects.filter(location_city=city))

        # check if the location is already saved in the database
        if offers_in_this_city[0].location_latitude is None and offers_in_this_city[0].location_longitude is None:
            get_coordinates_of_city(offers_in_this_city)

        popup = create_popup_html(offers_in_this_city, len(offers_in_this_city), url_from_request)

        latitude, longitude = offers_in_this_city[0].location_latitude, offers_in_this_city[0].location_longitude

        folium.Marker(location=[latitude, longitude], popup=popup,
                      icon=folium.Icon(color='blue', icon='university', prefix='fa')).add_to(map_with_offers)

    map_as_html = map_with_offers.get_root().render()

    map_as_html = add_styles_to_map(map_as_html)

    return map_as_html
