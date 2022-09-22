import django_tables2 as tables
from .models import Person
from django_filters.views import FilterView
from django_tables2.views import SingleTableMixin

class PersonTable(tables.Table, FilterView):
    id = tables.Column()
    name = tables.Column(attrs={"tf": {"bgcolor": "red"}})

    class Meta:
        attrs = {"class": "mytable"}
        model = Person
        template_name = "../templates/people.html"
        fields = ("name", "id")
