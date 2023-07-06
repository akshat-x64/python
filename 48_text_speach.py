import pyttsx3
engine = pyttsx3.init()

list_1 = ["Akshat","Ankit","Anmol","Pacholi"]
for li in list_1:
    engine.say(li)
    
engine.runAndWait()