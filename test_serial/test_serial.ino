void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);
}

void loop() {
  // put your main code here, to run repeatedly:
  int i=0;
  for(i = 0; i < 10;i++){
    Serial.println(i);
  }
  String rng;
  String bpm;
  bpm = "%";
  rng = random(60,100);
  rng.concat(bpm);
  bpm.concat(rng);
  Serial.println(bpm);
}
