from django.shortcuts import render
from django.http import HttpResponse
from scripts.mapHandler import *

def say_hello(request):
    from scripts import loadFromCSV as load
    load.run()
    from playground.models import Offer
    offer_list = Offer.objects.all()

    return render(request, "playground_view_1.html", {"offer_list": offer_list})



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


def vote(request, question_id):
    tostr = str(question_id)
    return render(request, "view2.html", {"name": tostr})


def map(request):
    map = createMapForMultipleOffers()
    html_string = map.get_root().render()
    return render(request, "map_view_1.html", {"map": html_string})
