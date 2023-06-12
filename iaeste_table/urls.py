from django.urls import path
from . import views
from django.shortcuts import redirect


# URL conf
urlpatterns = [
    path('', lambda req: redirect('offers/')),
    path('offers/', views.main_list, name="offers list"),
    path('offers/<str:ref_no>/', views.detail, name='offer details'),
    path('map/', views.get_map, name='offers map'),
    path('about-project/', views.about_project, name='about project'),
    path('about-author/', views.about_author, name='about author'),
]

