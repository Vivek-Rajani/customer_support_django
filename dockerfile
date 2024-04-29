FROM python:3.12.3
WORKDIR /app/customer_support_project
COPY . /app/customer_support_project
RUN pip install -r requirements.txt
EXPOSE 8000
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]