This portal is made for three different types of users.
1. Student
2. Club
3. Department

Requirements to install :
  python version = 3.5.2
  packages:
    django==2.0.7
    
A new student or new Club can register in the portal through the registration link.
A department/student/club can login through the login portal

########### COURSE SECTION
Any Club or Department can create it's own new tutorial series for any academic course or some other course. He can view his courses and edit his course any time. He can upload new video or material at anytime through the portal.

Student can view any course anytime.

##### Materials 

Any student can upload amy material at anytime. Others can view and download the uploaded documents.


## Working with the portal
To run the application, run the command : "python manage.py runserver"
To create your own admin account, run the command "python manage.py createsuperuser"
We've made some dummy database inside the application. Go to "localhost:8000/admin/"
Login through your newly created admin account and you can access the whole database, including username and passwords of all Types of Users.

## We recommend using the following user as they contain most of the database
Student : username - "s1", password - "s1"
Club : username - "4i Lab", password - "4i Lab"
Department : username - "cse", password - "cse"
