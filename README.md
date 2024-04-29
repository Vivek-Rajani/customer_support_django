# How to setup files locally
Note: Git repo is: https://github.com/Vivek-Rajani/customer_support_django/
Steps:
1. Extract the ZIP file to your desktop.
2. Drag the file inside the ZIP into your Python Directory (C://Users/Student/Documents/Python)
3. Open windows terminal and type: cd doc*\py*\comp314short*\customer*
4. Next, start the virtual environemnt by typing: myenv\Scripts\activate.bat
5. Once done, you do: python manage.py runserver.

To do it with docker locally, you do:
1. docker build -t cs_docker_app_img .
2. docker run -d -p 8000:8000 cs_docker_app_img

Then visit localhost:8000
If you did via runserver from bat, you can go to 127.0.0.1:8000, it will be the same thing regardless.

A super user was created to view data and confirm it was working.
