import smtplib

smtobj= smtplib.SMTP('smtp.gmail.com',587)
smtobj.ehlo()
smtobj.starttls()
smtobj.login('pragatideshmukh@gmail.com','My_email01')
smtobj.sendmail('pragatideshmukh@gmail.com','deshmukhpragati011@gmail.com','Subject: Smtp check. \n You are hacked!')
smtobj.quit()
