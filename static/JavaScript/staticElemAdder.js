function getBaseUrl(){
    const currentUrl = window.location.href; // get current url
    // console.log(currentUrl)
    const urlInParts = currentUrl.split('/', 4);
    // console.log(urlInParts);
    return urlInParts[2] + "/" + urlInParts[3] + "/";
}

         // horiznotal menu - add links to buttons
         function addLinksToMenu(){
         	const baseUrl = getBaseUrl();
         	// create link for every menu option
         	const menuLinkOfferList =  'http://' + baseUrl + 'offers/' ;
         	const menuLinkOfferMap =  'http://' + baseUrl + 'map/' ;
         	const menuLinkAboutProject = 'http://' + baseUrl + 'about-project/';
         	const menuLinkAboutAuthor= 'http://' + baseUrl + 'about-author/';
         	const menuLinkIaestePoland= 'https://www.iaeste.pl/';

         	document.getElementById("menu-link-offers").href=menuLinkOfferList;

         	document.getElementById("menu-link-map").href=menuLinkOfferMap;
         	document.getElementById("menu-link-map").target="_blank";

         	document.getElementById("menu-link-about-project").href=menuLinkAboutProject;
         	document.getElementById("menu-link-about-project").target="_blank";

         	document.getElementById("menu-link-about-author").href=menuLinkAboutAuthor;
         	document.getElementById("menu-link-about-author").target="_blank";

         	document.getElementById("menu-link-iaeste-poland").href=menuLinkIaestePoland;
         	document.getElementById("menu-link-iaeste-poland").target="_blank";

                      // adjust the active menu button --> current page
         	const currentUrl = window.location.href;
         	switch(currentUrl) {
         	  case menuLinkOfferList:
         		document.getElementById("menu-link-offers").classList.add("active");
         		break;
         	  case menuLinkOfferMap:
         		document.getElementById("menu-link-map").classList.add("active");
         		break;
         	  case menuLinkAboutProject:
         		document.getElementById("menu-link-about-project").classList.add("active");
         		break;
         	  case menuLinkAboutAuthor:
         		document.getElementById("menu-link-about-author").classList.add("active");
         		break;
         	  default:
         		document.getElementById("menu-link-offers").classList.add("active");
         	}
                  }