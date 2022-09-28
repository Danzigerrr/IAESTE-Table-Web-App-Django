from django.shortcuts import render
from scripts.mapHandler import *

def say_hello(request):
    from scripts import loadDataFromIAESTESpreadsheet as load
    load.run()
    from playground.models import Offer
    offer_list = Offer.objects.all()

    return render(request, "playground_view_1.html", {"offer_list": offer_list})



def findCityOfOfferWithId(question_id):
    from playground.models import Offer
    offer = Offer.objects.get(RefNo=question_id)
    return str(offer.City)


def city(request, question_id):
    cityName = findCityOfOfferWithId(question_id)
    map = createMap(cityName)
    html_string = map.get_root().render()
    return render(request, "city_view_1.html", {"map": html_string})


def detail(request, question_id):
    from playground.models import Offer
    offer = Offer.objects.get(RefNo=question_id)
    return render(request, "detail_view_1.html", {"offer": offer})


def map(request):
    map = createMapForMultipleOffers()
    html_string = map.get_root().render()
    return render(request, "map_view_1.html", {"map": html_string})
