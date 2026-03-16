import processing.serial.*;

Serial arduino;

void setup() {
  size(400, 200);

  println(Serial.list());   // Mira el índice correcto
  arduino = new Serial(this, Serial.list()[0], 9600);
}

void draw() {
  background(30);
  fill(255);
  textSize(14);
  text("W : Up",     50, 50);
  text("S : Down",   50, 70);
  text("A : Left",   50, 90);
  text("D : Right",  50, 110);
  text("R : Center", 50, 130);
}

void keyPressed() {
  if (arduino != null) {
    arduino.write(key);
  }
}
