/*
 * Arduino Server Code
 * Ver 04
 * Mojtaba Mansour Abadi 
 * OCRG
 * Northumbria University
 */


#define LED_PIN 9  // led pin number
#define BUF_LEN 10  // buffer length
#define INIT_DC 126  // initial duty cycle (126 = 50%)


float led_lux = INIT_DC ;  // led brightness
byte coeff = 0;  // led state

void setup() {
  // put your setup code here, to run once:
  
  Serial.begin(230400);
  
  pinMode(LED_PIN, OUTPUT);

  analogWrite(LED_PIN, 0);

  Serial.println(F("LabVIEW Demonstration:\nMessage format: L:x$\\n"));
}


void loop() {
  // put your main code here, to run repeatedly:

  char c;  // input message buffer

  delay(10);
  // send data only when you receive data:
  while (Serial.available() < 0);  
  // read the incoming byte:
  c = Serial.read();
  if(c != 'L') {
    return;
  }

  delay(10);
  // send data only when you receive data:
  while (Serial.available() < 0);  
  // read the incoming byte:
  c = Serial.read();
  if(c != ':') {
    return;
  }

  // look for the next valid integer in the incoming serial stream:
  delay(10);
  float ledLux = Serial.parseFloat();

  delay(10);
  // send data only when you receive data:
  while (Serial.available() < 0);  
  // read the incoming byte:
  c = Serial.read();
  if(c != '$') {
    return;
  }
  
  delay(10);
  // send data only when you receive data:
  while (Serial.available() < 0);  
  // read the incoming byte:
  c = Serial.read();
  if(c != '\n') {
    return;
  }
  
  Serial.print(F("LED DC = "));
  Serial.println(ledLux);    

  ledLux = int(constrain(ledLux, 0, 100) * 255.0/100.0);

  Serial.print(F("PWM DC value = "));
  Serial.println(ledLux);    

  analogWrite(LED_PIN, ledLux);
  
  Serial.println(F("----------------------"));
  
}
