import folium
from django.shortcuts import render
from scripts.mapHandler import *
from datetime import date
import os


def mainList(request):
    from scripts import loadDataFromIAESTESpreadsheet as load
    load.loadDataToDB()
    from iaesteTable.models import Offer
    offer_list = Offer.objects.all()

    return render(request, "mainList_view_1.html", {"offer_list": offer_list, "offer_list_len": len(offer_list)})


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


def getMap(request):
    result = getMap_createNewMapEveryTime(request)
    # result = getMap_mapWithCaching(request)
    return result


def getMap_createNewMapEveryTime(request):
    currentDate = date.today()
    # currentDate = date(2022, 12, 10)  # debugging
    savingDirectory = 'generatedMaps/'
    filename = "map_with_offers_"
    #templateToDisplay = "map_view_1.html"
    templateToDisplay = "map_view_loading.html"
    currentUrl = request.build_absolute_uri()
    # mapFolium = createMapForMultipleOffers(currentUrl)
    mapFolium = folium.Map()
    mapFolium.save(savingDirectory + filename + str(currentDate) + ".html")
    html_string = mapFolium.get_root().render()
    #return render(request, templateToDisplay, {"mapOfOffers": html_string})
    return render(request, templateToDisplay, {"mapOfOffers": html_string})


def getMap_mapWithCaching(request):
    currentDate = date.today()
    # currentDate = date(2022, 12, 10)  # debugging
    savingDirectory = 'generatedMaps/'
    filename = "map_with_offers_"
    templateToDisplay = "map_view_1.html"
    # templateToDisplay = "map_view_loading.html"
    # read current map
    res = []  # list to store files
    # Iterate directory
    for path in os.listdir(savingDirectory):
        # check if current path is a file
        if os.path.isfile(os.path.join(savingDirectory, path)):
            res.append(path)
    # print(res)
    currentMapIsUpToDate = False
    if len(res) > 0:
        if res[0] == filename + str(currentDate) + ".html":
            currentMapIsUpToDate = True

    if currentMapIsUpToDate:
        # print("using already generated map")
        html_as_string = ""
        filepath = savingDirectory + res[0]
        with open(filepath, 'r') as file:
            html_as_string = file.read().replace('\n', '')
        return render(request, templateToDisplay, {"mapOfOffers": html_as_string})
    else:
        # print('the date is different - deleting existing map')
        import shutil
        for filename in os.listdir(savingDirectory):
            file_path = os.path.join(savingDirectory, filename)
            try:
                if os.path.isfile(file_path) or os.path.islink(file_path):
                    os.unlink(file_path)
                elif os.path.isdir(file_path):
                    shutil.rmtree(file_path)
            except Exception as e:
                print('Failed to delete %s. Reason: %s' % (file_path, e))
        # print("create new map")
        currentUrl = request.build_absolute_uri()
        mapFolium = createMapForMultipleOffers(currentUrl)
        mapFolium.save(savingDirectory + filename + str(currentDate) + ".html")
        html_string = mapFolium.get_root().render()
        return render(request, templateToDisplay, {"mapOfOffers": html_string})

def aboutProject(request):
    return render(request, "aboutProject_view_1.html")


def aboutAuthor(request):
    return render(request, "aboutAuthor_view_1.html")
