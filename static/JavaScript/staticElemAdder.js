function addVerticalMenu(){


    document.getElementById("verticalMenuElement").innerHTML +=
        "<link rel=\"stylesheet\" href=\"https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css\">\n" +
        "    <div class=\"topnav\" id=\"myTopnav\">\n" +
        "    <a href=\"https://iaeste-offers-django-web-appkn.herokuapp.com/iaesteTable/offers\">Offers list</a>\n" +
        "    <a href=\"https://iaeste-offers-django-web-appkn.herokuapp.com/iaesteTable/map\" target=\"_blank\">Offers map</a>\n" +
        "    <a href=\"https://iaeste-offers-django-web-appkn.herokuapp.com/iaesteTable/aboutProject\" target=\"_blank\">About project</a>\n" +
        "    <a href=\"https://iaeste-offers-django-web-appkn.herokuapp.com/iaesteTable/aboutAuthor\" target=\"_blank\">About author</a>\n" +
        "      <a href=\"javascript:void(0);\" class=\"icon\" onclick=\"menuMyFunction()\">\n" +
        "        <i class=\"fa fa-bars\"></i>\n" +
        "      </a>\n" +
        "    </div>"

}


function addAuthorFootnote(){
    document.getElementById("authorFootnote").innerHTML += "" +
        "<p> Author: Krzysztof Nazar - check my <a style=\"color:white\" href=\"https://github.com/KrzysztofNazar01\" target=\"_blank\">GitHub</a>" +
        "</p>"

}


        /* Toggle between adding and removing the "responsive" class to topnav when the user clicks on the icon */
function menuMyFunction() {
      var x = document.getElementById("myTopnav");
      if (x.className === "topnav") {
        x.className += " responsive";
      } else {
        x.className = "topnav";
      }
    }