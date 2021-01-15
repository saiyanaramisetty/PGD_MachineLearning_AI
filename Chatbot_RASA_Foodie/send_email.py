import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

def send_email(top10_results, tracker, dispatcher):
    # Gmail ID created for Foodie Chatbot purpose
    sender_address = 'foodie.chatbot.communications@gmail.com'
    receiver_address = tracker.get_slot('email')
    sender_pass = 'upgrad123'

    message = MIMEMultipart()
    message['From'] = sender_address
    message['To'] = receiver_address
    message['Subject'] = 'Top restaurants from your search in Foodie'

    mail_content = top10_results
    message.attach(MIMEText(mail_content, 'plain'))

    session = smtplib.SMTP('smtp.gmail.com', 587)
    session.starttls()
    session.login(sender_address, sender_pass)
    text = message.as_string()
    session.sendmail(sender_address, receiver_address, text)
    session.quit()
