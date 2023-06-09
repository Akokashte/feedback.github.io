from urllib import request
from django.db import models
import datetime

# Create your models here.
class Feedback(models.Model):
     id = models.AutoField(primary_key=True)
     email = models.CharField(max_length=200,default=[])
     myclass = models.CharField(max_length=200,default=[])
     sem = models.CharField(max_length=200,default=[])
     branch = models.CharField(max_length=200,default=[])
     q1 = models.CharField(max_length=150,default=[])
     q2 = models.CharField(max_length=150,default=[])
     q3 = models.CharField(max_length=150,default=[])
     q4 = models.CharField(max_length=150,default=[])
     q5 = models.CharField(max_length=150,default=[])
     q6 = models.CharField(max_length=150,default=[])
     q7 = models.CharField(max_length=150,default=[])
     suggestion = models.CharField(max_length=150,default=[])
    #  rating = models.FloatField()
     date = models.DateField()
     # created by me to use name as entry in django admin panel
     def __str__(self):
         return str(self.id)

class AcademicForm(models.Model):
     id = models.AutoField(primary_key=True)
     email = models.CharField(max_length=100)
     branch = models.CharField(max_length=150,default="")
     myclass = models.CharField(max_length=150,default="")
     sem = models.CharField(max_length=50)
     feedbacktype = models.CharField(max_length=100,default="")
     date = models.DateField()
     # created by me to use name as entry in django admin panel
     def __str__(self):
         return str(self.id)
     
class Contact(models.Model):
     sno = models.AutoField(primary_key=True)
     name = models.CharField(max_length=255)
     phone = models.CharField(max_length=15)
     email = models.CharField(max_length=100)
     content = models.TextField()
     timestamp = models.DateTimeField(auto_now_add=True,blank=True)

     # created by me to use name as entry in django admin panel
     def __str__(self):
         return 'Message from ' + self.name + ' - '+self.email

class TheoryFeedback(models.Model):
     id = models.AutoField(primary_key=True)

     academic_year = models.CharField(max_length=100,default="")
     semester = models.CharField(max_length=100,default="")
     branch = models.CharField(max_length=100,default="")
     year = models.CharField(max_length=100,default="")

     # Subject No 1
     s1_subject_name = models.CharField(max_length=100,default="")
     s1_teacher_name = models.CharField(max_length=100,default="")
     s1_q1 = models.IntegerField(default=0)
     s1_q2 = models.IntegerField(default=0)
     s1_q3 = models.IntegerField(default=0)
     s1_q4 = models.IntegerField(default=0)
     s1_q5 = models.IntegerField(default=0)
     s1_q6 = models.IntegerField(default=0)
     s1_q7 = models.IntegerField(default=0)
     s1_suggestion = models.CharField(max_length=150,default="")

     # Subject No 2
     s2_subject_name = models.CharField(max_length=100,default="")
     s2_teacher_name = models.CharField(max_length=100,default="")
     s2_q1 = models.IntegerField(default=0)
     s2_q2 = models.IntegerField(default=0)
     s2_q3 = models.IntegerField(default=0)
     s2_q4 = models.IntegerField(default=0)
     s2_q5 = models.IntegerField(default=0)
     s2_q6 = models.IntegerField(default=0)
     s2_q7 = models.IntegerField(default=0)
     s2_suggestion = models.CharField(max_length=150,default="")

     # Subject No 3
     s3_subject_name = models.CharField(max_length=100,default="")
     s3_teacher_name = models.CharField(max_length=100,default="")
     s3_q1 = models.IntegerField(default=0)
     s3_q2 = models.IntegerField(default=0)
     s3_q3 = models.IntegerField(default=0)
     s3_q4 = models.IntegerField(default=0)
     s3_q5 = models.IntegerField(default=0)
     s3_q6 = models.IntegerField(default=0)
     s3_q7 = models.IntegerField(default=0)
     s3_suggestion = models.CharField(max_length=150,default="")

     # Subject No 4
     s4_subject_name = models.CharField(max_length=100,default="")
     s4_teacher_name = models.CharField(max_length=100,default="")
     s4_q1 = models.IntegerField(default=0)
     s4_q2 = models.IntegerField(default=0)
     s4_q3 = models.IntegerField(default=0)
     s4_q4 = models.IntegerField(default=0)
     s4_q5 = models.IntegerField(default=0)
     s4_q6 = models.IntegerField(default=0)
     s4_q7 = models.IntegerField(default=0)
     s4_suggestion = models.CharField(max_length=150,default="")

     # Subject No 5
     s5_subject_name = models.CharField(max_length=100,default="")
     s5_teacher_name = models.CharField(max_length=100,default="")
     s5_q1 = models.IntegerField(default=0)
     s5_q2 = models.IntegerField(default=0)
     s5_q3 = models.IntegerField(default=0)
     s5_q4 = models.IntegerField(default=0)
     s5_q5 = models.IntegerField(default=0)
     s5_q6 = models.IntegerField(default=0)
     s5_q7 = models.IntegerField(default=0)
     s5_suggestion = models.CharField(max_length=150,default="")


     def __str__(self):
         return str(self.id)
     
