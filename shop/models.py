from django.db import models

# Create your models here.

class Guru(models.Model):
    guruname = models.CharField(max_length=40)
    gurucode = models.CharField(max_length=5)
    
    def __str__(self):
        return self.guruname

class Course(models.Model):
    coursename = models.CharField(max_length=320)
    coursecode = models.CharField(max_length=5, null=True)
    guru = models.ForeignKey(Guru,on_delete=models.CASCADE,related_name='guru', null=True)
    courseduration = models.IntegerField()

    def __str__(self):
        return self.coursecode +" - "+ self.coursename+" by "+self.guru.guruname

class Student(models.Model):
    sfirstname = models.CharField(max_length=20)
    slastname = models.CharField(max_length=20)
    semail = models.CharField(max_length=40)
    sphone = models.IntegerField()
    scountry = models.CharField(max_length=40)
    scourses = models.ManyToManyField(Course, blank=True, related_name="students")
    
    def __str__(self):
        return self.sfirstname+" "+self.slastname




