# PyLED
A project for controlling an Arduino using Flask and pySerial.

## How to use
* Clone the repository somewhere on your filesystem
* (optional) create and activate a virtual invieroment

`$ virtualenv venv`\
`$ source venv/Scripts/activate`

* Install dependencies

`$ pip install -r requirements.txt`
* Run the app
`$ python app.py`
You should now be able to acces the interface from your browser at http://127.0.0.1:5000

### Arduino
To actually control the pins on the Arduino you need to upload the sketch in sketchLED/ to an arduino.
* Open sketchLED.ino with the Arduino IDE
* Upload the code to the Arduino board under Sketch>Upload(Ctrl+U)
* Note the number on the COM port under Tools>Port
* Correct the port number in LEDManager.py
