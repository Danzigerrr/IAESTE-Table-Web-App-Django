function getBaseUrl(){
    const currentUrl = window.location.href; // get current url
    // console.log(currentUrl)
    const urlInParts = currentUrl.split('/', 4);
    // console.log(urlInParts);
    return urlInParts[2] + "/" + urlInParts[3] + "/";
}

function addVerticalMenu(){
    // get base url
    const baseUrl = getBaseUrl();

    // create link for every menu option
    const menuLinkOfferList = '\"' + 'http://' + baseUrl + 'offers/' + '\"'
    const menuLinkOfferMap = '\"' + 'http://' + baseUrl + 'map/' + '\"'
    const menuLinkAboutProject = '\"' + 'http://' + baseUrl + 'about_project/' + '\"'
    const menuLinkAboutAuthor= '\"' + 'http://' + baseUrl + 'about_author/' + '\"'

    // create the menu and insert the links
    document.getElementById("verticalMenuElement").innerHTML +=
        "<link rel=\"stylesheet\" href=\"https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css\">\n" +
        "    <div class=\"topnav\" id=\"myTopnav\">\n" +
        "    <a href=" + menuLinkOfferList + ">Offers list</a>\n" +
        "    <a href=" + menuLinkOfferMap + " target=\"_blank\">Offers map</a>\n" +
        "    <a href=" + menuLinkAboutProject + ">About project</a>\n" +
        "    <a href=" + menuLinkAboutAuthor + ">About author</a>\n" +
        "      <a href=\"javascript:void(0);\" class=\"icon\" onclick=\"responsiveMenuToggle()\">\n" +
        "        <i class=\"fa fa-bars\"></i>\n" +
        "      </a>\n" +
        "    </div>"

}

function addAuthorFootnote(){
    document.getElementById("authorFootnote").innerHTML += "" +
        "<p> Author: Krzysztof Nazar - check my <a style=\"color:white\" href=\"https://github.com/KrzysztofNazar01\" target=\"_blank\">GitHub</a>" +
        "</p>"

}

/* Toggle between adding and removing the "responsive"
class to topnav when the user clicks on the icon */
function responsiveMenuToggle() {
      var x = document.getElementById("myTopnav");
      if (x.className === "topnav") {
        x.className += " responsive";
      } else {
        x.className = "topnav";
      }
    }
