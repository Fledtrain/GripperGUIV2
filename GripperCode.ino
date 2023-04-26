#include <Servo.h>
Servo ssm;
char buffer[3];
int angle = 0;
int current_angle = 0;  //Holds the most recent angle
int bufferIndex;
int ServoPos;
String value;


void setup() {
  // put your setup code here, to run once:
  ssm.attach(9);  //The number on board
  ssm.write(360);
  delay(2000);
  ssm.write(0);
  delay(2000);
  Serial.begin(9600);
  Serial.setTimeout(1);

  bufferIndex = 0;
}


void loop() {
  if (Serial.available() > 0) {
    delay(5);
    String command = Serial.readString();
    Serial.println(command);
    if (command[0] == 'o') {
      // Open the claw
      for (angle = 0; angle < 180; angle++) {
        ssm.write(angle);
        delay(1);
      }
      current_angle = 180;
    }
    else if (command[0] == 'c') {
      // Close the claw
      for (angle = 180; angle >= 0; angle--) {
        ssm.write(angle);
        delay(1);
      }
      current_angle = 0;
    }
    else{
        // Modify claw
        int int_command = command.toInt();
        if(int_command > 180 || int_command < 0){int_command = current_angle;}
        if (current_angle > int_command){   //Decrease to command
            for(current_angle; current_angle >= int_command; current_angle--){
                ssm.write(current_angle);
                delay(1);
            }
            current_angle = int_command;
        }
        else if (current_angle < int_command){  //Increase to command
            for(current_angle; current_angle <= int_command; current_angle++){
                ssm.write(current_angle);
                delay(1);
            }
            current_angle = int_command;
        }
    }
  }
}