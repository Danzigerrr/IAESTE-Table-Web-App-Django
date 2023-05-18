from django.shortcuts import render
from scripts.map_handler import *
from datetime import date
import os


def main_list(request):
    from scripts import load_data_from_iaeste_spreadsheet as load
    load.DataLoader()
    from iaeste_table.models import Offer
    offer_list = Offer.objects.all()

    return render(request, "offers_list.html", {"offer_list": offer_list, "offer_list_len": len(offer_list)})


def detail(request, ref_no):
    from iaeste_table.models import Offer
    offer = Offer.objects.get(ref_no=ref_no)
    return render(request, "offer_detail.html", {"offer": offer})


def save_map_to_file(directory, file_to_save, folium_map_as_html):
    # create a directory if it does not exist
    if not os.path.exists(directory):
        # If it doesn't exist, create it
        os.makedirs(directory)
    with open(file_to_save, "w", encoding="utf-8") as text_file:
        text_file.write(folium_map_as_html)


def get_map(request):
    current_date = date.today()
    # currentDate = date(2023, 12, 10)  # debugging
    save_directory = 'saved_maps/'
    filename = "map_on_"
    save_format = '.txt'
    save_date = str(current_date)

    file_to_save = save_directory + filename + save_date + save_format

    file_exists = os.path.exists(file_to_save)
    if file_exists:
        with open(file_to_save, 'r', encoding='utf-8') as file:
            folium_map_as_html = file.read().replace('\n', '')

        return render(request, "offers_map.html", {"mapOfOffers": folium_map_as_html})
    else:
        directory_exists = os.path.isdir(save_directory)
        if directory_exists:
            for f in os.listdir(save_directory):
                os.remove(os.path.join(save_directory, f))  # delete the existing file

        current_url = request.build_absolute_uri()
        folium_map_as_html = create_map_for_offers(current_url)
        save_map_to_file(save_directory, file_to_save, folium_map_as_html)

        return render(request, "offers_map.html", {"mapOfOffers": folium_map_as_html})


def about_project(request):
    return render(request, "about_project.html")


def about_author(request):
    return render(request, "about_author.html")
