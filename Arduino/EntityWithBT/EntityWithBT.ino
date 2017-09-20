#include <ArduinoJson.h>
#include <SoftwareSerial.h>

int bluetoothTx = 5;
int bluetoothRx = 6;

const int ledPin1 =  13;
const int ledPin2 =  12;
const int ledPin3 =  11;

SoftwareSerial bluetooth(bluetoothTx, bluetoothRx);

void setup()
{
  Serial.begin(9600);//시리얼 통신 초기화
  bluetooth.begin(9600);//블루투스 통신 초기화
  pinMode(ledPin1, OUTPUT);  
  pinMode(ledPin2, OUTPUT);  
  pinMode(ledPin3, OUTPUT);  
  Serial.println("hi");
}
 
 
void loop()
{ 
  handle();
}

void handle(){
  char response[128]={'\0'};
  int i = 0;
  while(!bluetooth.available());
  
  while(bluetooth.available()){
    delay(10);
    response[i] = bluetooth.read();
    i++;
  }
  /*
   * sample JSON : { "led" : 1, "time" : 1000 }
   * 1번 led를 1초 동안 켠다.
   */
  Serial.println(response);
  String result(response);
  StaticJsonBuffer<200> jsonBuffer;
  JsonObject& root = jsonBuffer.parseObject(result);
  int led = root["led"];
  int time = root["time"];
  if (led == 1) {
    digitalWrite (ledPin1, HIGH);
    delay(time);
    digitalWrite (ledPin1, LOW);
  } else if (led == 2) {
    digitalWrite (ledPin2, HIGH);
    delay(time);
    digitalWrite (ledPin2, LOW);    
  } else if (led == 3) {
    digitalWrite (ledPin3, HIGH);
    delay(time);
    digitalWrite (ledPin3, LOW);    
  }
}

