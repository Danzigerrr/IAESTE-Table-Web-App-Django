from iaeste_table.models import Offer
import re
import pandas as pd


class OfferClass:

    def __init__(self, IdNumber=0, RefNo=0, Deadline=0, City=0, Country=0, GeneralDisciplines=0,
                 FieldsOfStudy=0, RequiredKnowledgeAndExperiences=0, OtherRequirements=0,
                 CompletedYearsOfStudy=0, LanguageRequirements=0, WorkWeeksMin=0,
                 WorkWeeksMax=0, From=0, To=0, AlternativeFrom=0, AlternativeTo=0,
                 CompanyClosedFrom=0, CompanyClosedTo=0, WorkOfferedDescription=0,
                 GrossPay=0, WorkingHours=0, Employer=0, Workplace=0, Website=0,
                 Lodgingby=0, LivingCost=0, EstCostofLodging=0,
                 AdditionalInfo=0, OfferType=0):
        self.IdNumber = IdNumber
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


class DataLoader:
    # url of spreasheet with IAESTE offers in Poland
    url = "https://docs.google.com/spreadsheets/d/e/2PACX-1vR6FjcG59djSQ_kWTfzDok-KPm_KtvwCKAz-J6h" \
          "-zUr_zTHb2m2AlHCDRNRGTUdMG19py_d4q0sMVQB/pubhtml?gid=1873904204&amp;single=true&amp;widget=true&amp" \
          ";headers=false "

    allOffersHTML = pd.DataFrame()

    def __init__(self):
        self.allOffersHTML = self.getOffersFromUrl()
        self.saveActiveOffers(self.allOffersHTML)
        self.deleteInactiveOffers(self.allOffersHTML)

    def getOffersFromUrl(self):
        df = pd.read_html(self.url, encoding='utf-8')[0]

        # adjust column names
        df.iloc[0] = df.iloc[0].str.replace(' ', '')
        df.iloc[0] = df.iloc[0].str.replace('.', '')
        df.columns = df.iloc[0]  # Convert row to column header
        df = df.drop(df.index[0])  # drop unneeded row
        df = df.drop(df.index[0])  # drop unneeded row

        df.columns.values[0] = "IdNumber"  # rename id column
        df['IdNumber'] = range(len(df))
        df.reset_index()
        return df

    def saveActiveOffers(self, offers):
        for index, offer in offers.iterrows():
            # print("saving " + str(offerHTML.RefNo))
            if Offer.objects.filter(RefNo=offer.RefNo).exists():
                # print("the offer " + str(offerHTML.RefNo) + " already exists in the DB")
                pass
            else:
                self.saveOfferToDB(offer)

    def saveOfferToDB(self, offer):
        offer = Offer(
            IdNumber=offer.IdNumber,
            RefNo=offer.RefNo,
            Deadline=offer.Deadline,
            City=str(offer.City).capitalize(),
            Country=offer.Country,
            GeneralDisciplines=offer.GeneralDisciplines,
            FieldsOfStudy=offer.FieldsOfStudy,
            RequiredKnowledgeAndExperiences=offer.RequiredKnowledgeAndExperiences,
            OtherRequirements=offer.OtherRequirements,
            CompletedYearsOfStudy=offer.CompletedYearsOfStudy,
            LanguageRequirements=offer.LanguageRequirements,
            WorkWeeksMin=offer.WorkWeeksMin,
            WorkWeeksMax=offer.WorkWeeksMax,
            From=offer.From,
            To=offer.To,
            AlternativeFrom=offer.AlternativeFrom,
            AlternativeTo=offer.AlternativeTo,
            CompanyClosedFrom=offer.CompanyClosedFrom,
            CompanyClosedTo=offer.CompanyClosedTo,
            WorkOfferedDescription=offer.WorkOfferedDescription,
            GrossPay=offer.GrossPay,
            WorkingHours=offer.WorkingHours,
            Employer=offer.Employer,
            Workplace=offer.Workplace,
            Website=offer.Website,
            LodgingBy=offer.Lodgingby,
            LivingCost=offer.LivingCost,
            EstCostOfLodging=offer.EstCostofLodging,
            AdditionalInfo=offer.AdditionalInfo,
            OfferType=offer.OfferType
        )
        offer.save()

    def deleteInactiveOffers(self, OffersFromUrl):
        OffersFromDB = Offer.objects.all()
        for offerDB in OffersFromDB:
            # print(offerDB.RefNo)
            inactive = True
            for index, offerUrl in OffersFromUrl.iterrows():
                if offerDB.RefNo == offerUrl.RefNo:
                    inactive = False
            if inactive:
                print("Offer with RefNo '{}' is inactive and can be deleted from the database".format(offerDB.RefNo))
                Offer.objects.filter(RefNo=offerDB.RefNo).delete()




