from django.urls import path

from . import views

app_name="parksApp"
urlpatterns = [
    path('', views.ParksHomeView.as_view(), name='index'),
    path('marked/', views.MarkedParksView.as_view(), name="marked"),
    path('visited/', views.VisitedParksView.as_view(),name="visited"),
    path("<int:pk>/", views.ParkDetailView.as_view(),name="park"),
    path("<int:park_id>/toggleMark/", views.toggleMark, name="toggleMark"),
    path("<int:park_id>/toggleVisit/", views.toggleVisit, name="toggleVisit"),
    path("<int:park_id>/addEntry/", views.addEntry, name="addEntry"),
    path("<int:entry_id>/deleteEntry/", views.deleteEntry, name="deleteEntry"),

]
