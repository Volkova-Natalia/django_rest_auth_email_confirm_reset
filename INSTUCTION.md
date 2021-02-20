# How to write an Installable Django Application  
Suppose, you have a real django project with the following architecture:  
<details>  
<summary>show the architecture</summary>  

```
real_django_project/
|
|__ django_rest_auth_email_confirm_reset/
|   |__ serialisers/
|   |   |__ ...
|   |__ templates/
|   |   |__ ...
|   |__ tests/
|   |   |__ ...
|   |__ utils/
|   |   |__ ...
|   |__ views/
|   |   |__ ...
|   |
|   |__ __init__.py
|   |__ admin.py
|   |__ apps.py
|   |__ models.py
|   |__ settings.py
|   |__ urls.py
|
|__ real_django_project/
|   |__ __init__.py
|   |__ asgi.py
|   |__ settings.py
|   |__ urls.py
|   |__ wsgi.py
|
|__ requirements/
|   |__ ...
|
|__ .env
|__ .env.sample
|__ db.sqlite3
|__ manage.py
|__ requirements.txt
```
</details>  

And you want to package the **django_rest_auth_email_confirm_reset** application.  

<br>  



___
## Moving your Application out of the Project  
You should move the **django_rest_auth_email_confirm_reset** application out of the **real_django_project** project.  
The directory structure will look something like this:  
<details>  
<summary>show the directory structure</summary>  

```
django_rest_auth_email_confirm_reset/
|
|__ django_rest_auth_email_confirm_reset/
    |__ serialisers/
    |   |__ ...
    |__ templates/
    |   |__ ...
    |__ tests/
    |   |__ ...
    |__ utils/
    |   |__ ...
    |__ views/
    |   |__ ...
    |
    |__ __init__.py
    |__ admin.py
    |__ apps.py
    |__ models.py
    |__ settings.py
    |__ urls.py



real_django_project/
|
|__ real_django_project/
|   |__ __init__.py
|   |__ asgi.py
|   |__ settings.py
|   |__ urls.py
|   |__ wsgi.py
|
|__ requirements/
|   |__ ...
|
|__ .env
|__ .env.sample
|__ db.sqlite3
|__ manage.py
|__ requirements.txt
```
</details>  

<br>  




___
## Testing your separated Application  

### Bootstrapping Django outside of a Project  
Now that your app is outside of a Django project, you can not use the Django **manage.py** command to test your application as when the application was a part of **real_django_project**.  

You should create sample django project:  
<details>  
<summary>show the directory structure</summary>  

```
django_rest_auth_email_confirm_reset/
|
|__ django_rest_auth_email_confirm_reset/
|   |__ ...
|
|__ project_sample/
    |__ backend_django/
        |__ backend_django/
        |   |__ __init__.py
        |   |__ asgi.py
        |   |__ settings.py
        |   |__ urls.py
        |   |__ wsgi.py
        |
        |__ requirements/
        |   |__ ...
        |
        |__ .env
        |__ .env.sample
        |__ db.sqlite3
        |__ manage.py
        |__ requirements.txt
```
</details>  

<br>

Else, you should create a file with configuration of Django **boot_django.py**:  
<details>  
<summary>show the directory structure</summary>  

```
django_rest_auth_email_confirm_reset/
|
|__ django_rest_auth_email_confirm_reset/
|   |__ ...
|
|__ project_sample/
|   |__ ...
|
|__ boot_django.py
```
</details>  

<details>
<summary>show 'boot_django.py' code</summary>  

