from django.shortcuts import render, redirect
from .models import *
from .forms import *
from .decorators import *
from django.http import HttpResponse




## Utils

def get_student(request):
	return Student.objects.get(id=request.session['student_id'])

def get_club(request):
	return Club.objects.get(id=request.session['club_id'])

def get_dept(request):
	return Department.objects.get(id=request.session['dept_id'])



#### Create your views here.


def home(request):
	extendTemplate = 'base.html'
	if ('student_id' in request.session):
		videos = Video.objects.order_by('-uploaded_at')[:6]
		videosToShow = [
			[videos[0], videos[1]],
			[videos[2], videos[3]],
			[videos[4], videos[5]],
		]
		extendTemplate = 'baseStudent.html'
		return render(
			request, 
			'eLearning/home.html', 
			{'extendTemplate': extendTemplate, 'videosToShow': videosToShow}
		)
	elif 'club_id' in request.session:
		extendTemplate = 'baseClub.html'
		return redirect('eLearning:clubActivity')

	elif 'dept_id' in request.session:
		extendTemplate = 'baseDepartment.html'
		return redirect('eLearning:deptActivity')

	return render(request, 'eLearning/home.html', {'extendTemplate': extendTemplate})

######## AUTHENTICATION #######

def register(request):
	if ('student_id' in request.session) or ('club_id' in request.session) or ('dept_id' in request.session):
		return redirect('eLearning:home')
	formStudent = RegisterFormStudent()
	formClub = RegisterFormClub()
	if request.method=='POST':
		if 'student' in request.POST:
			form = RegisterFormStudent(request.POST)
			new_student = form.save(commit=False)
			new_student.save()
			request.session['student_id'] = new_student.id
		elif 'club' in request.POST:
			form = RegisterFormClub(request.POST)
			new_club = form.save(commit=False)
			new_club.save()
			request.session['club_id'] = new_club.id
		return redirect('eLearning:home')

	return render(request, 'eLearning/auth/register.html', {'formStudent': formStudent, 'formClub': formClub})

def login(request):
	if ('student_id' in request.session) or ('club_id' in request.session) or ('dept_id' in request.session):
		return redirect('eLearning:home')
	formStudent = LoginFormStudent()
	formClub = LoginFormClub()
	formDepartment = LoginFormDepartment()

	if request.method=='POST':
		t_username = request.POST['username']
		t_password = request.POST['password']
		if 'student' in request.POST:
			if Student.objects.filter(username=t_username, password=t_password).exists():
				student = Student.objects.get(username=t_username)
				request.session['student_id'] = student.id
				return redirect('eLearning:home')
		elif 'club' in request.POST:
			if Club.objects.filter(username=t_username, password=t_password).exists():
				club = Club.objects.get(username=t_username)
				request.session['club_id'] = club.id
				return redirect('eLearning:home')
		elif 'dept' in request.POST:
			if Department.objects.filter(username=t_username, password=t_password).exists():
				dept = Department.objects.get(username=t_username)
				request.session['dept_id'] = dept.id
				return redirect('eLearning:home')

	return render(
		request, 
		'eLearning/auth/login.html', 
		{
			'formStudent': formStudent, 
			'formClub': formClub, 
			'formDepartment': formDepartment
		}
	)


def logout(request):
	if 'student_id' in request.session:
		del request.session['student_id']
	elif 'club_id' in request.session:
		del request.session['club_id']
	elif 'dept_id' in request.session:
		del request.session['dept_id']
	return redirect('eLearning:login')



############################################################################
###################### COURSE SECTION ######################################

## Activities of Club
@club_login_required
def clubActivity(request):
	club = get_club(request)
	courses = club.choice_courses.order_by('-id')
	form = CreateTut()

	if request.method=='POST':
		if 'course' in request.POST and request.POST['course']:
			form = CreateTut(request.POST)
			new_tut = form.save(commit=False)
			new_tut.uploaded_by_club = club
			new_tut.save()
		elif 'course_code' in request.POST:
			## Add New Course
			if not Course.objects.filter(code=request.POST['course_code']):
				new_course = Course(code=request.POST['course_code'])
				new_course.save()
				CourseTutorial.objects.create(
					series_title = request.POST['series_title'],
					course = new_course,
					uploaded_by_club = club
				)
			else:
				new_course = Course.objects.get(code=request.POST['course_code'])
				CourseTutorial.objects.create(
					series_title = request.POST['series_title'],
					course = new_course,
					uploaded_by_club = club
				)
		return redirect('eLearning:clubActivity')

	return render(request, 'eLearning/club/activity.html', {'club': club, 'courses': courses, 'form': form})

