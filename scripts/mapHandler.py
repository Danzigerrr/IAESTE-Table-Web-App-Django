import folium
from iaeste_table.models import Offer
from datetime import date
import os

def getCoordinatesOfCity(city, country):
    from geopy.exc import GeocoderTimedOut
    from geopy.geocoders import Nominatim
    # Specify the user_agent as your
    # app name it should not be none
    geolocator = Nominatim(user_agent="iaeste_table")
    location = geolocator.geocode(city + ', ' + country, timeout=2000)
    if location is None:
        return 0, 0
    return location.latitude, location.longitude


def setColorOfOffer(offerType):
    match offerType:
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


def popup_html(offerList, offerCount, urlFromRequest):
    # adjust the url to details
    splittedUrl = urlFromRequest.split("/")

    # TODO: this might be changed to 'http://' or 'splittedUrl[0]
    urlToDetails = "http://" + splittedUrl[2] + '/' + splittedUrl[3] + '/offers/'

    rows = ""
    for offer in offerList:
        color = setColorOfOffer(offer.OfferType)

        row = "<tr>"
        row += '<td class="popupRow" style="background-color:' + color + ';"><span>' + offer.RefNo + '</span></td>'

        row += '<td class="popupRow" style="background-color:' + color + ';"><span>' + offer.OfferType + '</span></td>'

        button = '<form action="' + \
                 urlToDetails + offer.RefNo + \
                 '" method="get" target="_blank"> <button type="submit">Details </button> </form> '
        row += '<td class="popupRow" style="background-color: ' + color + ';"> ' + button + '</td>'

        row += "</tr>"
        rows += row

    if offerCount == 1:
        numberOfOffersInfo = "offer"
    else:
        numberOfOffersInfo = "offers"


    popup_html_code = """<!DOCTYPE html>
        <html>
        <head>
    
        </head>
            <h4 class="tableTitle"> """ + str(offerCount) + ' ' + numberOfOffersInfo +\
                      ' in ' + offerList[0].City + ", " + offerList[0].Country + """</h4>
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


def countFrequenciesOfCities(allOffers):
    # Creating an empty dictionary
    freq = {}
    for offer in allOffers:
        if offer.City in freq:
            freq[offer.City] += 1
        else:
            freq[offer.City] = 1

    return freq


def addStylesToMap(html_string):
    styleString = """
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
    html_string = html_string.replace("<style>", styleString)
    return html_string


def saveMapToFile(html_string):
    today = date.today()
    savingDirectory = 'savedMaps/'

    ## create a directory if it does not exist
    # Check if the directory exists
    if not os.path.exists(savingDirectory):
        # If it doesn't exist, create it
        os.makedirs(savingDirectory)

    filename = "map_on_" + str(today) + ".txt"
    with open(directory + filename, "w", encoding="utf-8") as text_file:
        text_file.write(html_string)


def createMapForOffers(urlFromRequest):
    allOffers = Offer.objects.all()

    cityFreq = countFrequenciesOfCities(allOffers)

    mapWithOffers = folium.Map(
        location=[13, 16],
        zoom_start=2,
    )

    for city, counter in cityFreq.items():
        offersInThisCity = list(Offer.objects.filter(City=city))

        lat, long = getCoordinatesOfCity(city, offersInThisCity[0].Country)

        popup = popup_html(offersInThisCity, len(offersInThisCity), urlFromRequest)

        folium.Marker(location=[lat, long], popup=popup,
                      icon=folium.Icon(color='blue', icon='university', prefix='fa')).add_to(mapWithOffers)

    html_string = mapWithOffers.get_root().render()

    html_string = addStylesToMap(html_string)

    saveMapToFile(html_string)

    return html_string



