This is a university project with three users:

Admin - who is resposible for adding student, teachers, admin, department as well as deleting them
Student - who can view results, views module registered

Teachers - who can upload results to the students

Procedure to open the project
i> create a virtualenv using python -m venv venv
ii> python manage.py makemigrations
iii> python manage.py migrate
iv> python manage.py createsuperuser

After createsuperuser this project is design using decorators as admin, so the admin site of a django you have to go the group and assign admin,student and teacher(image.png)
Then move to the users assign the same permissions and give the password
Lastly move to the adminusers and assign admin,student,teacher and their permissions(image.png)

Then go and fill the student in which the user will be the student as well as the teacher in which the user is the teacher
Finally fill all the required tables in the django admin

Then switch to the localhost http://127.0.0.1:8000/ through python manage.py runserver
And login as admin, student and teacher

Goodluck!!!!
