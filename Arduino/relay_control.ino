#define RELAY 8
#define BUZZER 9
#define LED 10

void setup() {
  pinMode(RELAY, OUTPUT);
  pinMode(BUZZER, OUTPUT);
  pinMode(LED, OUTPUT);
  Serial.begin(9600);
}

void loop() {
  if (Serial.available()) {
    String cmd = Serial.readStringUntil('\n');
    cmd.trim();
    if (cmd == "STOP") {
      digitalWrite(RELAY, LOW);
      digitalWrite(BUZZER, HIGH);
      digitalWrite(LED, HIGH);
    } else if (cmd == "START") {
      digitalWrite(RELAY, HIGH);
      digitalWrite(BUZZER, LOW);
      digitalWrite(LED, LOW);
    }
  }
}
