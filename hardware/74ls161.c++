int n = 0b0000;
int d0 = 6;
int d1 = 7;
int d2 = 8;
int d3 = 9;
int a0 = 2;
int a1 = 3;
int a2 = 4;
int a3 = 5;
int clkPin = 10;
int resetPin = 11;
int jumpPin = 12;
int incPin = A5;
bool clkEnable = true;
void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);
  pinMode(d0, OUTPUT);
  pinMode(d1, OUTPUT);
  pinMode(d2, OUTPUT);
  pinMode(d3, OUTPUT);
  pinMode(a0, INPUT);
  pinMode(a1, INPUT);
  pinMode(a2, INPUT);
  pinMode(a3, INPUT);
  pinMode(clkPin, INPUT);
  pinMode(resetPin, INPUT);
  pinMode(jumpPin, INPUT);
  pinMode(incPin, INPUT);

}

void loop() {
  // put your main code here, to run repeatedly:
  int clk = digitalRead(clkPin);
  int reset = digitalRead(resetPin);
  int jump = digitalRead(jumpPin);
  int inc = digitalRead(incPin);
  //Serial.print(clk);
  //Serial.println(reset);
  Serial.println(n, BIN);
  if (reset == 0) {
    n = 0b0;
  }
  if ((clk) && clkEnable && inc) {
    n += 0b0001;
    clkEnable = false;
  }
  if (!inc) {
    clkEnable = false;

  }
  if (jump == 0 && clk) {
    for (byte count = 0; count < 4; count++) {
      bitWrite(n, count, digitalRead((count + 1)));
    }
  }
  if (clk == 0 && inc) {
    clkEnable = true;
  }
  digitalWrite(d0, bitRead(n, 0));
  digitalWrite(d1, bitRead(n, 1));
  digitalWrite(d2, bitRead(n, 2));
  digitalWrite(d3, bitRead(n, 3));
  delay(1);
}
