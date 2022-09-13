Nama  : Muhammad Fahreza Azka Arafat
NPM   : 2106752331

1.
        HTTP REQUEST
      ---------------->                 -----> models.py
Client                 urls.py <---> View 
      <----------------                 -----> katalog.html
        HTTP RESPONSE
 When the client sends an HTTP request for the application, the urls.py (project_django) routes the request to the appropriate url using views.py. Views.py will then ren-
 der katalog.html along with the relevant data from models.py. After this is all done the host server will send a HTTP response back to the client.
 
 2. It is possible without a virtual environment. But it will be "messier", with a virtual environment it is easier to keep track of and separate dependencies if you have
 a lot of projects going on. It also makes the deployment faster because it prevents installing unnecesary dependencies on the server.
 
 3.
 STEP 1 : Use the template and clone the repo to my computer.
 STEP 2 : Making a show catalogue function.
 STEP 3 : Routing by adding another path to urlpatterns and defining app name.
 STEP 4 : Making forloop in katalog.html.
 STEP 5 : After finishing up, deploy to heroku as tutored in Lab 0.
