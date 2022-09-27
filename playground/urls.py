from django.urls import path
from . import views


# URL conf
urlpatterns = [
    path('hello/', views.say_hello),
    path('hello/<str:question_id>', views.detail, name = 'detail'),
    path('hello/<str:question_id>/city', views.city, name = 'city'),
    path('hello/<int:question_id>/results', views.results, name='results'),
]