import smtplib          # SMTPLib stands for =  Simple Mail Transfer Protocol Library

sender = "uzair.kayani555@gmail.com"
receiver = "uzair_kayani555@yahoo.com"
password = "52455269543115"
subject = "Python email test"
body = "Hey, this is a test email using python protocols"

# header
message = f"""From: Snoop Dogg {sender}
To: Nicholas Cage{receiver}
Subject: {subject}\n
{body}
"""

server = smtplib.SMTP("smtp.gmail.com",587)
server.starttls()
try:
    server.login(sender,password)
    print("Logged in...")
    server.sendmail(sender,reciever,message)
    print("Email has been sent!")

except smtplib.SMTPAuthenticationError:
    print("unable to sign in")

