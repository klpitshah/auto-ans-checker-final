# -*- coding: utf-8 -*-

import smtplib
import sys

s = smtplib.SMTP('smtp.gmail.com', 587) 
s.starttls() 
s.login("daiict.exam.portal@gmail.com", "@daiictexamportal@")
print(str(sys.argv[1]))
print(str(sys.argv[2]))
SUBJECT = "Registration request"
text = "Welcome to the DAIICT Exam Portal \nUsername= " + str(sys.argv[1]) + "\nPassword= " + str(sys.argv[2]) + "\nBest of luck"
message = 'Subject: {}\n\n{}'.format(SUBJECT, text)
s.sendmail("sender_email_id", str(sys.argv[1]) + "@daiict.ac.in", message) 
s.quit() 

