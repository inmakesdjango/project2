from . import views
from django.urls import path
app_name='searchapp'
urlpatterns = [

    path('search', views.SearchResult, name='SearchResult'),
]