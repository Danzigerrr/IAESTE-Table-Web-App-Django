from playground.models import Offer
import csv


def run():
    with open('AllOffers_21_09_2022.csv', 'r', encoding='UTF-8', newline='') as file:
        reader = csv.reader(file)

        next(reader)  # skip the row with column names

        Offer.objects.all().delete()  # clear DB

        for row in reader:
            offer = Offer(RefNo=row[0],
                          Deadline=row[1],
                          City=row[2],
                          Country=row[3],
                          GeneralDisciplines=row[4],
                          FieldsOfStudy=row[5],
                          RequiredKnowledgeAndExperiences=row[6],
                          OtherRequirements=row[7],
                          CompletedYearsOfStudy=row[8],
                          LanguageRequirements=row[9],
                          WorkWeeksMin=row[10],
                          WorkWeeksMax=row[11],
                          From=row[12],
                          To=row[13],
                          AlternativeFrom=row[14],
                          AlternativeTo=row[15],
                          CompanyClosedFrom=row[16],
                          CompanyClosedTo=row[17],
                          WorkOfferedDescription=row[18],
                          GrossPay=row[19],
                          WorkingHours=row[20],
                          Employer=row[21],
                          Workplace=row[22],
                          Website=row[23],
                          LodgingBy=row[24],
                          LivingCost=row[25],
                          EstCostOfLodging=row[26],
                          AdditionalInfo=row[27],
                          OfferType=row[28],

                          )
            offer.save()
