## Demo (Student walkthrough)

![Student Walkthrough](https://github.com/amritsaha607/kritiManas2019/raw/master/demo/student-walkthrough.gif)


### This portal is made for three different types of users.
1. Student
2. Club
3. Department

### Requirements
  python version = 3.5.2 <br/>
  packages: <br/>
    django==2.0.7
  
## Walkthrough
1. A new student or new Club can register in the portal through the registration link.
2. A department/student/club can login through the login portal.

### COURSE SECTION
Any Club or Department can create it's own new tutorial series for any academic course or some other course. He can view his courses and edit his course any time. He can upload new video or material at anytime through the portal.

Student can view any course anytime.

### Materials 

Any student can upload amy material at anytime. Others can view and download the uploaded documents.


## Working with the portal
To run the application, run the following command <br/> 
<code>python3 manage.py runserver </code>
<br/>
To create your own admin account, run the command <br/>
<code>python manage.py createsuperuser </code>
<br/>
We've made some dummy database inside the application. Go to  <i> localhost:8000/admin/ </i>
Login through your newly created admin account credentials and you can access the whole database.

## Dummy users for testing
Student : username - "s1", password - "s1" <br/>
Club : username - "4i Lab", password - "4i Lab" <br/>
Department : username - "cse", password - "cse" <br/>
