# CompSysAssignment2

Name: Mairead Holton
==============================
Student No. 20099850
==============================

# **BrewBuddy**

This is a simple IoT project to monitor the temperature and humidity inside a fermentation vessel (fridge). A SenseHat attached to a RaspberryPi is placed in the fridge, if the temperature falls outside of the optimum range an email is sent to the user, push notification is sent to their phone and a warning sound is played from a speaker via bluetooth. If the vesssel is opened a picture is sent to the user via email.

## **Structure**

2 python scripts have been written to proved the code for the RaspberryPi to monitor temperature and also to detect motion and send a picture via email.

*blynk.py* <br>
Contains code for importing and initializing blynk (line 1, line 16-18), also contains methods for blynk to run (line 50), write the temperature and humidity data to the blynk dashboard (line 57, line 66 and line 76) and log temperature excursion events to the dashboard (line 59 and line 68). This script also contains the code to display a pixelated image on the senseHat if the temperature is too high (line 63) or too low (line 72) and a code to call the aplay function to play a warning sound if there is a temperature excursion (line 61, line 70)

*camera.py* <br>
Conatins code for importing the picamera, smtp library and email functions. A function to send email via smtp using mailgun is contained in this script (line 16-39). An infinte while loop is used to read the acceleration from the sensehat (line 42- line 49), if the senseHat detects acceleration (line 51) it starts the camera (line 52) and takes a picture (line 56). The picture is then emailed from the images folder to the sender (line 58).


### **Elements used**

*Blynk IoT platform:* <br>
Used to create a dashboard to monitor temperature and humidity data and record any temperature excursion events. Also used to create a mobile app to monitor the temperature and humidity data and recieve push notifications from temperature excursions. Blynk is a cloud based platform used to connect all components together e.g. RaspberryPi, mobile device and dashboard. It uses WiFi and REST API to send a representation of the state of the resource (RaspberryPi with senseHat) to the requestor (dashboard, mobile device) using Python through virtual pins (v1 -temperature, v2 -humidity) to represent individual data streams. Uses the transport layer Transmission control protocol (TCP) to send messages from the device.

*Mailgun:* <br>
Email delivery service to allow pictures to be sent via email when the fermentation vessel is opened. the client SMTP connects to the server on port 587, once connected the client attempts to send the email, the server recieves the email and either forwards to another email server or stores the email until tje other email server is available. Uses the application layer protocol Simple Mail Transfer Protocol.

*Bluetooth:* <br>
Used to send a message from the raspberryPi to the bluetooth speaker. The raspberryPi is operating as a broadcaster/ server to send the warning.wav file to the speaker (which is acting as an observer/ client). THe bluetooth device adress is similar to a MAC address, has a6 byte number which was used to connect the raspberryPi to the speaker. Uses link layer protocol  GAP to broadcast device and GATT to establish a connection between the RaspberryPi and the bluetooth speaker 

#### **Sources**
[Blynk notifications]: https://community.blynk.cc/t/events-notifications-and-the-use-of-flag-variables/59822
[Blynk notifications]: https://github.com/blynkkk/lib-python
[Bluetooth speaker]: https://gist.github.com/actuino/9548329d1bba6663a63886067af5e4cb