```python
# This file sets up and configures Django. It's used by scripts that need to
# execute as if running in a Django server.
import os
import django
from django.conf import settings


BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), "django_rest_auth_email_confirm_reset"))


def boot_django():
    settings.configure(
        BASE_DIR=BASE_DIR,
        DEBUG=True,
        ALLOWED_HOSTS=[
            '127.0.0.1',
            'localhost',
        ],
        INSTALLED_APPS=[
            'django.contrib.admin',
            'django.contrib.auth',
            'django.contrib.contenttypes',
            'django.contrib.sessions',
            'django.contrib.messages',
            'django.contrib.staticfiles',
            'rest_framework',
            'django_rest_auth_email_confirm_reset',
        ],
        MIDDLEWARE=[
            'django.middleware.security.SecurityMiddleware',
            'django.contrib.sessions.middleware.SessionMiddleware',
            'django.middleware.common.CommonMiddleware',
            'django.middleware.csrf.CsrfViewMiddleware',
            'django.contrib.auth.middleware.AuthenticationMiddleware',
            'django.contrib.messages.middleware.MessageMiddleware',
            'django.middleware.clickjacking.XFrameOptionsMiddleware',
        ],
        ROOT_URLCONF='django_rest_auth_email_confirm_reset.urls',
        TEMPLATES=[
            {
                'BACKEND': 'django.template.backends.django.DjangoTemplates',
                'DIRS': [
                    os.path.join(BASE_DIR, 'templates'),
                ]
                ,
                'APP_DIRS': True,
                'OPTIONS': {
                    'context_processors': [
                        'django.template.context_processors.debug',
                        'django.template.context_processors.request',
                        'django.contrib.auth.context_processors.auth',
                        'django.contrib.messages.context_processors.messages',
                    ],
                },
            },
        ],
        DATABASES={
            'default': {
                'ENGINE': 'django.db.backends.sqlite3',
                'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
            }
        },
        AUTH_USER_MODEL='django_rest_auth_email_confirm_reset.User',
        AUTH_PASSWORD_VALIDATORS=[
            {
                'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
            },
            {
                'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
            },
            {
                'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
            },
            {
                'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
            },
        ],

        LANGUAGE_CODE='en-us',
        TIME_ZONE="UTC",
        USE_I18N=True,
        USE_L10N=True,
        USE_TZ=True,

        STATIC_URL='/static/',
        STATICFILES_DIRS=[
            os.path.join(BASE_DIR, 'static'),
            os.path.join(BASE_DIR),  # for swagger.json
            os.path.join(os.path.dirname(BASE_DIR)),  # for swagger.json
        ],
    )
    django.setup()
```
</details>  

<br>  

### Running management commands with your Installable Django Application
Now that you have **boot_django.py**, you can run any Django management command with a script like this:  
<details>
<summary>show script code</summary>  

```python
from django.core.management import call_command
from boot_django import boot_django

# call the django setup routine
boot_django()
call_command("makemigrations", "django_rest_auth_email_confirm_reset")
```
</details>  

You can add the **scripts** to your folder:  
<details>  
<summary>show the directory structure</summary>  

```
django_rest_auth_email_confirm_reset/
|
|__ django_rest_auth_email_confirm_reset/
|   |__ ...
|
|__ project_sample/
|   |__ ...
|
|__ boot_django.py
|
|__ djangoshell.py
|__ makemigrations.py
|__ migrate.py
|__ runserver.py
|__ test.py
```
</details>  

<br>

### Testing your Installable Django Application  
<details>  
<summary>show actions and commands to test</summary>  

**Install virtualenv**  
```
pip install virtualenv
```

Next, you must work from the root directory **backend_django**.

<br>

**Create a virtual environment**  
```
path_to_django_rest_auth_email_confirm_reset\project_sample\backend_django: virtualenv venv
```

<br>

**Activate the virtual environment**  
For Windows:
```
path_to_django_rest_auth_email_confirm_reset\project_sample\backend_django: venv\Scripts\activate.bat
```
For Linux:  
```
path_to_django_rest_auth_email_confirm_reset\project_sample\backend_django: source venv/bin/activate
```
After the command your command line will look like this:  
```
(venv) path_to_django_rest_auth_email_confirm_reset\project_sample\backend_django: $
```

<br>

**Deactivate the virtual environment**  
If you want to deactivate the virtual environment, you can use the command:  
```
(venv) path_to_django_rest_auth_email_confirm_reset\project_sample\backend_django: deactivate
```
*In general, you should skip this step.*  

<br>

**Choose the correct WORK_STAGE**  
Choose the correct work stage in the file **.env**:  
```python
WORK_STAGE = "test_before_packaging" 
```
You should choose only **one** stage!  
 
<br>

**Install requirements**  
Choose the correct file with requirements for the work stage in the file **requirements.txt**:  
```text
-r requirements/test_before_packaging.txt
```
You should choose only **one** file!  

Install all requirements:  
```
(venv) path_to_django_rest_auth_email_confirm_reset\project_sample\backend_django: pip install -r requirements.txt
```