# added by ak now
class Practical(models.Model):
     id = models.AutoField(primary_key=True)
     email = models.CharField(max_length=200,default=[])
     myclass = models.CharField(max_length=200,default=[])
     sem = models.CharField(max_length=200,default=[])
     branch = models.CharField(max_length=200,default=[])
     q1 = models.CharField(max_length=150,default=[])
     q2 = models.CharField(max_length=150,default=[])
     q3 = models.CharField(max_length=150,default=[])
     q4 = models.CharField(max_length=150,default=[])
     q5 = models.CharField(max_length=150,default=[])
     q6 = models.CharField(max_length=150,default=[])
     q7 = models.CharField(max_length=150,default=[])
     suggestion = models.CharField(max_length=150,default=[])
    #  rating = models.FloatField()
     date = models.DateField()
     # created by me to use name as entry in django admin panel
     def __str__(self):
         return str(self.id)
     
class PracticalFeedback(models.Model):
     id = models.AutoField(primary_key=True)

     academic_year = models.CharField(max_length=100,default="")
     semester = models.CharField(max_length=100,default="")
     branch = models.CharField(max_length=100,default="")
     year = models.CharField(max_length=100,default="")

     # Practical No 1
     p1_subject_name = models.CharField(max_length=100,default="")
     p1_teacher_name = models.CharField(max_length=100,default="")
     p1_q1 = models.IntegerField(default=0)
     p1_q2 = models.IntegerField(default=0)
     p1_q3 = models.IntegerField(default=0)
     p1_q4 = models.IntegerField(default=0)
     p1_q5 = models.IntegerField(default=0)
     p1_q6 = models.IntegerField(default=0)
     p1_q7 = models.IntegerField(default=0)
     p1_suggestion = models.CharField(max_length=150,default="")

     # Practical No 2
     p2_subject_name = models.CharField(max_length=100,default="")
     p2_teacher_name = models.CharField(max_length=100,default="")
     p2_q1 = models.IntegerField(default=0)
     p2_q2 = models.IntegerField(default=0)
     p2_q3 = models.IntegerField(default=0)
     p2_q4 = models.IntegerField(default=0)
     p2_q5 = models.IntegerField(default=0)
     p2_q6 = models.IntegerField(default=0)
     p2_q7 = models.IntegerField(default=0)
     p2_suggestion = models.CharField(max_length=150,default="")

     # Practical No 3
     p3_subject_name = models.CharField(max_length=100,default="")
     p3_teacher_name = models.CharField(max_length=100,default="")
     p3_q1 = models.IntegerField(default=0)
     p3_q2 = models.IntegerField(default=0)
     p3_q3 = models.IntegerField(default=0)
     p3_q4 = models.IntegerField(default=0)
     p3_q5 = models.IntegerField(default=0)
     p3_q6 = models.IntegerField(default=0)
     p3_q7 = models.IntegerField(default=0)
     p3_suggestion = models.CharField(max_length=150,default="")

     # Practical No 4
     p4_subject_name = models.CharField(max_length=100,default="")
     p4_teacher_name = models.CharField(max_length=100,default="")
     p4_q1 = models.IntegerField(default=0)
     p4_q2 = models.IntegerField(default=0)
     p4_q3 = models.IntegerField(default=0)
     p4_q4 = models.IntegerField(default=0)
     p4_q5 = models.IntegerField(default=0)
     p4_q6 = models.IntegerField(default=0)
     p4_q7 = models.IntegerField(default=0)
     p4_suggestion = models.CharField(max_length=150,default="")

     # Practical No 5
     p5_subject_name = models.CharField(max_length=100,default="")
     p5_teacher_name = models.CharField(max_length=100,default="")
     p5_q1 = models.IntegerField(default=0)
     p5_q2 = models.IntegerField(default=0)
     p5_q3 = models.IntegerField(default=0)
     p5_q4 = models.IntegerField(default=0)
     p5_q5 = models.IntegerField(default=0)
     p5_q6 = models.IntegerField(default=0)
     p5_q7 = models.IntegerField(default=0)
     p5_suggestion = models.CharField(max_length=150,default="")

     # Mini - Project
     project_name = models.CharField(max_length=100,default="")
     project_teacher_name = models.CharField(max_length=100,default="")
     project_q1 = models.IntegerField(default=0)
     project_q2 = models.IntegerField(default=0)
     project_q3 = models.IntegerField(default=0)
     project_q4 = models.IntegerField(default=0)
     project_q5 = models.IntegerField(default=0)
     project_q6 = models.IntegerField(default=0)
     project_q7 = models.IntegerField(default=0)
     project_suggestion = models.CharField(max_length=150,default="")

     def __str__(self):
         return str(self.id)

class ParentsFeedback(models.Model):
     id = models.AutoField(primary_key=True)
     name = models.CharField(max_length=200,default=[])
     email = models.CharField(max_length=200,default=[])
     comments = models.CharField(max_length=200,default=[])
     date = models.DateField(default=datetime.datetime.now())
     def __str__(self):
         return str(self.id)
     
class AlumniFeedback(models.Model):
     id = models.AutoField(primary_key=True)
     name = models.CharField(max_length=200,default=[])
     passout_year = models.IntegerField(default=0)
     department = models.CharField(max_length=50,default=[])
     email = models.CharField(max_length=50,default=[])
     comments = models.CharField(max_length=200,default=[])
     date = models.DateField(default=datetime.datetime.now())
     def __str__(self):
         return str(self.id)