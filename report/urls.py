from django.urls import path

from  report import views



urlpatterns = [
    path('<int:pk>/',views.student_detail,name='student_detail'),
]
