import folium as folium


def findGeocode(city):
    from geopy.exc import GeocoderTimedOut
    from geopy.geocoders import Nominatim
    import numpy as np
    # try and catch is used to overcome
    # the exception thrown by geolocator
    # using geocodertimedout
    try:
        # Specify the user_agent as your
        # app name it should not be none
        geolocator = Nominatim(user_agent="your_app_name")
        return geolocator.geocode(city)

    except GeocoderTimedOut:
        return findGeocode(city)


def getLatAndLong(cityName):
    '''

    :param cityName:
    :return:
        - latitude
        - longitude
        - if returned latitude and longitude equal 0, the city is not marked on the map
    '''
    import numpy as np
    loc = findGeocode(cityName)

    if loc != None:
        return loc.latitude, loc.longitude
    else:
        return 0, 0


def createMap(cityName):
    import folium
    latitude, longitude = getLatAndLong(cityName)

    # adjust position of view of the map
    my_map = folium.Map(
        location=[13, 16],
        zoom_start=2,
    )

    if latitude != 0 and longitude != 0:
        # set marker for the offer
        # html = popup_html(offer)
        # popup = folium.Popup(folium.Html(html, script=True), max_width=500)
        folium.Marker(location=[latitude, longitude],
                      icon=folium.Icon(color='blue', icon='university', prefix='fa')).add_to(my_map)

    return my_map


# ---------------------

def setColorOfOffer(offerType):
    match offerType:
        case "COBE":
            return "#bb5afd"
        case "FCFS":
            return "#fdfa5a"
        case "PreAC":
            return "#5afdb2"
        case default:
            return "#FFFFFF"


def popup_html(offerList, offerCount, city, urlFromRequest):
    # adjust the url to details
    splitted = urlFromRequest.split("/")
    urlToDetails = splitted[0] + "//" + splitted[2] + '/' + splitted[3] + '/offers/'

    rows = ""
    for offer in offerList:
        color = setColorOfOffer(offer.OfferType)

        row = "<tr>"
        row += '<td style="border: 1px solid; padding: 0.3em; font-size:1.1em; background-color:' + color + ';"><span>' + offer.RefNo + '</span></td>'
        row += '<td style="border: 1px solid; padding: 0.3em; font-size:1.1em; background-color:' + color + ';"><span>' + offer.OfferType + '</span></td>'

        button = '<form action="' + \
                 urlToDetails + offer.RefNo + \
                 '" method="get" target="_blank"> <button type="submit">Details </button> </form> '

        row += '<td style="border: 1px solid; padding: 0.3em; font-size:1.1em; background-color: ' + color + ';"> ' + button + '</td>'
        row += "</tr>"
        rows += row

    offersInfo = "offer"
    if offerCount > 1:
        offersInfo += "s"

    html = """<!DOCTYPE html>
        <html>
        <head>
            <h4 class="tableHeader" style="font-size:1.6em; text-align:center; font-weight: bolder;"> """ + str(
        offerCount) + ' ' + offersInfo + ' in ' + city + """</h4>

        </head>
            <table id="popupTable" style="border: 1px solid; width: auto; padding: 0.2em;">
            <thead>
                  <tr>
                    <th id="RefNoHeader" style="text-align: center; border: 1px solid; width: auto; font-size: 1.3em;">RefNo</th>
                    <th id="OfferTypeHeader" style="text-align: center; border: 1px solid; width: auto; font-size: 1.3em;" >Type</th>
                    <th id="DetailsHeader" style="text-align: center; border: 1px solid; width: auto; font-size: 1.3em;">Details</th>
                  </tr>
            </thead>
                <tbody>
                """ + rows + """
                </tbody>
            </table>
        </html>
        """
    return html


def countFrequenciesOfCities(allOffers):
    # Creating an empty dictionary
    freq = {}
    for offer in allOffers:
        if (offer.City in freq):
            freq[offer.City] += 1
        else:
            freq[offer.City] = 1

    return freq


def createMapForMultipleOffers(urlFromRequest):
    from iaesteTable.models import Offer
    allOffers = Offer.objects.all()

    cityFreq = countFrequenciesOfCities(allOffers)

    import folium

    my_map = folium.Map(
        location=[13, 16],
        zoom_start=2,
    )

    for city, counter in cityFreq.items():
        offerList = list(Offer.objects.filter(City=city))

        lat, long = getLatAndLong(city)

        # set marker for the offer
        html = popup_html(offerList, counter, city, urlFromRequest)
        popup = folium.Popup(folium.Html(html, script=True))
        folium.Marker(location=[lat, long], popup=popup,
                      icon=folium.Icon(color='blue', icon='university', prefix='fa')).add_to(my_map)

    return my_map
