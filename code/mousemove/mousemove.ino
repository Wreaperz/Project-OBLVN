#include <Mouse.h> 

byte bf[2];

int dx;
int dy;

void setup() { 
  Mouse.begin(); 
  Serial.begin(1200); 
  Serial.setTimeout(1);
}
 
void moveMouse(int xDir, int yDir, int spd = 5) {
  Mouse.move(xDir, yDir, 0);
  delay(spd);
}

void loop() {
  dx = 0; 
  dy = 0;
  if (Serial.available() > 0) {
    Serial.readBytes(bf, 2);
    // Convert X values into MouseMove coords
    if (bf[0] > 128) {
      dx = bf[0] - 256;
    }
    else { dx = bf[0]; }

    // Convert Y values into MouseMove coords
    if (bf[1] > 128) {
      dy = bf[1] - 256;
    }
    else { dy = bf[1]; }

    moveMouse(dx, dy);
  }
   else { 
    moveMouse(0, 0);
  } 
}