from iaeste_table.models import Offer
import re
import pandas as pd


class DataLoader:
    # url of spreasheet with IAESTE offers in Poland
    url = "https://docs.google.com/spreadsheets/d/e/2PACX-1vR6FjcG59djSQ_kWTfzDok-KPm_KtvwCKAz-J6h" \
          "-zUr_zTHb2m2AlHCDRNRGTUdMG19py_d4q0sMVQB/pubhtml?gid=1873904204&amp;single=true&amp;widget=true&amp" \
          ";headers=false "

    allOffersHTML = pd.DataFrame()

    def __init__(self):
        self.allOffersHTML = self.get_offers_from_url()
        self.save_active_offers(self.allOffersHTML)
        self.delete_inactive_offers_from_database(self.allOffersHTML)

    def to_snake_case(self, name):
        name = re.sub('(.)([A-Z][a-z]+)', r'\1_\2', name)
        name = re.sub('__([A-Z])', r'_\1', name)
        name = re.sub('([a-z0-9])([A-Z])', r'\1_\2', name)
        return name.lower()

    def get_offers_from_url(self):
        df = pd.read_html(self.url, encoding='utf-8')[0]

        # adjust column names
        df.iloc[0] = df.iloc[0].str.replace(' ', '')
        df.iloc[0] = df.iloc[0].str.replace('.', '')
        df.columns = df.iloc[0]  # Convert row to column header
        df = df.drop(df.index[0])  # drop unneeded row
        df = df.drop(df.index[0])  # drop unneeded row
        df = df.iloc[:, 1:]  # drop the first column

        # rename column names
        column_names_old = list(df.columns.values)
        column_names_new = []
        for column_name in column_names_old:
            new_name = self.to_snake_case(column_name)
            column_names_new.append(new_name)
        df.columns = column_names_new
        df.rename(columns={'city': 'location_city',
                           'country': 'location_country',
                           'from': 'date_from',
                           'to': 'date_to',
                           'lodgingby': 'lodging_by',
                           'est_costof_lodging': 'est_cost_of_lodging'},
                  inplace=True)

        df = df.reset_index()

        return df

    def save_active_offers(self, offers):
        for index, offer in offers.iterrows():
            # print("saving " + str(offerHTML.ref_no))
            offer_ref_no = offer['ref_no']
            if Offer.objects.filter(ref_no=offer_ref_no).exists():
                # print("the offer " + str(offerHTML.ref_no) + " already exists in the DB")
                pass
            else:
                self.save_offer_to_database(offer)

    def save_offer_to_database(self, offer):
        offer = Offer(
            ref_no=offer.ref_no,
            deadline=offer.deadline,
            location_city=str(offer.location_city).capitalize(),
            location_country=offer.location_country,
            general_disciplines=offer.general_disciplines,
            fields_of_study=offer.fields_of_study,
            required_knowledge_and_experiences=offer.required_knowledge_and_experiences,
            other_requirements=offer.other_requirements,
            completed_years_of_study=offer.completed_years_of_study,
            language_requirements=offer.language_requirements,
            work_weeks_min=offer.work_weeks_min,
            work_weeks_max=offer.work_weeks_max,
            date_from=offer.date_from,
            date_to=offer.date_to,
            alternative_from=offer.alternative_from,
            alternative_to=offer.alternative_to,
            company_closed_from=offer.company_closed_from,
            company_closed_to=offer.company_closed_to,
            work_offered_description=offer.work_offered_description,
            gross_pay=offer.gross_pay,
            working_hours=offer.working_hours,
            employer=offer.employer,
            workplace=offer.workplace,
            website=offer.website,
            lodging_by=offer.lodging_by,
            living_cost=offer.living_cost,
            est_cost_of_lodging=offer.est_cost_of_lodging,
            additional_info=offer.additional_info,
            offer_type=offer.offer_type
        )
        offer.save()

    def delete_inactive_offers_from_database(self, offers_from_url):
        offers_from_database = Offer.objects.all()
        for offer_db in offers_from_database:
            # print(offerDB.ref_no)
            inactive = True
            for index, offer_url in offers_from_url.iterrows():
                if offer_db.ref_no == offer_url.ref_no:
                    inactive = False
            if inactive:
                print("Offer with ref_no '{}' is inactive and can be deleted from the database".format(offer_db.ref_no))
                Offer.objects.filter(ref_no=offer_db.ref_no).delete()
