import smtplib
from email.message import EmailMessage

email = EmailMessage()
email['from'] = 'Gokulakrishnan'
email['to'] = 'krishkrishnan0685@gmail.com'
email['subject'] = 'you won 1,000,000 dollars!'

email.set_content('I am a python Master!')

with smtplib.SMTP(host='smtp.gmail.com', port=587) as smtp:
    try:
        smtp.ehlo()
        smtp.starttls()
        smtp.login("gokulakrishnan21official@gmail.com", "strongpassword123@")
        smtp.send_message(email)
        print("all good!")

    except:
        print("disable the less secure option in your google settings")
