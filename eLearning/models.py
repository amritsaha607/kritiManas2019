from django.db import models
from django.utils import timezone
from datetime import datetime

# Create your models here.

###################################
############# USERS ###############
###################################

class Student(models.Model):
	name = models.CharField(max_length=255)
	username = models.CharField(max_length=255, unique=True)
	email = models.EmailField(max_length=255, unique=True)
	password = models.CharField(max_length=255)

	def __str__(self):
		return self.username


class Club(models.Model):
	name = models.CharField(max_length=255)
	username = models.CharField(max_length=255, unique=True)
	password = models.CharField(max_length=255)

	def __str__(self):
		return self.name + ' Club'


class Department(models.Model):
	name = models.CharField(max_length=500)
	short_name = models.CharField(max_length=20)
	username = models.CharField(max_length=255, unique=True)
	password = models.CharField(max_length=255)

	def __str__(self):
		return self.short_name



## Document or video tags uploaded by students or clubs or departments
class Tag(models.Model):
	name = models.CharField(max_length=400)

	def __str__(self):
		return self.name



############# Course Section


## Academic Course or Course By Clubs
class Course(models.Model):
	code = models.CharField(max_length=500, unique=True)
	name = models.CharField(max_length=255, unique=True, null=True, blank=True)

	def __str__(self):
		return str(self.code)

## Videos for Course tutorial By Club/Dept
class Video(models.Model):
	title = models.CharField(max_length=10000)
	link = models.CharField(max_length=50000, null=True, blank=True)
	video = models.FileField(null=True, blank=True)
	uploaded_at = models.DateTimeField(default=datetime.now())

	tags = models.ManyToManyField(Tag, related_name='choice_videos', null=True, blank=True)
	course = models.ForeignKey('CourseTutorial', related_name='choice_videos', on_delete=models.CASCADE, null=True, blank=True)

	def __str__(self):
		return self.title

## Materials for course by Club/Dept
class Material(models.Model):
	name = models.CharField(max_length=25555)
	met = models.FileField()
	course = models.ForeignKey('CourseTutorial', related_name='choice_materials', on_delete=models.CASCADE, null=True, blank=True)
	tags = models.ManyToManyField(Tag, related_name='choice_materials', null=True, blank=True)
	uploaded_at = models.DateTimeField(default=datetime.now())

	def __str__(self):
		return self.name


## Courses by Club/Department


## One Course Tutorial can be given in multiple series by depts and clubs, so different table is made apart from Course

class CourseTutorial(models.Model):
	series_title = models.CharField(max_length=10000, default='')
	course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='choice_tutorials')
	videos = models.ManyToManyField(Video, related_name='choice_courses', null=True, blank=True)
	materials = models.ManyToManyField(Material, related_name='choice_courses', null=True, blank=True)
	last_update = models.DateTimeField(default=datetime.now())
	tot_rating = models.DecimalField(default=0.00, decimal_places=2, max_digits=20)
	rating_count = models.IntegerField(default=0)
	uploaded_by_club = models.ForeignKey(Club, related_name='choice_courses', on_delete=models.CASCADE, null=True, blank=True)
	uploaded_by_dept = models.ForeignKey(Department, related_name='choice_courses', on_delete=models.CASCADE, null=True, blank=True)

	def __str__(self):
		return self.series_title


## Rating for courses
class CourseRating(models.Model):
	value = models.IntegerField(default=0)
	student = models.ForeignKey(Student, related_name='my_ratings', on_delete=models.CASCADE)
	course = models.ForeignKey('CourseTutorial', related_name='my_ratings', on_delete=models.CASCADE)




###########################
#### MATERIALS SECTION ####
###########################

## Students Materials Sharing

## Document type uploaded by students (like scanned notes, Materials, books, Papers, assignment etc)
class DocType(models.Model):
	docType = models.CharField(max_length=255)

	def __str__(self):
		return self.docType

## Semester for which student is uploading material
class Semester(models.Model):
	sem = models.IntegerField(unique=True)

	def __str__(self):
		return 'Semester' + str(self.sem)

## Documents uploaded
class Document(models.Model):
	file = models.FileField()
	filename = models.CharField(max_length=1000)

	tags = models.ManyToManyField(Tag, related_name='choice_docs', null=True, blank=True)
	doc_type = models.ForeignKey(DocType, related_name='choice_docs', on_delete=models.SET_NULL, null=True, blank=True)
	sem = models.ManyToManyField(Semester, related_name='choice_docs', null=True, blank=True)
	course = models.ManyToManyField(Course, related_name='choice_docs', null=True, blank=True)
	dept = models.ManyToManyField(Department, related_name='choice_docs', null=True, blank=True)
	uploaded_by = models.ForeignKey(Student, on_delete=models.SET_NULL, related_name='choice_docs', null=True, blank=True)
	uploaded_at = models.DateTimeField(default=datetime.now())

	approved = models.BooleanField(default=False)

	def __str__(self):
		return self.filename
