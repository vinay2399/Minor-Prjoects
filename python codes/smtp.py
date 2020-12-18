import smtplib
s=smtplib.SMTP('smtp.gmail.com',587)
s.starttls()
print('server started')
username=input('Enter username : ')
passward=input('Enter passward  :')
s.login(username,passward)
print('logged in')
rec=input('Enter receipient : ')
msg=input('Type your message here : ')
s.sendmail(username,rec,msg)
print('mail sent successfully !!')
s.quit()
print('logged out !')


