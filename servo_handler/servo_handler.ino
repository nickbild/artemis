#include <Servo.h>

Servo servo1;
Servo servo2;

int pos1 = 90;
int pos2 = 90;

int in1 = 10;
int in2 = 12;
int select_servo = A0;

int in1_active = 1;
int in2_active = 1;

void setup() {
  servo1.attach(9);
  servo2.attach(7);

  pinMode(in1, INPUT);
  pinMode(in2, INPUT);
  pinMode(select_servo, INPUT); // LOW = servo1, HIGH = servo2

  servo1.write(pos1);
  servo2.write(pos2);
}

void loop() {
  ////
  // Modify servo position the first time a high signal is seen on an input.
  ////
  
  if (digitalRead(in1) == HIGH && in1_active) {
    if (digitalRead(select_servo) == LOW) {
      pos1 += 1;
    } else {
      pos2 += 1;
    }
    
    in1_active = 0;
  }
  if (digitalRead(in2) == HIGH && in2_active) {
    if (digitalRead(select_servo) == LOW) {
      pos1 -= 1;
    } else {
      pos2 -= 1;
    }
    
    in2_active = 0;
  }

  ////
  // Adjust servo position.
  ////

  if (pos1 > 180) { pos1 = 180; }
  if (pos2 > 180) { pos2 = 180; }
  if (pos1 < 0) { pos1 = 0; }
  if (pos2 < 0) { pos2 = 0; }

  if (digitalRead(select_servo) == LOW) {
    servo1.write(pos1);
  } else {
    servo2.write(pos2);
  }

  ////
  // When an input goes LOW, reactivate it so it can trigger on the next HIGH signal.
  ////
  
  if (digitalRead(in1) == LOW) {
    in1_active = 1;
  }
  if (digitalRead(in2) == LOW) {
    in2_active = 1;
  }

}
