# import the library 
import smtplib as smt
ob = smt.SMTP('smtp.gmail.com','587')
ob.ehlo()
ob.starttls()

# pass your email id and password
ob.login("Your email","pass")

# enter your subject title
subject = " test"

# enter your content
body = " Easily Done😄"
message = "subject : {}\n\n{}".format(subject,body)

# list of all the people whom you want to send mail
listadd=['all the ones you want to send']
ob.sendmail("Your email",listadd,message)
print("Mail sended")

# Done
ob.quit()

# Rest python will take care  
