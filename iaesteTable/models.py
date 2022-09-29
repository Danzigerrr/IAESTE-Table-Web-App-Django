from datetime import datetime

from django.db import models


class Offer(models.Model):
    RefNo = models.CharField(max_length=100, default="")
    Deadline = models.CharField(max_length=100, default="")
    From = models.CharField(max_length=100, default="")
    To = models.CharField(max_length=100, default="")
    City = models.CharField(max_length=100, default="")
    Country = models.CharField(max_length=100, default="")
    GeneralDisciplines = models.CharField(max_length=500, default="")
    FieldsOfStudy = models.CharField(max_length=500, default="")
    RequiredKnowledgeAndExperiences = models.CharField(max_length=500, default="")
    OtherRequirements = models.CharField(max_length=500, default="")
    CompletedYearsOfStudy = models.CharField(max_length=100, default="")
    LanguageRequirements = models.CharField(max_length=500, default="")
    WorkWeeksMin = models.CharField(max_length=100, default="")
    WorkWeeksMax = models.CharField(max_length=100, default="")
    AlternativeFrom = models.CharField(max_length=100, default="")
    AlternativeTo = models.CharField(max_length=100, default="")
    CompanyClosedFrom = models.CharField(max_length=100, default="")
    CompanyClosedTo = models.CharField(max_length=100, default="")
    WorkOfferedDescription = models.CharField(max_length=2000, default="")
    GrossPay = models.CharField(max_length=100, default="")
    WorkingHours = models.CharField(max_length=100, default="")
    Employer = models.CharField(max_length=200, default="")
    Workplace = models.CharField(max_length=100, default="")
    Website = models.CharField(max_length=300, default="")
    LodgingBy = models.CharField(max_length=100, default="")
    LivingCost = models.CharField(max_length=100, default="")
    EstCostOfLodging = models.CharField(max_length=100, default="")
    AdditionalInfo = models.CharField(max_length=500, default="")
    OfferType = models.CharField(max_length=50, default="")

    def __str__(self):
        return self.RefNo
