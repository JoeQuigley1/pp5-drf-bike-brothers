# Introduction 

Bike bros is intended to be a site for Motorcycle enthusiasts to come together. The site allows users to and share photos of their bikes. The app also encourages users to create Bike Meets where like-minded people can meet to show off their bikes.

# Deplyed FRONTEND website 
A link to the live website can be found [here](https://fe-bike-bros.herokuapp.com/)

# Deployed BACKEND website 
A link to the live website can be found [here](https://bike-bros.herokuapp.com/)

# DRF README
A link to the FRONTEND README can be found here [here](https://github.com/JoeQuigley1/pp5-fe-bike-brothers/blob/main/README.md)


# Manual Testing 

1. Manually verified each url path is working and opens without error. 

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
3. Run terminal command django-admin startproject pp5_drf_api . (pp5-drf-ap is the name of my api - make sure to include the dot at the end to initialize project in it's current directory).
4. Run terminal command pip install django-cloudinary-storage to install Django Cloudinary Storage.
5. Run terminal command pip install Pillow to install Pillow image processing capabilities (note the uppercase 'P').
6. Add the newly installed apps 'cloudinary_storage' and 'cloudinary' to INSTALLED_APPS in settings.py as shown below:
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


# Deployment Elephant SQL 

As of November 2022, Heroku ceased to provide a free service. The hosting of this website is carried out using the free service [Elephant SQL](https://www.elephantsql.com/). 


# Credits
- The Code Institute DRF-API walkthrough as a guide to building a DRF_API.
- [Martina Terlevic](https://github.com/SephTheOverwitch): For help and support throughout a tough year.
- Tutor support for their assistance. 
- Slack for the huge archive of helpful information