<br>

Now, you can run tests, perform migrations and apply them, run server by calling appropriate scripts like this:  
```
(venv) path_to_django_rest_auth_email_confirm_reset\project_sample\backend_django: ..\..\test.py
``` 

</details>  

<br>

Or you can use script **test_before_packaging.py** instead all commands:
```
path_to_django_rest_auth_email_confirm_reset: test_before_packaging.py
```  
It is not exclude choosing the correct work stage in the file **.env**:  
```python
WORK_STAGE = "test_before_packaging" 
```

<br>





___
## Packaging your Application

### Add files README.md and LICENSE  
<details>  
<summary>show the directory structure</summary>  

```
django_rest_auth_email_confirm_reset/
|
|__ django_rest_auth_email_confirm_reset/
|   |__ ...
|
|__ project_sample/
|   |__ ...
|
|__ boot_django.py
|
|__ djangoshell.py
|__ makemigrations.py
|__ migrate.py
|__ runserver.py
|__ test.py
|
|__ README.md
|__ LICENSE
```
</details>  

<br>

### Defining your Installable Package with setup.cfg 
This **setup.cfg** file describes the package that you’ll build.  
<details>
<summary>show 'setup.cfg' code</summary>  

```python
[metadata]
name = django_rest_auth_email_confirm_reset
version = 0.1
description = Packaged rest application to work with authentication confirmation and password reset with using email.
long_description = file: README.md
url = https://github.com/Volkova-Natalia/django_rest_auth_email_confirm_reset
author = Volkova Natalia
license = MIT
classifiers =
    Environment :: Web Environment
    Framework :: Django
    Framework :: Django :: 3.1.6
    Intended Audience :: Developers
    License :: OSI Approved :: MIT License
    Operating System :: OS Independent
    Programming Language :: Python
    Programming Language :: Python :: 3
    Programming Language :: Python :: 3 :: Only
    Programming Language :: Python :: 3.8
    Topic :: Software Development :: Libraries :: Application Frameworks
    Topic :: Software Development :: Libraries :: Python Modules

[options]
include_package_data = True
packages = find:
python_requires = >=3.8
install_requires =
    Django>=3.1.6
    djangorestframework>=3.12.2
test_suite = test.get_suite
```
</details>    

<br>

Else, you need a **setup.py** script, which will automatically use your **setup.cfg** file.  
<details>
<summary>show 'setup.py' code</summary>  

```python
if __name__ == "__main__":
    from setuptools import setup

    setup()
```
</details>  

<br>

Only Python modules and packages will be included in the package by default.
You need a **MANIFEST.in** file to include additional files.  
<details>
<summary>show 'MANIFEST.in' code</summary>  

```text
include LICENSE
include README.md
recursive-include django_rest_auth_email_confirm_reset/static *
recursive-include django_rest_auth_email_confirm_reset/templates *
```
</details> 

<br>

It’s considered best practice to include a **pyproject.toml** file with your package.  
<a href=https://snarky.ca/what-the-heck-is-pyproject-toml>An article on the subject</a> can run you through the details.  
<details>
<summary>show 'pyproject.toml' code</summary>  

```text
[build-system]
requires = ["setuptools >= 53.0.0", "wheel >= 0.36.2"]
build-backend = "setuptools.build_meta"
```
</details> 

<br>


<details>  
<summary>show the directory structure</summary>  

```
django_rest_auth_email_confirm_reset/
|
|__ django_rest_auth_email_confirm_reset/
|   |__ ...
|
|__ project_sample/
|   |__ ...
|
|__ boot_django.py
|
|__ djangoshell.py
|__ makemigrations.py
|__ migrate.py
|__ runserver.py
|__ test.py
|
|__ README.md
|__ LICENSE
|
|__ setup.cfg
|__ setup.py
|__ MANIFEST.in
|__ pyproject.toml
```
</details>  

<br>

### Testing your Installable Package  
<details>  
<summary>show actions and commands to test</summary>  

You should use new environment. If you have folder **venv** in *'path_to_django_rest_auth_email_confirm_reset\project_sample\backend_django'*, delete it and create new:  

**Install virtualenv**  
```
pip install virtualenv
```

Next, you must work from the root directory **backend_django**.

<br>

