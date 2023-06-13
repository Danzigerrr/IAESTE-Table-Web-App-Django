from django.db import models


class Offer(models.Model):
    ref_no = models.CharField(max_length=100, default="")
    deadline = models.CharField(max_length=100, default="")
    date_from = models.CharField(max_length=100, default="")
    date_to = models.CharField(max_length=100, default="")
    location_city = models.CharField(max_length=100, default="")
    location_country = models.CharField(max_length=100, default="")
    location_latitude = models.FloatField(null=True)
    location_longitude = models.FloatField(null=True)
    general_disciplines = models.CharField(max_length=500, default="")
    fields_of_study = models.CharField(max_length=500, default="")
    required_knowledge_and_experiences = models.CharField(max_length=500, default="")
    other_requirements = models.CharField(max_length=500, default="")
    completed_years_of_study = models.CharField(max_length=100, default="")
    language_requirements = models.CharField(max_length=500, default="")
    work_weeks_min = models.CharField(max_length=100, default="")
    work_weeks_max = models.CharField(max_length=100, default="")
    alternative_from = models.CharField(max_length=100, default="")
    alternative_to = models.CharField(max_length=100, default="")
    company_closed_from = models.CharField(max_length=100, default="")
    company_closed_to = models.CharField(max_length=100, default="")
    work_offered_description = models.CharField(max_length=2000, default="")
    gross_pay = models.CharField(max_length=100, default="")
    working_hours = models.CharField(max_length=100, default="")
    employer = models.CharField(max_length=200, default="")
    workplace = models.CharField(max_length=100, default="")
    website = models.CharField(max_length=300, default="")
    lodging_by = models.CharField(max_length=100, default="")
    living_cost = models.CharField(max_length=100, default="")
    est_cost_of_lodging = models.CharField(max_length=100, default="")
    additional_info = models.CharField(max_length=500, default="")
    offer_type = models.CharField(max_length=50, default="")
    iaeste_pdf_link = models.CharField(max_length=200, default="")

    def __str__(self):
        return self.ref_no