## View CLub Course
@club_login_required
def viewCourse(request, tut_id):
	club = get_club(request)
	tut = CourseTutorial.objects.get(id=tut_id)

	if request.method=='GET':
		if 'paramvideo' in request.GET:
			video_id = int(request.GET['paramvideo'])
			vid = Video.objects.get(id=video_id)
			isvideo = True
			if not vid.link=="":
				isvideo = False
			return render(request, 'eLearning/Student/showTut.html', {'tut': tut, 'vid': vid, 'isvideo': isvideo})
		if 'paramMet' in request.GET:
			met_id = int(request.GET['paramMet'])
			met = Material.objects.get(id=met_id)
			return render(request, 'eLearning/Student/showTut.html', {'tut': tut, 'met_id': met_id, 'met': met})
		else:
			print('\n\n\n\n\n')
			print(tut.videos.all().count())
			print('\n\n\n\n\n')
			whatToClick = None
			if not tut.videos.all().count()==0:
				whatToClick = "Video"
			elif not tut.materials.all().count()==0:
				whatToClick = "Met"
			return render(request, 'eLearning/Student/showTut.html', {'tut': tut, 'whatToClick': whatToClick})

	return render(request, 'eLearning/club/viewCourse.html', {'tut': tut, 'club': club})




	return render(request,'eLearning/club/showCourse.html', {'club': club, 'course': course})

## Edit Tutorial by Club
@club_login_required
def editTut(request, tut_id):
	club = get_club(request)
	if not CourseTutorial.objects.filter(id=tut_id).exists():
		return render(request, 'error.html', {})
	tut = CourseTutorial.objects.get(id=tut_id)

	if request.method=='POST':
		print(request.POST)
		new_video = Video(course=tut)
		new_met = Material(course=tut)


		if 'title' in request.POST:
			new_video.title = request.POST['title']
			new_video.save()
		if 'video_link' in request.POST:
			new_video.link=request.POST['video_link']
			new_video.save()
		if 'video' in request.FILES:
			new_video.video = request.FILES['video']
			new_video.save()
		
		

		if ('met_title' in request.POST) and request.POST['met_title'] and 'met' in request.FILES and request.FILES['met']:
			new_met.name = request.POST['met_title']
			new_met.met = request.FILES['met']
			new_met.save()
		

		if ('video_tags' in request.POST) and request.POST['video_tags']:
			new_video.save()
			tags = request.POST['video_tags'].split(' ')
			for tag in tags:
				new_tag = None
				if not Tag.objects.filter(name=tag).exists():
					new_tag = Tag(name=tag)
					new_tag.save()
				else:
					new_tag = Tag.objects.get(name=tag)
				new_video.tags.add(new_tag)
			new_video.save()

		if ('material_tags' in request.POST) and request.POST['material_tags']:
			new_met.save()
			tags = request.POST['material_tags'].split(' ')
			for tag in tags:
				new_tag = None
				if not Tag.objects.filter(name=tag).exists():
					new_tag = Tag(name=tag)
					new_tag.save()
				else:
					new_tag = Tag.objects.get(name=tag)
				new_met.tags.add(new_tag)
			new_tag.save()


		## Last update of the tutorial is changed
		try:
			tut.videos.add(new_video)
			tut.materials.add(new_met)
			tut.last_update = datetime.now()
		except ValueError:
			try:
				tut.materials.add(new_met)
				tut.last_update = datetime.now()
			except ValueError:
				pass
		tut.save()

		return redirect('eLearning:clubActivity')

	return render(request, 'eLearning/club/editTut.html', {'tut': tut})




