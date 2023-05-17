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


def saveMapToFile(directory, file_to_save):
    ## create a directory if it does not exist
    # Check if the directory exists
    if not os.path.exists(directory):
        # If it doesn't exist, create it
        os.makedirs(directory)
    with open(file_to_save, "w", encoding="utf-8") as text_file:
        text_file.write(html_string)


def get_map(request):
    currentDate = date.today()
    currentDate = date(2023, 12, 10)  # debugging
    save_directory = 'savedMaps/'
    filename = "map_on_"
    save_format = '.txt'
    save_date = str(currentDate)

    file_to_save = save_directory + filename + save_date + save_format

    file_exists = os.path.exists(file_to_save)
    if file_exists:
        with open(file_to_save, 'r', encoding='utf-8') as file:
            folium_map_as_html = file.read().replace('\n', '')

        return render(request, "map_view_1.html", {"mapOfOffers": folium_map_as_html})
    else:
        # delete the existing file
        for f in os.listdir(save_directory):
            os.remove(os.path.join(save_directory, f))

        currentUrl = request.build_absolute_uri()
        folium_map_as_html = createMapForOffers(currentUrl)
        saveMapToFile(save_directory, file_to_save)
        return render(request, "map_view_1.html", {"mapOfOffers": folium_map_as_html})


def aboutProject(request):
    return render(request, "aboutProject_view_1.html")


def aboutAuthor(request):
    return render(request, "aboutAuthor_view_1.html")
