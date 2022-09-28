function addVerticalMenu(){
    document.getElementById("verticalMenuElement").innerHTML += "<!-- Menu vertical on the left side -->\n" +
        "<ul>\n" +
        "    <li><a href=\"http://127.0.0.1:8000/playground/hello/\">Offers list</a></li>\n" +
        "    <li><a href=\"http://127.0.0.1:8000/playground/map\" target=\"_blank\">Offers map</a></li>\n" +
        "    <li><a href=\"http://127.0.0.1:8000/playground/aboutProject\" >About project</a></li>\n" +
        "    <li><a href=\"http://127.0.0.1:8000/playground/aboutAuthor\">About author</a></li>\n" +
        "</ul>";

    }

function addAuthorFootnote(){
    document.getElementById("authorFootnote").innerHTML += "" +
        "<p> Author: Krzysztof Nazar</p>"
}

