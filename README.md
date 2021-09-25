# Url-Shortener

This is an url shortener Rest API which takes url as an input and gives an short url as response. 
This API is built using Django Rest Framework
This API also contains swagger API doc to test API

__________________________________________________________________________________________________

#API Endpoints.

- 'localhost' to view all the previously generated urls
- 'localhost/create/' to generate short url from long url
- 'localhost/swagger/' displays swagger API test doc

__________________________________________________________________________________________________

#Setting up this project locally.

- Make sure you have installed python, django, django rest framework and swagger
- Git clone the project in your local directory 
- Enter into the 'project' directory
- Type 'python manage.py runserver', now the django's inbuilt server gets started and display a localhost link on your terminal
- Make sure your 'HOST_URL' in settings.py and localhost port are same
- Type localhost and port number on your browser, browsable api gets open and display all the data objects if available in your db.
- Type '/create/' after localhost url in your browser to generate short url from long url
- After post, you will get a short url as a response on the same browser 
- Copy the short url and paste in your browser it redirects to the original url


 
