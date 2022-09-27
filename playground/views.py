from django.shortcuts import render
from django.http import HttpResponse


def say_hello(request):
    from scripts import loadFromCSV as load
    load.run()
    from playground.models import Offer
    offer_list = Offer.objects.all()

    return render(request, "playground_view_1.html", {"offer_list": offer_list})


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

def getLongAndLat(cityName):
    import numpy as np
    loc = findGeocode(cityName)

    if loc != None:
        return loc.latitude, loc.longitude
    else:
        return 0,0

def createMap(cityName):
    import folium
    print('city:' + cityName)
    latitude, longitude = getLongAndLat(cityName)
    print('long lat:' + str(longitude) + " " + str(latitude))
    # adjust position of view of the map
    my_map = folium.Map(
        location=[13, 16],
        zoom_start=2,
    )

    # set marker for the offer
    #html = popup_html(offer)
    #popup = folium.Popup(folium.Html(html, script=True), max_width=500)
    folium.Marker(location=[latitude, longitude],
                  icon=folium.Icon(color='blue', icon='university', prefix='fa')).add_to(my_map)

    # save the map
    my_map.save("map.html")
    return my_map

    # open the map
    # webbrowser.open("map.html")


def findCityOfOfferWithId(question_id):
    import pandas as pd
    df = pd.read_csv("AllOffers_21_09_2022.csv")
    offer = df.loc[df['RefNo'] == question_id]
    return str(offer["City"].item())


def city(request, question_id):
    cityName = findCityOfOfferWithId(question_id)
    map = createMap(cityName)
    map.save("map.html")
    html_string = map.get_root().render()
    return render(request, "city_view_1.html", {"map": html_string})


def detail(request, question_id):
    from playground.models import Offer
    offer = Offer.objects.get(RefNo=question_id)
    return render(request, "detail_view_1.html", {"offer": offer})


def results(request, question_id):
    return HttpResponse("This is the result of the question: %s" % question_id)


def vote(request, question_id):
    tostr = str(question_id)
    return render(request, "view2.html", {"name": tostr})
