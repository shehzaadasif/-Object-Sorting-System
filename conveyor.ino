const int s0 = A3;  
const int s1 = A4;  
const int s2 =A1;  
const int s3 = A2;  
const int out = A0;   
// values
int red = 0;  
int green = 0;  
int blue = 0;  

int m11=2;

int m12=3;





void setup()   
{  
  Serial.begin(9600); 
 
  pinMode(s0, OUTPUT);  
  pinMode(s1, OUTPUT);  
  pinMode(s2, OUTPUT);  
  pinMode(s3, OUTPUT);  
  pinMode(out, INPUT);

  pinMode(m11, INPUT);
  pinMode(m12, INPUT);
     
  
  digitalWrite(s0, HIGH);  
  digitalWrite(s1, HIGH);

  digitalWrite(m11,LOW);
  digitalWrite(m12,LOW);
} 
 
void loop() 
{  


  color();


  if (red < 100)
  {  
    Serial.print("R");
    delay(2000);
}  
else if (blue < red && blue < green)   
  {  
      if (red <=10 && green <=10 && blue <= 10){
      
  }else {
   Serial.print("B");
     delay(500);
   digitalWrite(m11,LOW);
  digitalWrite(m12,HIGH);
  delay(300
  );
  digitalWrite(m11,LOW);
  digitalWrite(m12,LOW);
  delay(3000);
  }
  }  
  else if (green < red && green < blue)  
  {  
    if (red <= 10 && green <=10 && blue <= 10){
      
  } else{
   Serial.print("G");
   delay(500);
     digitalWrite(m11,LOW);
  digitalWrite(m12,HIGH);
  delay(300);
   digitalWrite(m11,LOW);
  digitalWrite(m12,LOW); 
  delay(3000);
  } 
  }  

}
void color()  
{    
  digitalWrite(s2, LOW);
  digitalWrite(s3, LOW);  
  red = pulseIn(out, digitalRead(out) == HIGH ? LOW : HIGH);  
  digitalWrite(s3, HIGH);  
  blue = pulseIn(out, digitalRead(out) == HIGH ? LOW : HIGH);  
  digitalWrite(s2, HIGH);  
  green = pulseIn(out, digitalRead(out) == HIGH ? LOW : HIGH);  
}
 