**Create a virtual environment**  
```
path_to_django_rest_auth_email_confirm_reset\project_sample\backend_django: virtualenv venv
```

<br>

**Activate the virtual environment**  
For Windows:
```
path_to_django_rest_auth_email_confirm_reset\project_sample\backend_django: venv\Scripts\activate.bat
```
For Linux:  
```
path_to_django_rest_auth_email_confirm_reset\project_sample\backend_django: source venv/bin/activate
```
After the command your command line will look like this:  
```
(venv) path_to_django_rest_auth_email_confirm_reset\project_sample\backend_django: $
```

<br>

**Deactivate the virtual environment**  
If you want to deactivate the virtual environment, you can use the command:  
```
(venv) path_to_django_rest_auth_email_confirm_reset\project_sample\backend_django: deactivate
```
*In general, you should skip this step.*  

<br>

**Choose the correct WORK_STAGE**  
Choose the correct work stage in the file **.env**:  
```python
WORK_STAGE = "test_after_packaging" 
```
You should choose only **one** stage!  
 
<br>

**Install requirements**  
Choose the correct file with requirements for the work stage in the file **requirements.txt**:  
```text
-r requirements/test_after_packaging.txt
```
You should choose only **one** file!  

Install all requirements:  
```
(venv) path_to_django_rest_auth_email_confirm_reset\project_sample\backend_django: pip install -r requirements.txt
```

<br>

**Add INSTALLED_APPS**  
Edit your **settings.py** file to include **django_rest_auth_email_confirm_reset** in the **INSTALLED_APPS** listing:  
```python
INSTALLED_APPS = [
    ...
    'django_rest_auth_email_confirm_reset',
]
``` 

<br>

**Define an user model**  
Specify a custom user model from the **django_rest_auth_email_confirm_reset** application as the default user model for your project using the **AUTH_USER_MODEL** setting in your **settings.py**:  
```python
AUTH_USER_MODEL = 'django_rest_auth_email_confirm_reset.User'
```

<br>

**Using the Django *manage.py* command**  
Now, you can make all as in usual django project.  
For example, you can run tests:  
```
(venv) path_to_django_rest_auth_email_confirm_reset\project_sample\backend_django: manage.py test
``` 
Or so:  
```
(venv) path_to_django_rest_auth_email_confirm_reset\project_sample\backend_django: manage.py test django_rest_auth_email_confirm_reset
``` 

</details>  

<br>

Or you can use script **test_after_packaging.py** instead all commands:
```
path_to_django_rest_auth_email_confirm_reset: test_after_packaging.py
```
It is not exclude editing your **settings.py** file to include **django_rest_auth_email_confirm_reset** in the **INSTALLED_APPS** listing:  
```python
INSTALLED_APPS = [
    ...
    'django_rest_auth_email_confirm_reset',
]
```   
It is not exclude specifying a custom user model from the **django_rest_auth_email_confirm_reset** application as the default user model for your project using the **AUTH_USER_MODEL** setting in your **settings.py**:  
```python
AUTH_USER_MODEL = 'django_rest_auth_email_confirm_reset.User'
```
It is not exclude choosing the correct work stage in the file **.env**:  
```python
WORK_STAGE = "test_after_packaging" 
```

<br>






___
## Building your Package  
Using the command:  
```
(venv) path_to_django_rest_auth_email_confirm_reset\: python setup.py sdist
```  
This creates a directory called **dist** and builds your new package, **django_rest_auth_email_confirm_reset-0.1.tar.gz**.  

<br>

<details>  
<summary>show the directory structure</summary>  

```
django_rest_auth_email_confirm_reset/
|
|__ dist/
|   |__ django_rest_auth_email_confirm_reset-0.1.tar.gz
|
|__ django_rest_auth_email_confirm_reset/
|   |__ ...
|
|__ project_sample/
|   |__ ...
|
|__ boot_django.py
|
|__ djangoshell.py
|__ makemigrations.py
|__ migrate.py
|__ runserver.py
|__ test.py
|
|__ README.md
|__ LICENSE
|
|__ setup.cfg
|__ setup.py
|__ MANIFEST.in
|__ pyproject.toml
```
</details>  

<br>

### Testing your Built Package  
<details>  
<summary>show actions and commands to test</summary>  

