// Cardiac Pulse Monitor Bip TM
 
#define USE_ARDUINO_INTERRUPTS true

volatile int pulsePin = 1;                   // Sensor is connected in the pin A0
// These variables are volatile beacause they're used in Interupt.ino
volatile int BPM;                   // Beats per minute
volatile int Signal;                // Sensor data entry 
volatile int IBI = 600;             // Time between pulses
volatile boolean Pulse = false;     // True when the pulse wave is high, false when is low
volatile boolean QS = false;        // Quantified Self is true when the Arduino search a heart pulse
int Threshold = 550;
float seno;
int frequencia;
unsigned long tempo;

void setup()
{                    
 Serial.begin(9600);                // Starts the serial Monitor
 pinMode(10,OUTPUT);
 pinMode(6,OUTPUT);
 interruptSetup();                  // Activate the BPM reading function  
}

void loop()
{
 int pulso = analogRead(A1);        //Read the value from the sensor in Analog A0
 String charac;
  charac = "%";
  String str_BPM;
  str_BPM = BPM;
  str_BPM.concat(charac);
  charac.concat(str_BPM);
 Serial.println(charac);
  Serial.println(pulso);
if(40 < BPM && BPM < 80)
{
alarme();
}
else
{
analogWrite(6,0);
digitalWrite(10,LOW);
}

  if (QS == true){                  // Quantified Self is true when the Arduino search a heart pulse
    QS = false;                     // Reseting Quantified Self 
  }

}


void alarme()
{
 digitalWrite(10,HIGH);
 for(int x=0;x<180;x++)
{
 
  seno=(sin(x*3.1416/180));
  frequencia = 2000+(int(seno*1000));
  analogWrite(6,frequencia);  
}
}
