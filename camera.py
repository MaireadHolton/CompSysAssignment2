from sense_hat import SenseHat
from time import sleep
from picamera import PiCamera
import datetime
import smtplib
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart

sense = SenseHat()
camera = PiCamera()
frame = 1

# Send an email with an attachment using SMTP

def send_mail(eFrom, to, subject, text, attachment):
    # SMTP Server details
    smtpServer= 'smtp.mailgun.org'
    smtpUser='postmaster@sandbox7df3e5122abd43299ed70dcd4d221c0e.mailgun.org'
    smtpPassword='2bb84441a7b95f617042aa26c6bec454-48d7d97c-9e8944ac'
    port=587

    # open attachment and read in as MIME image
    fp = open(attachment, 'rb')
    msgImage = MIMEImage(fp.read())
    fp.close()

    #construct MIME Multipart email message
    msg = MIMEMultipart()
    msg.attach(MIMEText(text))
    msgImage['Content-Disposition'] = 'attachment; filename="image.jpg"'
    msg.attach(msgImage)
    msg['Subject'] = subject

    # Authenticate with SMTP server and send
    s = smtplib.SMTP(smtpServer, port)
    s.login(smtpUser, smtpPassword)
    s.sendmail(eFrom, to, msg.as_string())
    s.quit()

while True:
 acceleration = sense.get_accelerometer_raw()
 x = acceleration ['x']
 y = acceleration ['y']
 z = acceleration ['z']

 x = abs(x)
 y = abs(y)
 z = abs(z)

 if x > 1 or y > 1 or z > 1:
  camera.start_preview()
  fileLoc = f'/home/pi/Assignment/images/frame{frame}.jpg'
  currentTime = datetime.datetime.now().strftime("%H:%M:%S")

  camera.capture(fileLoc)
  text = f'Hi, \n the attached image was taken today at {currentTime}'
  send_mail('myPi@brewBuddy.ie', 'maireadholton@gmail.com', 'Fridge door event', text, fileLoc)
  print(f'frame {frame} taken at {currentTime}')
  frame += 1
 else:
  camera.stop_preview()
sleep (0.5)
