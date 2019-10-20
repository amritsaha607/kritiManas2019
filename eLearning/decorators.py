from django.shortcuts import redirect

def student_login_required(function):
	def wrapper(request, login_url='eLearning:login', *args, **kwargs):
		if not 'student_id' in request.session:
			request.session['url_to_go'] = request.get_full_path()
			return redirect(login_url)
		else:
			return function(request, *args, **kwargs)
	return wrapper

def club_login_required(function):
	def wrapper(request, login_url='eLearning:login', *args, **kwargs):
		if not 'club_id' in request.session:
			request.session['url_to_go'] = request.get_full_path()
			return redirect(login_url)
		else:
			return function(request, *args, **kwargs)
	return wrapper

def dept_login_required(function):
	def wrapper(request, login_url='eLearning:login', *args, **kwargs):
		if not 'dept_id' in request.session:
			request.session['url_to_go'] = request.get_full_path()
			return redirect(login_url)
		else:
			return function(request, *args, **kwargs)
	return wrapper