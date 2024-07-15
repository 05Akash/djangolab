from django.db import models

# Create your models here.


class Student(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Course(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    students = models.ManyToManyField(Student, related_name="courses", blank=True)

    def __str__(self):
        return self.name


class Project(models.Model):
    student = models.ForeignKey(
        Student, on_delete=models.CASCADE, related_name="projects"
    )
    topic = models.CharField(max_length=200)
    languages_used = models.CharField(max_length=200)
    duration = models.IntegerField()

    def __str__(self):
        return self.topic


# Shell commands used:

# from part2.models import Student, Course

# course1 = Course.objects.create(name="Math 101", description="Introduction to Algebra")
# course2 = Course.objects.create(name="History 201", description="World History")

# student1 = Student.objects.create(first_name="Arjun", last_name="shetty", email="arjun@gmail.com")
# student2 = Student.objects.create(first_name="Rithika", last_name="K", email="rithika.doe@gmail.com")

# course1.students.add(student1, student2)
# course2.students.add(student2)
