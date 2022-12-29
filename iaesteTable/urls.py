from django.urls import path
from . import views


# URL conf
urlpatterns = [
    path('offers/', views.mainList, name="list"),
    path('offers/<str:RefNo>/', views.detail, name='detail'),
    path('offers/<str:RefNo>/city/', views.city, name='city'),
    path('map/', views.getMap, name='map'),
    path('aboutProject/', views.aboutProject, name='aboutProject'),
    path('aboutAuthor/', views.aboutAuthor, name='aboutAuthor'),
]