from django.urls import path
from collection import views

urlpatterns = [
    path('', views.home, name='artefact_list'),
    path('detail/<int:id>/', views.artefact_detail, name='artefact_detail'),
    path('detail/<int:id>/favourite_artefact/', views.favourite_artefact, name='favourite_artefact'),
    path('favourites/', views.favourite_artefact_list, name='favourite_artefact_list'),
]