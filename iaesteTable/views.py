from django.shortcuts import render
from scripts.mapHandler import *


def mainList(request):
    from scripts import loadDataFromIAESTESpreadsheet as load
    load.loadDataToDB()
    from iaesteTable.models import Offer
    offer_list = Offer.objects.all()

    return render(request, "mainList_view_1.html", {"offer_list": offer_list})


def findCityOfOfferWithId(RefNo):
    from iaesteTable.models import Offer
    offer = Offer.objects.get(RefNo=RefNo)
    return str(offer.City)


def city(request, RefNo):
    cityName = findCityOfOfferWithId(RefNo)
    map = createMap(cityName)
    html_string = map.get_root().render()
    return render(request, "city_view_1.html", {"map": html_string})


def detail(request, RefNo):
    from iaesteTable.models import Offer
    offer = Offer.objects.get(RefNo=RefNo)
    return render(request, "detail_view_1.html", {"offer": offer})


def map(request):
    map = createMapForMultipleOffers()
    html_string = map.get_root().render()
    return render(request, "map_view_1.html", {"map": html_string})


def aboutProject(request):
    return render(request, "aboutProject_view_1.html")


def aboutAuthor(request):
    return render(request, "aboutAuthor_view_1.html")
