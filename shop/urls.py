from django.urls import path
from . import views

urlpatterns = [
    path("",views.index, name="index"),
    path("<int:course_id>",views.course, name="course"),
    path("<int:course_id>/enroll",views.enroll, name="enroll")
]