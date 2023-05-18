# IAESTE Table offers analyzer - web application using Django framework

Author: Krzysztof Nazar

Check this project running live with Pythonanywhere [here](https://iaesteofferspoland.up.railway.app/iaesteTable/offers/).


## The goal of the project
**The goal of this project was to deploy a web application displaying IAESTE Poland offers for international internships. I wanted to make the searching process much more comfortable, faster and easier for the user.**

## Main functionalities for user
 - **Offers List** - Check every currently available offer. The table can be sorted and filtered. The user can select which columns are visible.
 - **Offers Map** - See the offers on the interactive map. A pin is set in every location where at least one offer is available. After clicking the button, user can go to details of selected offer.</li>
            

## IAESTE Association 

"The International Association for the Exchange of Students for Technical Experience, Association sans but lucratif (non-profit association), commonly known as IAESTE A.s.b.l. is an association of national committees representing academic, industrial and student interests. We serve 3500+ students, 3000 employers and 1000 academic institutions through career-focused professional internships abroad, social and intercultural reception programmes, international networking and other career and employer branding activities in more than 80 countries worldwide."

Text source: [link](https://iaeste.org/about)

## Description

When I heard about IAESTE, I wanted to check their website and see the offers they had. I found only two options:

1. Check PDFs - a single PDF contains information about one offer and before opening the PDF the user knows only the Ref. number of the offer, which is not important information when student is looking for an internship.

2. Use this [spreadsheet](https://iaeste.pl/offers). In my opinion, using it is extremely inconvenient, because the columns cannot be easily sorted or filtered, so the only way to look for offers is by using the "ctrl+f" method.

**Therefore, I created this project - I wanted to make the searching process much more comfortable, faster and easier for the user.**

**This web application is built using the Django framework.**


The major steps in this project were:
 1. Convert the IAESTE [spreadsheet](https://iaeste.pl/offers) into HTML code and extract information about each offer. 
 2. Create a model and database containing the information about the offers.
 3. Display the offers as a table. Each column can be filtered and sorted in ascending and descending order.
 4. Display the offers on an interactive world map. Each pin on the map corresponds to a city where an internship is available. After clicking the pin, a pop-up table appears, and the user can click a link to see details about the specific offer.

## Used libraries
 - Django
 - folium
 - geopy
 - NumPy
 - urllib

## Future improvements
 - Add more responsive CSS (for mobiles)

