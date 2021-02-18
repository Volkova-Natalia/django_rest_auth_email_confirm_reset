# django_rest_auth_email_confirm_reset
Packaged rest application to work with authentication confirmation and password reset with using email.  
 
The application realizes custom authentication.   
You can registration and login using **email**.  
When you registration, you should **confirm** yourself using email.  
When you forget your **password**, you can **reset** it using email.  
It is REST application. There are not templates.  

The application uses the following endpoints:  
***/registration/***  
***/confirmation/{uidb64}/{token}/*** - to confirm your email  
***/login/***  
***/logout/***  
***/password-reset/*** - to send a password reset link to your email  
***/password-reset-confirmation/{uidb64}/{token}/*** - to confirm your password reset link and change password  
***/auth-info/*** - to check, the user is authenticated or not  
***/swagger/expected/*** - OpenApi specification of the application  

More information about the endpoints see ***/swagger/expected/***  

<br>

## Install the application  
The application **is not published**, so you should use link to the github repository:  
```shell script
pip install https://github.com/Volkova-Natalia/django_rest_auth_email_confirm_reset/raw/master/dist/django_rest_auth_email_confirm_reset-0.1.tar.gz
```

<br>

Edit your **settings.py** file to include 'django_rest_auth_email_confirm_reset' in the **INSTALLED_APPS** listing:  
```python
INSTALLED_APPS = [
    ...
    'django_rest_auth_email_confirm_reset',
]
```

<br>

And specify a custom user model from the application as the default user model for your project using the **AUTH_USER_MODEL** setting in your **settings.py**:  
```python
AUTH_USER_MODEL = 'django_rest_auth_email_confirm_reset.User'
```

<br>

Edit your project **urls.py** file to import the URLs:  
```python
urlpatterns = [
    ...
    path('auth/', include('django_rest_auth_email_confirm_reset.urls')),
]
```

<br>

Finally, add the models to your database:  
```shell script
./manage.py makemigrations django_rest_auth_email_confirm_reset
```  

