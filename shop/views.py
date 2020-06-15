from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from .models import Course, Student, Guru

# Create your views here.
def index(request):
    context = {
        "courses": Course.objects.all()
    }
    return render(request,"courses/index.html", context)

def course(request, course_id):
    try:
        course = Course.objects.get(pk=course_id)
    except Course.DoesNotExist:
        raise Http404("Course does not exist")
        

    context = {
        "course": course,
        "students": course.students.all(),
        "non_students" : Student.objects.exclude(scourses=course).all()
    }
    return render(request,"courses/course.html", context)

def enroll(request, course_id):
    try:
        student_id = int(request.POST["student"])
        student = Student.objects.get(pk=student_id)
        course = Course.objects.get(pk=course_id)

    except KeyError:
        return render(request,"courses/error.html", {"message" : "No Selection done"})
    except Course.DoesNotExist:
        return render(request,"courses/error.html", {"message" : "No Course present"})
    except Student.DoesNotExist:
        return render(request,"courses/error.html", {"message" : "No student present"})

    student.scourses.add(course)
    return HttpResponseRedirect(reverse("course",args=(course_id,)))


