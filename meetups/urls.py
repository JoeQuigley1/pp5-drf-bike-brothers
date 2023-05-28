from django.urls import path
from meetups import views

urlpatterns = [
    path('meetups/', views.MeetUpsList.as_view()),
    path('meetups/<int:pk>/', views.MeetUpsDetail.as_view())
]
