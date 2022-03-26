int n = 0b0000;
int d0 = 5;
int d1 = 6;
int d2 = 7;
int d3 = 8;
bool clkEnable = true;
void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);
  pinMode(d0, OUTPUT);
  pinMode(d1, OUTPUT);
  pinMode(d2, OUTPUT);
  pinMode(d3, OUTPUT);
}

void loop() {
  // put your main code here, to run repeatedly:
  int clk = analogRead(A0);
  int reset = analogRead(A1);
  Serial.println(reset);
  Serial.println(n, BIN);
  if (reset < 50) {
    n = 0b0;
  }
  if ((clk > 650) && clkEnable) {
    n += 0b0001;
    clkEnable = false;
  }
  if (clk < 650) {
    clkEnable = true;
  }
  digitalWrite(d0, bitRead(n, 0));
  digitalWrite(d1, bitRead(n, 1));
  digitalWrite(d2, bitRead(n, 2));
  digitalWrite(d3, bitRead(n, 3));
  delay(5);
}
