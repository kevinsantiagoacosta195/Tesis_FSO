int led=7;
int boton=11;
int valor;

void setup() {
  pinMode (led,OUTPUT);
  pinMode (boton,INPUT); 
}
void loop (){
  valor= digitalRead(boton);
  if(valor==1){
    digitalWrite (led,HIGH);
    delay (5000);
  }
  else {
    digitalWrite (led,LOW);
  }
}