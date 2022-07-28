import smtplib
sender_email = "uthmanqadri123213@gmail.com" #sending email
rec_email = "muhammadtai1292@hotmail.com" #recieving email
password = '42250Mm.'


subject = 'python test code'


message = "Testing my code"


msg = f'Subject: {subject}\n\n{message}'
server = smtplib.SMTP('smtp-mail.outlook.com', 587)
server.starttls()
server.login(sender_email,password)
print("works") #check if email opened
server.sendmail(sender_email, rec_email,msg)
print("email has worked") #check if email worked