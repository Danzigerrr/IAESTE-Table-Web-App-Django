from django.shortcuts import render
from django.http import HttpResponse


def clearHTMLCode(htmlCode):
    result = htmlCode
    result = result.replace("['']", "")
    result = result.replace("']", "")
    result = result.replace("['", "")
    result = result.replace("', '", " ")
    return result


def addSortingButtons(newHTML, df):
    newHTML = newHTML.replace("<table ", '<table id="myTable" ')
    for col in df.columns:
        newHTML = newHTML.replace("<th>"+col+"</th>", '<th onclick="sortTable(0)">' + col + '</th>')
    print(newHTML)
    return newHTML


def deleteIDColumn(newHTML, nrows=2):
    newHTML = newHTML.replace("<th></th>", '')
    for i in range(nrows):
        id = str(i)
        newHTML = newHTML.replace("<th>" + id + "</th>", '')
    return newHTML


def addLinksToRefNo(newHTML, RNList):
    for i in range(len(RNList)):
        id = str(RNList[i])
        ipaddress = "http://127.0.0.1:8000/playground/hello/" + id
        href = '<a href="' + ipaddress + '" target="_blank">' + id + '</a>'
        currrentTD = "<td>" + id + "</td>"
        newHTML = newHTML.replace(currrentTD, '<td>' + href + '</td>')
    return newHTML


def say_hello(request):
    import pandas as pd
    nrows = 3
    df = pd.read_csv("AllOffers_21_09_2022.csv", nrows=nrows)
    df = df[["RefNo", "City", "Deadline"]]
    newHTML = clearHTMLCode(df.to_html())
    newHTML = deleteIDColumn(newHTML, nrows)
    newHTML = addSortingButtons(newHTML, df)
    newHTML = addLinksToRefNo(newHTML, df["RefNo"])

    with open('test.txt', 'w') as f:
        f.write(newHTML)

    return render(request, "playground_view_1.html", {"table": newHTML})


def detail(request, question_id):
    import pandas as pd
    OfferId = question_id
    df = pd.read_csv("AllOffers_21_09_2022.csv")
    rowWithOffer = df.loc[df['RefNo'] == OfferId]
    newHTML = clearHTMLCode(rowWithOffer.to_html())
    newHTML = deleteIDColumn(newHTML)
    return render(request, "detail_view_1.html", {"table": newHTML})


def results(request, question_id):
    return HttpResponse("This is the result of the question: %s" % question_id)


def vote(request, question_id):
    tostr = str(question_id)
    return render(request, "view2.html", {"name": tostr})


from django_tables2 import SingleTableView

from .models import Person
from .tables import PersonTable
from django_filters.views import FilterView
from django_tables2.views import SingleTableMixin


class PersonListView(SingleTableMixin, FilterView):
    table_class = PersonTable
    model = Person
    template_name = "../templates/people.html"