#################### DEPARTMENT
@dept_login_required
def deptActivity(request):
	dept = get_dept(request)
	courses = dept.choice_courses.order_by('-id')
	form = CreateTut()

	if request.method=='POST':
		if 'course' in request.POST and request.POST['course']:
			form = CreateTut(request.POST)
			new_tut = form.save(commit=False)
			new_tut.uploaded_by_dept = dept
			new_tut.save()
		elif 'course_code' in request.POST:
			## Add New Course
			if not Course.objects.filter(code=request.POST['course_code']):
				new_course = Course(code=request.POST['course_code'])
				new_course.save()
				CourseTutorial.objects.create(
					series_title = request.POST['series_title'],
					course = new_course,
					uploaded_by_club = dept
				)
			else:
				new_course = Course.objects.get(code=request.POST['course_code'])
				CourseTutorial.objects.create(
					series_title = request.POST['series_title'],
					course = new_course,
					uploaded_by_club = dept
				)
		return redirect('eLearning:deptActivity')

	return render(request, 'eLearning/dept/activity.html', {'dept': dept, 'courses': courses, 'form': form})

## Edit Tutorial by Club
@dept_login_required
def editTutdept(request, tut_id):
	dept = get_dept(request)
	if not CourseTutorial.objects.filter(id=tut_id).exists():
		return render(request, 'error.html', {})
	tut = CourseTutorial.objects.get(id=tut_id)

	if request.method=='POST':
		new_video = Video(course=tut)
		new_met = Material(course=tut)

		if ('title' in request.POST) and request.POST['title']:
			new_video.title = request.POST['title']
			new_video.save()
			if ('video_link' in request.POST) and request.POST['video_link']:
				new_video.link=request.POST['video_link']
				new_video.save()
			if 'video' in request.FILES:
				new_video.video = request.FILES['video']
				new_video.save()
		
		

		if ('met_title' in request.POST) and request.POST['met_title'] and ('met' in request.FILES) and request.FILES['met']:
			new_met.name = request.POST['met_title']
			new_met.met = request.FILES['met']
			new_met.save()
		

		if 'video_tags' in request.POST:
			new_video.save()
			tags = request.POST['video_tags'].split(' ')
			for tag in tags:
				new_tag = None
				if not Tag.objects.filter(name=tag).exists():
					new_tag = Tag(name=tag)
					new_tag.save()
				else:
					new_tag = Tag.objects.get(name=tag)
				new_video.tags.add(new_tag)
			new_video.save()

		if ('material_tags' in request.POST) and request.POST['material_tags']:
			new_met.save()
			tags = request.POST['material_tags'].split(' ')
			for tag in tags:
				new_tag = None
				if not Tag.objects.filter(name=tag).exists():
					new_tag = Tag(name=tag)
					new_tag.save()
				else:
					new_tag = Tag.objects.get(name=tag)
				new_met.tags.add(new_tag)
			new_met.save()


		## Last update of the tutorial is changed
		try:
			tut.videos.add(new_video)
			tut.materials.add(new_met)
			tut.last_update = datetime.now()
		except ValueError:
			try:
				tut.materials.add(new_met)
				tut.last_update = datetime.now()
			except ValueError:
				pass
		tut.save()




		# if new_video is not None:
		# 	tut.videos.add(new_video)
		# if new_met is not None:
		# 	tut.materials.add(new_met)
		# if (new_video is not None) or (new_met is not None):
		# 	tut.last_update = datetime.now()
		# tut.save()

		return redirect('eLearning:deptActivity')

	return render(request, 'eLearning/club/editTut.html', {'tut': tut})





########################### Student
@student_login_required
def coursesStudent(request):
	student = get_student(request)
	courses = CourseTutorial.objects.order_by('-last_update')
	all_tags = Tag.objects.all()
	if request.method=='POST':
		if Tag.objects.filter(name=request.POST['tag']).exists():
			tag = Tag.objects.get(name=request.POST['tag'])
			videos = tag.choice_videos.all()
			courses = set([vid.course for vid in videos])
		else:
			courses = None
	return render(request, 'eLearning/Student/course.html', {'courses': courses, 'student': student, 'all_tags': all_tags})

