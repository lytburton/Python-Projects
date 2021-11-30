from django.db import models


# created a new class with attributes and an object manager

class djangoClasses(models.Model):
    title = models.CharField(max_length=100, default="")
    course_number = models.IntegerField(default=0)
    instructor_name = models.CharField(max_length=100, default="")
    duration = models.FloatField(default=0)

    object = models.Manager()

    # string for representing the djangoClasses object
    def __str__(self):
        return self.title
