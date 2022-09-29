function addVerticalMenu(){
    document.getElementById("verticalMenuElement").innerHTML += "<!-- Menu vertical on the left side -->\n" +
        "<ul>\n" +
        "    <li><a href=\"https://iaeste-offers-django-web-appkn.herokuapp.com/iaesteTable/offers\">Offers list</a></li>\n" +
        "    <li><a href=\"https://iaeste-offers-django-web-appkn.herokuapp.com/iaesteTable/map\" target=\"_blank\">Offers map</a></li>\n" +
        "    <li><a href=\"https://iaeste-offers-django-web-appkn.herokuapp.com/iaesteTable/aboutProject\" target=\"_blank\">About project</a></li>\n" +
        "    <li><a href=\"https://iaeste-offers-django-web-appkn.herokuapp.com/iaesteTable/aboutAuthor\" target=\"_blank\">About author</a></li>\n" +
        "</ul>";

    }

function addAuthorFootnote(){
    document.getElementById("authorFootnote").innerHTML += "" +
        "<p> Author: Krzysztof Nazar</p>"
}

