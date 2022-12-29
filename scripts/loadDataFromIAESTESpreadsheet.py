from iaesteTable.models import Offer
import re


class OfferClass:

    def __init__(self, RefNo=0, Deadline=0, City=0, Country=0, GeneralDisciplines=0,
                 FieldsOfStudy=0, RequiredKnowledgeAndExperiences=0, OtherRequirements=0,
                 CompletedYearsOfStudy=0, LanguageRequirements=0, WorkWeeksMin=0,
                 WorkWeeksMax=0, From=0, To=0, AlternativeFrom=0, AlternativeTo=0,
                 CompanyClosedFrom=0, CompanyClosedTo=0, WorkOfferedDescription=0,
                 GrossPay=0, WorkingHours=0, Employer=0, Workplace=0, Website=0, Lodgingby=0,
                 LivingCost=0, EstCostofLodging=0, AdditionalInfo=0, OfferType=0):
        self.RefNo = RefNo
        self.Deadline = Deadline
        self.City = City
        self.Country = Country
        self.GeneralDisciplines = GeneralDisciplines
        self.FieldsOfStudy = FieldsOfStudy
        self.RequiredKnowledgeAndExperiences = RequiredKnowledgeAndExperiences
        self.OtherRequirements = OtherRequirements
        self.CompletedYearsOfStudy = CompletedYearsOfStudy
        self.LanguageRequirements = LanguageRequirements
        self.WorkWeeksMin = WorkWeeksMin
        self.WorkWeeksMax = WorkWeeksMax
        self.From = From
        self.To = To
        self.AlternativeFrom = AlternativeFrom
        self.AlternativeTo = AlternativeTo
        self.CompanyClosedFrom = CompanyClosedFrom
        self.CompanyClosedTo = CompanyClosedTo
        self.WorkOfferedDescription = WorkOfferedDescription
        self.GrossPay = GrossPay
        self.WorkingHours = WorkingHours
        self.Employer = Employer
        self.Workplace = Workplace
        self.Website = Website
        self.Lodgingby = Lodgingby
        self.LivingCost = LivingCost
        self.EstCostofLodging = EstCostofLodging
        self.AdditionalInfo = AdditionalInfo
        self.OfferType = OfferType


def countOffers(html):
    begginningOfOfferId = "1873904204R"
    return html.count(begginningOfOfferId, 0, len(html))


def getPageAsHTML(url):
    from urllib.request import urlopen
    page = urlopen(url)
    html_bytes = page.read()  # get sequence of bytes
    html = html_bytes.decode("utf-8")  # decode bytes
    return html


def getCurrentOfferData(divided):
    currentOffer = OfferClass()
    for i in range(len(divided)):
        el = divided[i]
        match i:
            case 0:
                currentOffer.RefNo = el
            case 1:
                currentOffer.Deadline = el
            case 2:
                currentOffer.City = el
            case 3:
                currentOffer.Country = el
            case 4:
                currentOffer.GeneralDisciplines = el
            case 5:
                currentOffer.FieldsOfStudy = el
            case 6:
                currentOffer.RequiredKnowledgeAndExperiences = el
            case 7:
                currentOffer.OtherRequirements = el
            case 8:
                currentOffer.CompletedYearsOfStudy = el
            case 9:
                currentOffer.LanguageRequirements = el
            case 10:
                currentOffer.WorkWeeksMin = el
            case 11:
                currentOffer.WorkWeeksMax = el
            case 12:
                currentOffer.From = el
            case 13:
                currentOffer.To = el
            case 14:
                currentOffer.AlternativeFrom = el
            case 15:
                currentOffer.AlternativeTo = el
            case 16:
                currentOffer.CompanyClosedFrom = el
            case 17:
                currentOffer.CompanyClosedTo = el
            case 18:
                currentOffer.WorkOfferedDescription = el
            case 19:
                currentOffer.GrossPay = el
            case 20:
                currentOffer.WorkingHours = el
            case 21:
                currentOffer.Employer = el
            case 22:
                currentOffer.Workplace = el
            case 23:
                currentOffer.Website = el
            case 24:
                currentOffer.Lodgingby = el
            case 25:
                currentOffer.LivingCost = el
            case 26:
                currentOffer.EstCostofLodging = el
            case 27:
                currentOffer.AdditionalInfo = el
            case 28:
                currentOffer.OfferType = el
    return currentOffer


