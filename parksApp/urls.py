from django.urls import path

from . import views

urlpatterns = [
    path('', views.ParksHomeView.as_view(), name='index'),
    path('marked/', views.MarkedParksView.as_view(), name="marked"),
    path('visited/', views.VisitedParksView.as_view(),name="visited"),
    path("<int:pk>/", views.ParkDetailView.as_view(),name="park"),
    path("<int:park_id>/toggleMark/", views.toggleMark, name="toggleMark"),

]
