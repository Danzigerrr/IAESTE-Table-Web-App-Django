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
                          City=row[2]
                          )
            offer.save()

