from django.urls import path
from . import views
from playground.views import PersonListView


# URL conf
urlpatterns = [
    path('hello/', views.say_hello),
    path('hello/<str:question_id>', views.detail, name = 'detail'),
    path('hello/<int:question_id>/vote', views.vote, name = 'vote'),
    path('hello/<int:question_id>/results', views.results, name='results'),
    path("people/", PersonListView.as_view(), name="people")
]