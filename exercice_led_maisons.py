import network   #import des fonction lier au wifi
import urequests   #import des fonction lier au requetes http
import utime   #import des fonction lier au temps
import ujson   #import des fonction lier aà la convertion en Json
from machine import Pin, PWM

wlan = network.WLAN(network.STA_IF) # met la raspi en mode client wifi
wlan.active(True) # active le mode client wifi

ssid = 'iPhone de Corentin'
password = 'classiquement'
wlan.connect(ssid, password) # connecte la raspi au réseau
url = "http://172.20.10.10:3000/iot/iot"

houses = { "Gryffindor": [10000, 0, 0],
           "Slytherin": [0, 10000, 0],
           "Ravenclaw": [0, 0, 10000],
           "Hufflepuff": [10000, 10000, 0]
            }
 
pwm_ledR = PWM(Pin(14,mode=Pin.OUT))
pwm_ledR.freq(1_000)
pwm_ledG = PWM(Pin(13,mode=Pin.OUT))
pwm_ledG.freq(1_000)
pwm_ledB = PWM(Pin(12,mode=Pin.OUT))
pwm_ledB.freq(1_000)

while not wlan.isconnected():
    print("pas co")
    utime.sleep(1)
    pass

while(True):
    try:
        print("GET")
        r = urequests.get(url) # lance une requete sur l'url
        print(r.json()["Iot"])
        
        house=r.json()["Iot"]
        pwm_ledR.duty_u16(houses[house][0])
        pwm_ledG.duty_u16(houses[house][1])
        pwm_ledB.duty_u16(houses[house][2])
        
        r.close() # ferme la demande
        utime.sleep(1)  
    except Exception as e:
        print(e)