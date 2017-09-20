from flask import Flask
    app = Flask(__name__)   #플라스크 호출
 
@app.route("/gpio.html") # 주소가 index.php 이면 index.php페이지 호출
def indexPage():
    return "gpio.html"
     
if __name__ == "__main__":
    app.run(host'0.0.0.0', port=80, debug=True) #서버동작
def turn_led_onoff(action):
	if (action == "on"):                #LED ON
		GPIO.output(ledPin, GPIO.HIGH)
	if (action == "off"):               #LED OFF
		GPIO.output(ledPin, GPIO.LOW)
	if (action == "toggle"):            #껏다켯다 한버튼으로 동작
		state = not GPIO.input(ledPin)
		GPIO.output(ledPin, state)
	return (''), 204 #204는 왜하는지 잘 모르겠음
