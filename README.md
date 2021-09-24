# Url-Shortener

This is an url shortener Rest API which takes url as an input and gives an short url as response. 
This API is built using Django Rest Framework
This API also contains swagger API doc to test API

__________________________________________________________________________________________________

#Setting up this project locally.

- Make sure you have installed python, django, django rest framework and swagger.
- git clone the project in your local directory 
- open the cloned project/directory in any IDE/editor and enter into the 'project' directory
- type 'python manage.py runserver', now the django's inbuilt server gets started and display a localhost link on your terminal
- click on the link and browsable api gets open, you will get all the previous original and short link if you have in db.
- to get short url from long url, type '/create/' after localhost link in your browser
- then enter your url in the original_url field and click post, you will get a short url as a response on the same browser 
- copy the short url and paste in your browser it redirects to the original url
 