def getDataFromWebsite(url):
    html = getPageAsHTML(url)
    numberOfRows = countOffers(html)

    allOffers = []
    indexStart = '<th id=\"1873904204R'
    for i in range(1, numberOfRows):  # the first row contains names of columns
        indexCurrent = indexStart + str(i) + '\"'
        indexNext = indexStart + str(i + 1) + '\"'
        if i == (numberOfRows - 1):  # handle last offer
            indexNext = '</td></tr></tbody></table>'
        result = re.search(indexCurrent + '(.*)' + indexNext, html)

        offerAsText = result.group(1)
        offerDividedIntoFeatures = offerAsText.split("<td ")
        offerDividedIntoFeatures = offerDividedIntoFeatures[1:]  # the first part contains metadata

        removeMetadataFromOffer(offerDividedIntoFeatures)

        currentOffer = getCurrentOfferData(offerDividedIntoFeatures)

        if len(currentOffer.FieldsOfStudy) > 1:
            currentOffer.FieldsOfStudy = currentOffer.FieldsOfStudy.split(",")
        # printCurrentOffer(currentOffer)

        allOffers.append(currentOffer)

    return allOffers


def printCurrentOffer(currentOffer):
    print("CURRENT OFFER:")
    from pprint import pprint
    pprint(vars(currentOffer))


def removeMetadataFromOffer(offerFeatures):
    for i in range(len(offerFeatures)):
        # removing html tags
        offerFeatures[i] = offerFeatures[i].replace("class=\"s0\">", "")
        offerFeatures[i] = offerFeatures[i].replace("class=\"s1\">", "")
        offerFeatures[i] = offerFeatures[i].replace("</td>", "")
        offerFeatures[i] = offerFeatures[i].replace("</tr><tr style=\"height: 20px\">", "")
        offerFeatures[i] = offerFeatures[i].replace("&amp", "&")

        # get list of General Disciplines
        if i == 4:
            offerFeatures[i] = offerFeatures[i].split("<br>")

        # get list of Fields Of Study
        if i == 5:
            offerFeatures[i] = offerFeatures[i].split("<br>")

        # get list of Required Knowledge And Experiences
        if i == 6:
            offerFeatures[i] = offerFeatures[i].split("<br>")

        # get list of Other Requirements
        if i == 7:
            offerFeatures[i] = offerFeatures[i].split("<br>")

        # replace "<br> as a newline sign
        if i == 18:
            offerFeatures[i] = offerFeatures[i].replace("<br>", "\n")

        # get real link to the Website (delete the google docs link)
        if i == 23 and len(offerFeatures[i]) > 0:
            if "google" in offerFeatures[i]:  # link by google
                # get the website link only
                offerFeatures[i] = offerFeatures[i].split(">")[2]
                # delete "</a" from the end of the string
                offerFeatures[i] = offerFeatures[i][:len(offerFeatures[i]) - 3]
            else:
                offerFeatures[i] = offerFeatures[i].replace("//", "/")


def getDataFromWebsite(url):
    html = getPageAsHTML(url)
    numberOfRows = countOffers(html)

    allOffers = []
    indexStart = '<th id=\"1873904204R'
    for i in range(1, numberOfRows):  # the first row contains names of columns
        indexCurrent = indexStart + str(i) + '\"'
        indexNext = indexStart + str(i + 1) + '\"'
        if i == (numberOfRows - 1):  # handle last offer
            indexNext = '</td></tr></tbody></table>'
        result = re.search(indexCurrent + '(.*)' + indexNext, html)

        offerAsText = result.group(1)
        offerDividedIntoFeatures = offerAsText.split("<td ")
        offerDividedIntoFeatures = offerDividedIntoFeatures[1:]  # the first part contains metadata

        removeMetadataFromOffer(offerDividedIntoFeatures)

        currentOffer = getCurrentOfferData(offerDividedIntoFeatures)

        if len(currentOffer.FieldsOfStudy) > 1:
            currentOffer.FieldsOfStudy = currentOffer.FieldsOfStudy.split(",")
        # printCurrentOffer(currentOffer)

        allOffers.append(currentOffer)

    return allOffers


def splitSingleDisc(disc):
    if '-' in disc:
        disc = disc.split('-')[1].capitalize()
    return disc


def splitMultipleDisc(disc):
    if ',' in disc:
        splitted = disc.split(',')
        newlist = ""
        for s in splitted:
            s = splitSingleDisc(s)
            newlist = savingDiscToNewList(newlist, s, splitted)
        disc = deleteLastComma(newlist)
    return disc


