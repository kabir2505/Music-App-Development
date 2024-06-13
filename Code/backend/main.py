from app.__init__ import create_app
from app.__init__ import db
from flask_security import hash_password
from werkzeug.security import generate_password_hash
from app.sec import datastore
import bcrypt
from app.worker import celery_init_app
from celery.schedules import crontab
from app.tasks import daily_reminder,monthly_reports
from app.models import Users
from app.instances import cache
version = bcrypt.__version__


#app,datastore=create_app()
app=create_app()
celery_app=celery_init_app(app)


@celery_app.on_after_configure.connect
def send_email(sender,**kwargs):
    
    
    sender.add_periodic_task(
        crontab(hour=6,minute=5),

        daily_reminder.s('''
Beep boop bop, music friend! Where you been? Your beats miss you!''')
    )

@celery_app.on_after_configure.connect
def send_report(sender,**kwargs):
    sender.add_periodic_task(
        crontab(hour=12,minute=1, day_of_month=1),
        monthly_reports.s('montly report')

    )




def upload_roles():
    from app.models import Users,Roles
    with app.app_context():
       db.create_all()
       datastore.find_or_create_role(name="admin",description="User is an admin")
       datastore.find_or_create_role(name="creator",description="user is an instructor")
       datastore.find_or_create_role(name="norm_user",description="user is a basic user")
       db.session.commit()
       if not datastore.find_user(email="admin@gmail.com"):
           datastore.create_user(email='admin@gmail.com',uname='admin',password=generate_password_hash("admin"),roles=["admin"])
           
       if not datastore.find_user(email="creator1@gmail.com"):
           datastore.create_user(email='creator1@gmail.com',uname='creator1',password=generate_password_hash("creator1"),roles=["creator"],active=True)
       if not datastore.find_user(email="norm_user1@gmail.com"):
           datastore.create_user(email='norm_user1@gmail.com',uname='norm_user1',password=generate_password_hash("norm_user1" ),roles=["norm_user"])
       if not datastore.find_user(email="norm_user2@gmail.com"):
           datastore.create_user(email='norm_user2@gmail.com',uname='norm_user2',password=generate_password_hash("norm_user2" ),roles=["norm_user"])
       db.session.commit()

upload_roles()









if __name__=='__main__':
    app.run(debug=True)