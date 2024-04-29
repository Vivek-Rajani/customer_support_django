# How to setup files locally
Notes:
Git repo is https://github.com/Vivek-Rajani/customer_support_django/

Steps:
1. Extract the ZIP file
2. The folder called "comp314shortproject" should be placed into your Python directory. (C:\Users\Name\Documents\Python)
3. Open windows terminal and type: cd docume*\pyth*\comp314short*\cust* 
4. Next, start the virtual environemnt by typing: myenv\Scripts\activate.bat
5. Once done, you do: python manage.py makemigrations
6. Then: python manage.py migrate
7. To run the server at last, enter: python manage.py runserver
8. To stop the server, you can do Ctrl+C then "deactivate" to stop the virtual environment.

To do it with docker locally, skip steps 7 and 8 and do the following:
1. docker build -t cs_docker_app_img .
2. docker run -d -p 8000:8000 cs_docker_app_img

Then visit localhost:8000
If you did via runserver from earlier methods, you can go to 127.0.0.1:8000, it will be the same thing regardless.

A super user was created to view data and confirm it was working.
