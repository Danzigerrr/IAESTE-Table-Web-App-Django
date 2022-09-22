from django.shortcuts import render
from django.http import HttpResponse


def clearHTMLCode(htmlCode):
    result = htmlCode
    result = result.replace("['']", "")
    result = result.replace("']", "")
    result = result.replace("['", "")
    result = result.replace("', '", " ")
    return result


def addSortingButtons(newHTML):
    newHTML = newHTML.replace("<table ", '<table id="myTable" ')
    newHTML = newHTML.replace("<th>RefNo</th>", '<th onclick="sortTable(0)">RefNo</th>')
    newHTML = newHTML.replace("<th>City</th>", '<th onclick="sortTable(0)">City</th>')
    newHTML = newHTML.replace("<th>Deadline</th>", '<th onclick="sortTable(0)">Deadline</th>')
    print(newHTML)
    return newHTML


def deleteIDColumn(newHTML, nrows):
    newHTML = newHTML.replace("<th></th>", '')
    for i in range(nrows):
        id = str(i)
        newHTML = newHTML.replace("<th>"+id+"</th>", '')
    return newHTML


def addLinksToRefNo(newHTML, RNList):
    for i in range(len(RNList)):
        id = str(RNList[i])
        newHTML = newHTML.replace("<td>"+id+"</td>", '')
    return newHTML


def say_hello(request):
    import pandas as pd
    nrows = 3
    df = pd.read_csv("AllOffers_21_09_2022.csv", nrows=nrows)
    df = df[["RefNo", "City", "Deadline"]]
    newHTML = clearHTMLCode(df.to_html())
    newHTML = deleteIDColumn(newHTML, nrows)
    newHTML = addSortingButtons(newHTML)
    #newHTML = addLinksToRefNo(newHTML, df["RefNo"])

    with open('test.txt', 'w') as f:
        f.write(newHTML)

    return render(request, "playground_view_1.html", {"table": newHTML})






def detail(request, question_id):
    return HttpResponse("This is the detail view of the question: %s" % question_id)





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
