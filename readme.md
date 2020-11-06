**Basic API Project to Python dev role at [Smarket](https://smarket.com.br/)**

You can find the project scope at [Teste_tecnico_smarket PDF File](https://github.com/matheusads/smarket_backend/blob/master/Teste_tecnico_smarket.pdf) in PT-Br

Tldr: API should create users and tasks related to the users.


**Project Stack**

I choose use minimum possible external libs, so in this project I only used Django with Django Rest Framework 
because they allow me a fast development and didn't need to deal with database configuration for example. 
So for this I didn't use pytest(my preference).

For development and tests I used PyCharm and [DRF Browsable API](https://restframework.herokuapp.com/) 
in Elementary OS (Ubuntu based)

**Project Setup**

Python 3.6 - was the default in my system
Virtualenv

Clone project
```
git clone git@github.com:matheusads/smarket_backend.git
```

Make a virtualenv with at least Python 3.6
```
python3 -m venv venv
```

Activate virtualenv
```
source venv/bin/activate
```

Install dependencies
```
pip install -r requirements.txt
```
Make migrations
```
python manage.py makemigrations
python manage.py migrate
```
Create a superuser.
```
python manage.py creatersuperuser
```
Then finally run server
```
python manage.py runserver
```

Unit tests
```
python manage.py test
```

**API usage**

As this is a small POC, to insert data we can use Browsable API, Django Admin or APIs 
requests as in Postman Collection (recommended). For lot of data I would make a [management script](https://docs.djangoproject.com/en/3.1/howto/custom-management-commands/)  


We need to add some _users_

At ``/users/`` POST should send through body request some data like this `{'username': 'usertest'}`
All other rest methods are allowed here, but not necessary to use. Just in frontend part.

At ``/tasks/`` POST should send data ``{'user_id': 1, 'status': 'D', 'description': 'Test from api'}``
**User_id** is a foreign key to store user id created before.
**Description** is a char field with 1000 characters max length.
**Status** is a char field with only one character. The three options are _'C', 'P' and 'D'_ 
that corresponds to Created, In Progress and Done.

In GET we have two option, get all tasks and get filtering by user id associated in the task

To get all tasks use GET ``/tasks/``
To get by user tasks use GET ``/tasks/?user_id=1`` - change 1 for user id you want.

In PUT through api requests we can update any field, but in front just _status_ are available.
Example using data in POST, to update status just change this field to one of the options.
You need send PUT request to ``/tasks/task_id/`` with follow data.
``{'user_id': 1, 'status': 'P', 'description': 'Test from api'}``

Task_id is a UUID field auto-generated.

To delete some task send DELETE request to ``/tasks/task_id/``.
 
After run this project clone [frontend](https://github.com/matheusads/smartket_frontend) part and use.

**_PS:_**  
My known errors.  
For the sake of simplicity of these project I also didn't use git branches.
My commit are have a lot of code too.
I didn't add some much unit tests(users mainly) either postman tests.  
In Angular app I should create unit test and reusable components.
The Users and Tasks lists could be the same component for example. _In these cases I use the awesome copy-paste programming._