def deleteLastComma(newlist):
    return newlist[:-3]  # deleting last comma from string


def savingDiscToNewList(newlist, s, splitted):
    newlist += str(s + ', \n').capitalize()
    return newlist


def adjustGenDiscipl(discipList):
    newdiscList = []
    for disc in discipList:
        if disc == "OTHER":
            disc = disc.capitalize()
        else:
            disc = splitMultipleDisc(disc)
            disc = splitSingleDisc(disc)
        newdiscList.append(disc)
    return newdiscList


def loadDataToDB():
    # url of spreasheet with IAESTE offers in Poland
    url = "https://docs.google.com/spreadsheets/d/e/2PACX-1vR6FjcG59djSQ_kWTfzDok-KPm_KtvwCKAz-J6h" \
          "-zUr_zTHb2m2AlHCDRNRGTUdMG19py_d4q0sMVQB/pubhtml?gid=1873904204&amp;single=true&amp;widget=true&amp" \
          ";headers=false "

    # get data of all offers from spreadsheet
    allOffersHTML = getDataFromWebsite(url)

    # list to save active offer
    activeOffersRefNumbers = []

    # check all offers that are currently in the spreadsheet
    saveActiveOffers(activeOffersRefNumbers, allOffersHTML)

    deleteInactiveOffers(activeOffersRefNumbers)


def saveActiveOffers(activeOffersRefNumbers, allOffersHTML):
    for offerHTML in allOffersHTML:
        # print("saving " + str(offerHTML.RefNo))
        activeOffersRefNumbers.append(offerHTML.RefNo)
        if Offer.objects.filter(RefNo=offerHTML.RefNo).exists():
            print("the offer " + str(offerHTML.RefNo) + " already exists in the DB")
        else:
            saveOfferToDB(offerHTML)


def deleteInactiveOffers(activeOffersRefNumbers):
    allOffersInDB = Offer.objects.all()
    for offerInDB in allOffersInDB:
        if offerInDB.RefNo not in activeOffersRefNumbers:
            print("deleting" + str(offerInDB.RefNo))
            Offer.objects.filter(RefNo=offerInDB.RefNo).delete()


def saveOfferToDB(offerHTML):
    offerHTML.GeneralDisciplines = adjustGenDiscipl(offerHTML.GeneralDisciplines)
    offer = Offer(RefNo=offerHTML.RefNo,
                  Deadline=offerHTML.Deadline,
                  City=str(offerHTML.City).capitalize(),
                  Country=offerHTML.Country,
                  GeneralDisciplines=(", ".join(offerHTML.GeneralDisciplines)),  # hiding brackets of list
                  FieldsOfStudy=(", ".join(offerHTML.FieldsOfStudy)),  # hiding brackets of list
                  RequiredKnowledgeAndExperiences=(", ".join(offerHTML.RequiredKnowledgeAndExperiences)).replace(
                      "*", "\n").replace("•", "\n"),
                  OtherRequirements=(", ".join(offerHTML.OtherRequirements)),
                  CompletedYearsOfStudy=offerHTML.CompletedYearsOfStudy,
                  LanguageRequirements=offerHTML.LanguageRequirements,
                  WorkWeeksMin=offerHTML.WorkWeeksMin,
                  WorkWeeksMax=offerHTML.WorkWeeksMax,
                  From=offerHTML.From,
                  To=offerHTML.To,
                  AlternativeFrom=offerHTML.AlternativeFrom,
                  AlternativeTo=offerHTML.AlternativeTo,
                  CompanyClosedFrom=offerHTML.CompanyClosedFrom,
                  CompanyClosedTo=offerHTML.CompanyClosedTo,
                  WorkOfferedDescription=offerHTML.WorkOfferedDescription,
                  GrossPay=offerHTML.GrossPay,
                  WorkingHours=offerHTML.WorkingHours,
                  Employer=offerHTML.Employer,
                  Workplace=offerHTML.Workplace,
                  Website=offerHTML.Website,
                  LodgingBy=offerHTML.Lodgingby,
                  LivingCost=offerHTML.LivingCost,
                  EstCostOfLodging=offerHTML.EstCostofLodging,
                  AdditionalInfo=offerHTML.AdditionalInfo,
                  OfferType=offerHTML.OfferType,

                  )
    offer.save()
