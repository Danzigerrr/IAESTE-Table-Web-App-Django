import folium
from django.shortcuts import render
from scripts.mapHandler import *
from datetime import date
import os


def mainList(request):
    from scripts import loadDataFromIAESTESpreadsheet as load
    load.DataLoader()
    from iaeste_table.models import Offer
    offer_list = Offer.objects.all()

    return render(request, "mainList_view_1.html", {"offer_list": offer_list, "offer_list_len": len(offer_list)})


def detail(request, RefNo):
    from iaeste_table.models import Offer
    offer = Offer.objects.get(RefNo=RefNo)
    return render(request, "detail_view_1.html", {"offer": offer})


def get_map(request):
    currentDate = date.today()
    currentDate = date(2023, 12, 10)  # debugging
    savingDirectory = 'savedMaps/'

    ## create a directory if it does not exist
    # Check if the directory exists
    if not os.path.exists(savingDirectory):
        # If it doesn't exist, create it
        os.makedirs(savingDirectory)

    filename = "map_on_" + str(currentDate) + ".txt"
    path = savingDirectory + filename
    file_exists = os.path.exists(path)
    if file_exists:
        with open(path, 'r', encoding='utf-8') as file:
            folium_map_as_html = file.read().replace('\n', '')

        return render(request, "map_view_1.html", {"mapOfOffers": folium_map_as_html})
    else:
        # delete the existing file
        for f in os.listdir(savingDirectory):
            os.remove(os.path.join(savingDirectory, f))

        currentUrl = request.build_absolute_uri()
        folium_map_as_html = createMapForOffers(currentUrl)
        return render(request, "map_view_1.html", {"mapOfOffers": folium_map_as_html})


def aboutProject(request):
    return render(request, "aboutProject_view_1.html")


def aboutAuthor(request):
    return render(request, "aboutAuthor_view_1.html")
