# Introduction 

Bike bros is intended to be a site for Motorcycle enthusiasts to come together. The site allows users to and share photos of their bikes. The app also encourages users to create Bike Meets where like-minded people can meet to show off their bikes.

# Deplyed FRONTEND website 
A link to the live website can be found [here](https://fe-bike-bros.herokuapp.com/)

# Deployed BACKEND website 
A link to the live website can be found [here](https://bike-bros.herokuapp.com/)

# DRF README
A link to the FRONTEND README can be found here [here](https://github.com/JoeQuigley1/pp5-fe-bike-brothers/blob/main/README.md)


# Manual Testing 

## Testing steps
1. Manually verify that all url paths are created an working without error.
2. Verify that CRUD functionality is working in the following: Meetups, Comments, Followers, Likes, Posts and Profiles.
- Check link to each.
- Create a new item. 
- Check the new URL is working
- Check Edit fuctionality is working. (excluding Likes, Followers and Profiles)
- Check delete fucntionality is working. (exluding Users and Profiles)
3. Check Search functionlity is working for Posts.
4. Reapeat steps 1-3 for the Deployed API. 

## URL Testing

| Feature | Expected Result |    Actual Result   | Development|Deployment| Comments |
|-------|-----|----|----|----|------|
|Root URL|Display Welcome message|As Expected|Pass|Pass|N/A|
|Profiles|Display Profiles list|As Expected|Pass|TBD|N/A|
|Profiles Id|Display Profiles Detail|As Expected|Pass|TBD|N/A|
|Posts|Display Post List|As Expected|Pass|TBD|N/A|
|Posts Id|Display Post Detail|As Expected|Pass|TBD|N/A|
|Comments|Display Comment List|As Expected|Pass|TBD|N/A|
|Comments|Display Comment Detail|As Expected|Pass|TBD|N/A|
|Likes|Display Likes List|As Expected|Pass|TBD|N/A|
|List Id|Display Like Detail|As Expected|Pass|TBD|N/A|
|Followers|Display Follower List|As Expected|Pass|TBD|N/A|
|Followers|Display Follower Detail|As Expected|Pass|TBD|N/A|
|Meetups|Display Meetup List|As Expected|Pass|TBD|N/A|
|Meetups Id|Display Meetups Detail|As Expected|Pass|TBD|N/A|
|Contact|Display Contact List|As Expected|Pass|TBD|N/A|


- All URLs are tested and are working in Develpoment. 

## CRUD Testing

| Feature | Expected Result |    Actual Result   | Development|Deployment| Comments |
|-------|-----|----|----|----|------|
|Profiles|Profile can becreated |As Expected|Pass|TBD|N/A|
|Posts| Post can be created|As Expected|Pass|TBD|N/A|
|Posts| Post can be edited|As Expected|Pass|TBD|As Owner
|Posts| Post can be deleted|As Expected|Pass|TBD|As Owner
|Comments| Comment can be created|As Expected|Pass|TBD|N/A|
|Comments| Comment can be edited|As Expected|Pass|TBD|As Owner|
|Comments| Comment can be deleted|As Expected|Pass|TBD|As Owner|
|Likes| Likes can be created|As Expected|Pass|TBD|N/A|
|Likes| Likes can be deleted|As Expected|Pass|TBD|As Owner|
|Followers| Followers can be created|As Expected|Pass|TBD|N/A|
|Followers| Followers can be deleted|As Expected|Pass|TBD|N/A|
|Meetups|Meetup can be created|As Expected|Pass|TBD|N/A|
|Meetups |Meetup can be edited|As Expected|Pass|TBD|N/A|
|Meetups |Meetup can be deleted|As Expected|Pass|TBD|N/A|
|Contact|Contact  can be created|As Expected|Pass|TBD|N/A|


## Search Functionality testing
### Pending writeup

# Technologies Used: 

- Python

# Frameworks and Libraries Used: 

- Django
- Django RestFramework
- Cloudinary
- Heroku 
- Pillow
- Django Rest Auth
- PostgresSQL
- Cors Headers


# Modules and dependancies 

![Requirements](static/screenshots/Modules.png)

# Platforms 

- Cloudinary - Storage of image files
- Github - Repository with GIT version control
- Gitpod - IDE for development
- Heroku - Hosting/ Deployment of DRF database and React site
- Elephant SQL - Hosting of DRF database. 

# Project Setup
1. Create a new repository from the Code institute template respository.
2. Run terminal command pip3 install 'django<4' to install Django.
4. Run terminal command django-admin startproject drf_api . (drf-ap is the name of my api - make sure to include the dot at the end to initialize project in it's current directory).
5. Run terminal command pip install django-cloudinary-storage to install Django Cloudinary Storage.
6. Run terminal command pip install Pillow to install Pillow image processing capabilities (note the uppercase 'P').
7. Add the newly installed apps 'cloudinary_storage' and 'cloudinary' to INSTALLED_APPS in settings.py as shown below:
``` 
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'cloudinary_storage', 
    'django.contrib.staticfiles',
    'cloudinary',
] 
```
7. Create an env.py file in the top directory, import and add ClOUDINARY_URL as show below:
```
import os
os.environ["CLOUDINARY_URL"] = "cloudinary://API KEY HERE"
```

8. In the settings.py file load environment variable with Cloudinary your credientials, set a CLOUDINARY_STORAGE variable, make a MEDIA_URL folder and set a DEFAULT_FILE_STORAGE variable as below:
```
import os

if os.path.exists('env.py'):
    import env


CLOUDINARY_STORAGE = {
    'CLOUDINARY_URL': os.environ.get('CLOUDINARY_URL')
}
MEDIA_URL = '/media/'
DEFAULT_FILE_STORAGE = 'cloudinary_storage.storage.MediaCloudinaryStorage'
```

# Deployment 
1. Install JWT awthentication by running the `pip3 install dj-rest-auth==2.1.9` in the terminal. 
2. Add 'rest_framework.authtoken' and 'dj_rest_auth' to the list of INSTALLED_APPS in settings.py as below:
```
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'cloudinary_storage',
    'django.contrib.staticfiles',
    'cloudinary',
    'location_field.apps.DefaultConfig',
    'rest_framework',
    'django_filters',
    'rest_framework.authtoken',
    'dj_rest_auth',
```
3. ADD `SITE_ID = 1` to settings.py
4. Add the dj-rest-auth urls paths to the main urls.py file as below:
```
urlpatterns = [
    path('', root_route),
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path('dj-rest-auth/', include('dj_rest_auth.urls')),
```
5. To install the JSON tokens, run terminal command `pip install djangoframework-simplejwt`
6. Set [DEV] to 1 in the env.py file:
```
os.environ['DEV'] = '1'
```
7. In to settings.py add the following if/else statement:
```
REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': [(
        'rest_framework.authentication.SessionAuthentication'
        if 'DEV' in os.environ
        else 'dj_rest_auth.jwt_auth.JWTCookieAuthentication'
    )],
```
8. To enable token authentication, set REST_USE_JWT to True. To ensure tokens are sent over HTTPS only, set JWT_AUTH_SECURE to True. Cookie names must also be declared. To do all of this, add the following code below the if/else statement just added to settings.py:
```
REST_USE_JWT = True
JWT_AUTH_SECURE = True
JWT_AUTH_COOKIE = 'my-app-auth'
JWT_AUTH_REFRESH_COOKIE = 'my-refresh-token'
```
9. Create serializers.py file in the drf_api directory, and copy UserDetailsSerializer code from Django documentation as follows:
```
from dj_rest_auth.serializers import UserDetailsSerializer
from rest_framework import serializers


class CurrentUserSerializer(UserDetailsSerializer):
    profile_id = serializers.ReadOnlyField(source='profile.id')
    profile_image = serializers.ReadOnlyField(source='profile.image.url')

    class Meta(UserDetailsSerializer.Meta):
        fields = UserDetailsSerializer.Meta.fields + (
            'profile_id', 'profile_image'
        )
```
10. Overwrite the default user detail serializer in settings.py with the following:
```
REST_AUTH_SERIALIZERS = {
    'USER_DETAILS_SERIALIZER': 'drf_api.serializers.CurrentUserSerializer'
}
```
11. Once complete in the terminal migrate the database
12. Update requirements.txt
```
 pip freeze --local > requirements.txt
``` 
### Prepare API for Deployment
13. In the drf_api directory, create a views.py file add a route_route to create custom message by adding the following code:
```
from rest_framework.decorators import api_view
from rest_framework.response import Response

@api_view()
def root_route(request):
    return Response({
        "message": "Welcome to my drf API"
    })
```
14. Import to the main urls.py file, and add to the top of the urlpatterns list as follows:
```
from .views import root_route

urlpatterns = [
    path('', root_route),

```
15. To set up page pagination and to render the date time format in a clear and readbale format add the following to settings.py (inside REST_FRAMEWORK):
```
REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': [(
        'rest_framework.authentication.SessionAuthentication'
        if 'DEV' in os.environ
        else 'dj_rest_auth.jwt_auth.JWTCookieAuthentication'
    )],
    'DEFAULT_PAGINATION_CLASS':
        'rest_framework.pagination.PageNumberPagination',
    'PAGE_SIZE': 10,
    'DATETIME_FORMAT': '%d %b %Y',
}
```
16. Set the default renderer to JSON for the production environment in settings.py:
```
if 'DEV' not in os.environ:
    REST_FRAMEWORK['DEFAULT_RENDERER_CLASSES'] = [
        'rest_framework.renderers.JSONRenderer',
    ]
```
### Pending
17. For comments, set DATETIME format to show how long ago a comment was created and updated. To do this, add the following code to any serializers.py files within comment apps:
```
created_at = serializers.SerializerMethodField()
updated_at = serializers.SerializerMethodField()

def get_created_at(self, obj):
        return naturaltime(obj.created_at)

    def get_updated_at(self, obj):
        return naturaltime(obj.updated_at)
```
18. Add, push and commit changes to Github.
19. In [Eephant SQL](https://www.elephantsql.com/) Click “Create New Instance" 
20. Give your plan a Name (this is commonly the name of the project)
21. Select the Tiny Turtle (Free) plan
22. Select “Select Region”
23. Select a data center near you.
24. Then click “Review”.
25. Check your details are correct and then click “Create instance”.
26. Return to the ElephantSQL dashboard and click on the database instance name for the project
27. In the URL section, click the copy icon to copy the database URL
28. Create the project app on [Heroku](https://www.heroku.com/)
29. Go to 'Settings' and click on 'Reveal Config Vars'
30. Add a Config Var DATABASE_URL, and for the value, copy in your database URL from ElephantSQL (do not add quotation marks)
31. Back in the DRF app, In the terminal, install `dj_database_url` and `psycopg2`, (both of these are needed to connect to your external database) as seen bwlow:
```
 pip3 install dj_database_url==0.5.0 psycopg2
```
32. In the settings.py file, import dj_database_url underneath the import for os as seen below:
```
 import os
 import dj_database_url
```
33. Update the DATABASES section to the following:
```
 if 'DEV' in os.environ:
     DATABASES = {
         'default': {
             'ENGINE': 'django.db.backends.sqlite3',
             'NAME': BASE_DIR / 'db.sqlite3',
         }
     }
 else:
     DATABASES = {
         'default': dj_database_url.parse(os.environ.get("DATABASE_URL"))
     }
```
34. In the env.py file, add a new environment variable with the key set to DATABASE_URL, and the value to your ElephantSQL database URL as seen below:
```
 os.environ['DATABASE_URL'] = "<your PostgreSQL URL here>"
```
35. Migrate your database models to your new database by enter the following into the terminal:
```
 python3 manage.py migrate
```
36. Create a superuser to test the migration was successful. Use the following command and follow the prompts:
```
 python3 manage.py createsuperuser
``` 
37. On the ElephantSQL page for your database, in the left side navigation, select “BROWSER”
38. Click the Table queries button, select auth_user
39. When you click “Execute”, you should see your newly created superuser details displayed. This confirms your tables have been created and you can add data to your database.
40. In the terminal of your IDE workspace, install gunicorn:
```
 pip3 install gunicorn django-cors-headers
```
41. Update requirements.txt
```
 pip freeze --local > requirements.txt
``` 
42. Create a Procfile and add the following:

```
release: python manage.py makemigrations && python manage.py migrate
web: gunicorn drf_api.wsgi
```
43. In your settings.py file, update the value of the ALLOWED_HOSTS variable to include your Heroku app’s URL as below:
```
 ALLOWED_HOSTS = ['localhost', '<your_app_name>.herokuapp.com']
```
44. Add corsheaders to INSTALLED_APPS
```
INSTALLED_APPS = [
    ...
    'dj_rest_auth.registration',
    'corsheaders',
    ...
 ]
```
45. Add corsheaders middleware to the TOP of the MIDDLEWARE
```
SITE_ID = 1
 MIDDLEWARE = [
     'corsheaders.middleware.CorsMiddleware',
     ...
 ]
```
46. Under the MIDDLEWARE list, set the ALLOWED_ORIGINS for the network requests made to the server with the following code:
```
if 'CLIENT_ORIGIN' in os.environ:
     CORS_ALLOWED_ORIGINS = [
         os.environ.get('CLIENT_ORIGIN')
     ]
 else:
     CORS_ALLOWED_ORIGIN_REGEXES = [
         r"^https://.*\.gitpod\.io$",
     ]
```
47. Back on the Heroku dashboard for your new app, open the Settings tab
48. Add SECRET_KEY(Make sure you change your initial SECRET KEY) and CLOUDINARY_URL(Do not include the quotaion marks) to the Config Vars
49. Open the Deploy tab and in the Deployment method section, select Connect to GitHub
50. Search for the DRF repo in Github and connect to the heroku app. 
51. Use the Manual deploy section and click Deploy Branch. Click the  View Deploy and once the app is deployed successfully Open the app to ensure it is working correctly. 

APPLY dj-rest-auth Bug Fix
52.  In drf_api/views.py, import JWT_AUTH settings from settings.py
```
from .settings import (
    JWT_AUTH_COOKIE, JWT_AUTH_REFRESH_COOKIE, JWT_AUTH_SAMESITE,
    JWT_AUTH_SECURE,
)

```
53. then, add the following log out view code:
```
@api_view(['POST'])
def logout_route(request):
    response = Response()
    response.set_cookie(
        key=JWT_AUTH_COOKIE,
        value='',
        httponly=True,
        expires='Thu, 01 Jan 1970 00:00:00 GMT',
        max_age=0,
        samesite=JWT_AUTH_SAMESITE,
        secure=JWT_AUTH_SECURE,
    )
    response.set_cookie(
        key=JWT_AUTH_REFRESH_COOKIE,
        value='',
        httponly=True,
        expires='Thu, 01 Jan 1970 00:00:00 GMT',
        max_age=0,
        samesite=JWT_AUTH_SAMESITE,
        secure=JWT_AUTH_SECURE,
    )
    return response
```
54. In the main urls.py file, import the logout_route:
```
from .views import root_route, logout_route
```
55. Add the urls patterns as below:
```
path('dj-rest-auth/logout/', logout_route),
    path('dj-rest-auth/', include('dj_rest_auth.urls')),
```
56. Add commit and push the changes to Github. 

Final Deployment Steps

57. In settings.py, in the ALLOWED_HOSTS list, copy your ‘... .herokuapp.com’ as below:
```
ALLOWED_HOSTS = [
    '... .herokuapp.com',
    'localhost',
]
```
58. In Heroku click settings and then reveal Config Vars, Add the new key of ALLOWED_HOST with the value for your deployed Heroku application URL.
59. In settings Back in settings.py, replace your ALLOWED HOSTS list '... .herokuapp.com' as below:
```
ALLOWED_HOSTS = [
   os.environ.get('ALLOWED_HOST'),
   'localhost',
]
```
60. Because my project was created using Gitpod I added the CLIENT_ORIGIN_DEV.
61. In settings.py import `import re` 
62. Replace the existing if 'CLIENT_ORIGIN' in os.environ: with the following code:
```
if 'CLIENT_ORIGIN_DEV' in os.environ:
    extracted_url = re.match(r'^.+-', os.environ.get('CLIENT_ORIGIN_DEV', ''), re.IGNORECASE).group(0)
    CORS_ALLOWED_ORIGIN_REGEXES = [
        rf"{extracted_url}(eu|us)\d+\w\.gitpod\.io$",
    ]
```
63. Add, commit and push the changes to Github.
64. Once pushed return to Heroku and click "Deploy" and then "Deploy Branch"

# Deployment Elephant SQL 

As of November 2022, Heroku ceased to provide a free service. The hosting of this website is carried out using the free service [Elephant SQL](https://www.elephantsql.com/). 


# Credits
- The Code Institute DRF-API walkthrough as a guide to building a DRF_API.
- [Martina Terlevic](https://github.com/SephTheOverwitch): For help and support throughout a tough year.
- Tutor support for their assistance. 
- Slack for the huge archive of helpful information