@student_login_required
def showTut(request, tut_id):
	tut = CourseTutorial.objects.get(id=tut_id)

	if request.method=='GET':
		if 'paramvideo' in request.GET:
			video_id = int(request.GET['paramvideo'])
			vid = Video.objects.get(id=video_id)
			isvideo = True
			if not vid.link=="":
				isvideo = False
			return render(request, 'eLearning/Student/showTut.html', {'tut': tut, 'vid': vid, 'isvideo': isvideo})
		if 'paramMet' in request.GET:
			met_id = int(request.GET['paramMet'])
			met = Material.objects.get(id=met_id)
			return render(request, 'eLearning/Student/showTut.html', {'tut': tut, 'met_id': met_id, 'met': met})
		else:
			print('\n\n\n\n\n')
			print(tut.videos.all().count())
			print('\n\n\n\n\n')
			whatToClick = None
			if not tut.videos.all().count()==0:
				whatToClick = "Video"
			elif not tut.materials.all().count()==0:
				whatToClick = "Met"
			return render(request, 'eLearning/Student/showTut.html', {'tut': tut, 'whatToClick': whatToClick})

	return render(request, 'eLearning/Student/showTut.html', {'tut': tut})


@student_login_required
def eLibrary(request):
	student = get_student(request)
	form = NewDocLibraryForm()
	all_sems = Semester.objects.all()
	all_depts = Department.objects.all()
	all_courses = Course.objects.all()
	all_types = DocType.objects.all()
	all_docs = Document.objects.all().order_by('-uploaded_at')
	all_tags = Tag.objects.all()

	if request.method=='POST':
		if 'upload' in request.POST:
			new_doc = Document(
				file = request.FILES['newdoc'],
				filename = request.POST['filename'],
				doc_type = DocType.objects.get(id=int(request.POST['typeNo'])),
				uploaded_by = student,
				uploaded_at = datetime.now(),
			)
			new_doc.save()
			for t_sem in request.POST.getlist('semNo'):
				new_doc.sem.add(Semester.objects.get(id=int(t_sem)))
			for t_dept in request.POST.getlist('deptNo'):
				new_doc.dept.add(Department.objects.get(id=int(t_dept)))
			for t_course in request.POST.getlist('courseNo'):
				new_doc.course.add(Course.objects.get(id=int(t_course)))
			for t_tag in (request.POST['tags']).split(' '):
				if t_tag:
					if Tag.objects.filter(name=t_tag).exists():
						new_doc.tags.add(Tag.objects.get(name=t_tag))
					else:
						new_tag = Tag(name=t_tag)
						new_tag.save()
						new_doc.tags.add(new_tag)
			new_doc.save()
			return redirect('eLearning:library')

		elif 'filter' in request.POST:
			if not request.POST['dept'] == "":
				all_docs = all_docs.filter(dept=Department.objects.get(id=int(request.POST['dept'])))
			if not request.POST['sem'] == "":
				all_docs = all_docs.filter(sem=Semester.objects.get(id=int(request.POST['sem'])))
			if not request.POST['doctype'] == "":
				all_docs = all_docs.filter(doc_type=DocType.objects.get(id=int(request.POST['doctype'])))
			if not request.POST['course'] == "":
				all_docs = all_docs.filter(course=Course.objects.get(id=int(request.POST['course'])))
			if not request.POST['tag']=="":
				if Tag.objects.filter(name=request.POST['tag']).exists():
					curr_tag = Tag.objects.get(name=request.POST['tag'])
					all_docs = all_docs & curr_tag.choice_docs.all()
	return render(
		request, 
		'eLearning/Student/library.html', 
		{
			'all_docs': all_docs, 
			'all_sems': all_sems,
			'all_depts': all_depts,
			'all_types': all_types,
			'all_tags': all_tags,
			'all_courses': all_courses,
			'form': form
		}
	)




###################### AJAX
def ajax_rateCourse(request):
	for key in request.GET:
		if key != "_":
			dataGet = key.split('_')
			t_rating = int(dataGet[0])
			course_id = int(dataGet[1])
			corr_course = CourseTutorial.objects.get(id=course_id)

			student = get_student(request)
			if not CourseRating.objects.filter(student=student, course=corr_course).exists():
				CourseRating.objects.create(
					value = t_rating,
					student = get_student(request),
					course = corr_course,
				)

				corr_course.rating_count += 1
				corr_course.tot_rating += t_rating
				corr_course.save()
			else:
				obj = CourseRating.objects.get(student=student, course=corr_course)

				corr_course.tot_rating += (t_rating - obj.value)
				corr_course.save()

				obj.value = t_rating
				obj.save()

			
			return HttpResponse("done")