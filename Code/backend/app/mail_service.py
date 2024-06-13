from smtplib import SMTP #SMTP class is used to create a SMTP client
from email.mime.multipart import MIMEMultipart #sender email, recepient email #Multipart->msg will have multiple parts(to,subject,From,..) #mimetype declares the content type of  messages in email
from email.mime.text import MIMEText #only used to create the body of the mail  #mimetype declares the content type of  messages in email

SMTP_HOST="localhost" #because we are using mailhog
SMTP_PORT=1025
SENDER_EMAIL="22f3001138@ds.study.iitm.ac.in"
SENDER_PASSWORD=""




def send_message(to,subject,body):
	msg=MIMEMultipart() #msg is of type multipart
	msg['To']=to
	msg['From']=SENDER_EMAIL
	msg["Subject"]=subject
	
	msg_body=MIMEText(body,'html') #can be 'plain' as well
	msg.attach(msg_body)

	client=SMTP(host=SMTP_HOST,port=SMTP_PORT)
	client.send_message(msg=msg)  #send_message is a function from  smtplib
	client.close()

# send_message("kabirj2505@gmail.com",'test','<html>Test mail</html>')
	
