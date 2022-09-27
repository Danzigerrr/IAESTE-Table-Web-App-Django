function addVerticalMenu(){
    document.getElementById("verticalMenuElement").innerHTML += "<!-- Menu vertical on the left side -->\n" +
        "<ul>\n" +
        "    <li><a href=\"http://127.0.0.1:8000/playground/hello/\">Offers list</a></li>\n" +
        "    <li><a href=\"http://127.0.0.1:8000/playground/map\">Offers map</a></li>\n" +
        "    <li><a href=\"about.asp\">About project</a></li>\n" +
        "    <li><a href=\"contact.asp\">About author</a></li>\n" +
        "</ul>";

    }

function addAuthorFootnote(){
    document.getElementById("authorFootnote").innerHTML += "" +
        "<p> Author: Krzysztof Nazar</p>"
}

