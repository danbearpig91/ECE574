import time
from gpiozero import MotionSensor
from twilio.rest import Client

#twilio account information for establishing connection
account_sid ="AC51be8274dac7bad1f416ecdc891e642b"
auth_token ="e6fe7bff36538969815bb89948286033"

#Initializes twilio client
client = Client(account_sid, auth_token)
#Initializes GPIO pin 4 to detect a signal change
sensor = MotionSensor(4)
#Waits for motion to be detected which then sends a text with a video stream link. Followed by a timeout for 30 minutes as to not receive to many texts.
while True:
	sensor.wait_for_motion()
	message = client.api.account.messages.create(to="+17347091859", 
						     from_="+19382539068", 
						     body="Motion Detected Please Check Phone App or visit proxy21.rt3.io:35701/stream/video.mjpeg")
	time.sleep(1800) 