You should use new environment. If you have folder **venv** in *'path_to_django_rest_auth_email_confirm_reset\project_sample\backend_django'*, delete it and create new:  

**Install virtualenv**  
```
pip install virtualenv
```

Next, you must work from the root directory **backend_django**.

<br>

**Create a virtual environment**  
```
path_to_django_rest_auth_email_confirm_reset\project_sample\backend_django: virtualenv venv
```

<br>

**Activate the virtual environment**  
For Windows:
```
path_to_django_rest_auth_email_confirm_reset\project_sample\backend_django: venv\Scripts\activate.bat
```
For Linux:  
```
path_to_django_rest_auth_email_confirm_reset\project_sample\backend_django: source venv/bin/activate
```
After the command your command line will look like this:  
```
(venv) path_to_django_rest_auth_email_confirm_reset\project_sample\backend_django: $
```

<br>

**Deactivate the virtual environment**  
If you want to deactivate the virtual environment, you can use the command:  
```
(venv) path_to_django_rest_auth_email_confirm_reset\project_sample\backend_django: deactivate
```
*In general, you should skip this step.*  

<br>

**Choose the correct WORK_STAGE**  
Choose the correct work stage in the file **.env**:  
```python
WORK_STAGE = "work_after_building_local" 
```
Or, if you committed the source archive and want to work with it:  
```python
WORK_STAGE = "work_after_building_commit" 
```
You should choose only **one** stage!  
 
<br>

**Install requirements**  
Choose the correct file with requirements for the work stage in the file **requirements.txt**:  
```text
-r requirements/work_after_building_local.txt
```
Or, if you committed the source archive and want to work with it:  
```text
-r requirements/work_after_building_commit.txt
```
You should choose only **one** file!  

Install all requirements:  
```
(venv) path_to_django_rest_auth_email_confirm_reset\project_sample\backend_django: pip install -r requirements.txt
```

<br>

**Check INSTALLED_APPS**  
Make sure your **settings.py** file includes **django_rest_auth_email_confirm_reset** in the **INSTALLED_APPS** listing:  
```python
INSTALLED_APPS = [
    ...
    'django_rest_auth_email_confirm_reset',
]
``` 

<br>

**Check an user model**  
Make sure your default user model in **settings.py** file is a custom user model from the **django_rest_auth_email_confirm_reset**:  
```python
AUTH_USER_MODEL = 'django_rest_auth_email_confirm_reset.User'
```

<br>

**Using the Django *manage.py* command**  
Now, you can make all as in usual django project.  
For example, you can run tests:  
```
(venv) path_to_django_rest_auth_email_confirm_reset\project_sample\backend_django: manage.py test
``` 
Or so:  
```
(venv) path_to_django_rest_auth_email_confirm_reset\project_sample\backend_django: manage.py test django_rest_auth_email_confirm_reset
``` 

</details>  

<br>

Or you can use script **test_after_building_local.py** instead all commands:
```
path_to_django_rest_auth_email_confirm_reset: test_after_building_local.py
```
Or, if you committed the source archive and want to work with it, you can use script **test_after_building_commit.py** instead all commands:  
```
path_to_django_rest_auth_email_confirm_reset: test_after_building_commit.py
```  
It is not exclude editing your **settings.py** file to include **django_rest_auth_email_confirm_reset** in the **INSTALLED_APPS** listing:  
```python
INSTALLED_APPS = [
    ...
    'django_rest_auth_email_confirm_reset',
]
```   
It is not exclude specifying a custom user model from the **django_rest_auth_email_confirm_reset** application as the default user model for your project using the **AUTH_USER_MODEL** setting in your **settings.py**:  
```python
AUTH_USER_MODEL = 'django_rest_auth_email_confirm_reset.User'
```
It is not exclude choosing the correct work stage in the file **.env**:  
```python
WORK_STAGE = "work_after_building_local" 
```
Or, if you committed the source archive and want to work with it:  
```python
WORK_STAGE = "work_after_building_commit" 
```

<br>










<br>

<br>



___
## Docs, Articles & Sources
* <a href=https://snarky.ca/what-the-heck-is-pyproject-toml>What the heck is pyproject.toml?</a>  
* <a href=https://realpython.com/installable-django-app/>How to Write an Installable Django App</a>  
