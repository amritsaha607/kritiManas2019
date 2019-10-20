from django.urls import path
from . import views

app_name = 'eLearning'

urlpatterns = [
	path('login/', views.login, name='login'),
	path('register/', views.register, name='register'),
	path('', views.home, name='home'),
	path('logout/', views.logout, name='logout'),


	## Clubs
	path('club/activity/', views.clubActivity, name='clubActivity'),
	path('club/editTut<int:tut_id>/', views.editTut, name='editTut'),
	path('club/viewCourse<int:tut_id>/', views.viewCourse, name='viewCourse'),

	## Departments
	path('dept/activity/', views.deptActivity, name='deptActivity'),
	path('dept/editTut<int:tut_id>/', views.editTutdept, name='editTutdept'),


	## Students
	path('student/courses/', views.coursesStudent, name='coursesStudent'),
	path('student/courses/tutorial<int:tut_id>/', views.showTut, name='showTut'),

	## Uploading Books and Materials by Students
	path('student/library/', views.eLibrary, name='library'),


	### AJAX
	path('ajax_rateCourse/', views.ajax_rateCourse, name='ajax_rateCourse'),
]