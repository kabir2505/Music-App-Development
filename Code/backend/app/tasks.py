from celery import shared_task
from .mail_service import send_message
from .models import Users,Roles,Songs,Albums
from datetime import datetime,timedelta
import json
from jinja2 import Template
import os
from sqlalchemy import func
from app.__init__ import db


#ignore result False to store the result into the result backend
@shared_task(ignore_result=False)
def say_hello():
    users = Users.query.all()
    current_time = datetime.now()
    a = []
    for user in users:
        time_difference = current_time - user.last_login
        if time_difference > timedelta(hours=12):
            a.append(str(time_difference))  # Convert timedelta to string
    return json.dumps(a)
@shared_task(ignore_result=False)
def add(a,b):
    return a+b



@shared_task(ignore_result=True)
def daily_reminder(text):
    current_time = datetime.now()
    users=Users.query.all()
    for user in users:
        if user.email:
            time_difference = current_time - user.last_login
            if time_difference > timedelta(hours=12):
                send_message(user.email,'reminder',text)
    return 'Ok'



template_folder=os.path.join(os.getcwd(),'mail_templates')
@shared_task(ignore_result=True)
def monthly_reports(subject):
    users=Users.query.filter(Users.roles.any(Roles.name=="creator"))
    for user in users:
        with open(os.path.join(template_folder,"welcome.html"),'r') as f:
             template=Template(f.read())
             avg_rating = db.session.query(func.avg(Songs.ratings)).filter(Songs.creator_id ==user.uid).scalar()
             if avg_rating:
                avg_rating = round(avg_rating, 1)
             
             send_message(user.email,subject,body=template.render(user=user,songs=user.songs,albums=user.albums,avg_rating=avg_rating))


      
         
