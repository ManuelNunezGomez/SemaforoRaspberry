from gpiozero import LED
from time import sleep
verde1 = LED(22)
amarillo1 = LED(27)
rojo1 = LED(17)
verde2= LED(13)
amarillo2=LED(6)
rojo2 = LED(5)


def abre_1():
   verde2.off()
   amarillo2.on()
   sleep(1)
   amarillo2.off()
   rojo2.on()
   sleep(1)
   rojo1.off()
   verde1.on()
   rojo2.on()

def abre_2():
   verde1.off()
   amarillo1.on()
   sleep(1)
   amarillo1.off()
   rojo1.on()
   sleep(1)
   rojo2.off()
   verde2.on()

def lectura():
    f = open("/var/www/html/php_files/test.txt")
    letra = f.read(1)
    return letra
   
while True:
    if (lectura()=="1"):
       abre_1()
       while(lectura()=="1"):
           sleep(0.1)
    elif (lectura()=="2"):
       abre_2()
       while(lectura()=="2"):
           sleep(0.1)
       
    abre_1()
    
    if (lectura()=="1"):
       abre_1()
       while(lectura()=="1"):
           sleep(0.1)
    elif (lectura()=="2"):
       abre_2()
       while(lectura()=="2"):
           sleep(0.1)
           
    sleep(5)
    
    if (lectura()=="1"):
       abre_1()
       while(lectura()=="1"):
           sleep(0.11)
    elif (lectura()=="2"):
       abre_2()
       while(lectura()=="2"):
           sleep(0.1)
           
    abre_2()
    if (lectura()=="1"):
       abre_1()
       while(lectura()=="1"):
           sleep(0.11)
    elif (lectura()=="2"):
       abre_2()
       while(lectura()=="2"):
           sleep(0.1)
           
    sleep(5)