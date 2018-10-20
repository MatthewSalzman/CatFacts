import smtplib

from string import Template

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from celery.decorators import task
from celery import shared_task

from core.models import Fact, Email, Header, Footer


MY_ADDRESS = 'MrFactCat@gmail.com'
PASSWORD = 'catfacts!'




@shared_task
def send_email(subject, header, fact, footer, email):
    #message_template = read_template('message.txt')

    # set up the SMTP server
    s = smtplib.SMTP(host='smtp.gmail.com', port=587)
    s.starttls()
    s.login(MY_ADDRESS, PASSWORD)

    # For each contact, send the email:
    # email = 'salzmamj@mail.uc.edu'

    msg = MIMEMultipart()       # create a message

    # add in the actual person name to the message template
    message = header +":\n\n"
    message += fact + "\n\n"
    message += "Sincerely,\nThe Fact Cat"
    
    # Prints out the message body for our sake
    print(message)

    # setup the parameters of the messa
    msg['From']=MY_ADDRESS
    msg['To']=email
    msg['Subject']=subject
        
    # add in the message body
    msg.attach(MIMEText(message, 'plain'))
        
    # send the message via the server set up earlier.
    s.send_message(msg)
    del msg
        
    # Terminate the SMTP session and close the connection
    s.quit()
    
    
    
# header = "Its Friday, check out this fact"
# fact = "Cats have been domesticated for around 4,000 years. While they were once valued for their hunting abilities, they are now valued for their companionship and loving behaviour."
# footer = "Sincerly,\nMr. Fact Cat"
# send_email(header, fact, footer)
def send_email_to_all_users():
    subject = "Check out this fact"
    users = Email.objects.all()

    fact = Fact.objects.order_by('?').first()
    header = Header.objects.order_by('?').first()
    footer = Footer.objects.order_by('?').first()

    for user in users:
        send_email.delay(subject, header.header, fact.fact, footer.footer, user.email_address)




# send_email('catfact! now','Check this out','Did you know, facts are awesome!','Thanks!','salzmamj@mail.uc.edu')