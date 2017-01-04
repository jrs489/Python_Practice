#!/usr/bin/env python
# -*- coding: utf-8 -*-

# A program for turning text into morse code
# Limits: I'm not allowed to google "morse" and "python" at the same time.

# Load the libraries I need
import RPi.GPIO as GPIO
import time


# This is my morse code dictionary


#mymorsedict2 = pd.read_excel("C:/Users/John Shults/Documents/jshults/Learning/1400_Data_Management_and_Analysis/Python/morse_dictionary_3.xlsx", sheetname = "morse_dictionary", header = 0)
#mymorsedict2 = pd.read_csv("C:/Users/John Shults/Documents/jshults/Learning/1400_Data_Management_and_Analysis/Python/morse_dictionary_3.csv", header = 0, error_bad_lines = False)
#print(mymorsedict2)

mymorsedict3 = {
"A":".-",
"B":"-…",
"C":"-.-.",
"D":"-..",
"E":".",
"F":"..-.",
"G":"--.",
"H":"….",
"I":"..",
"J":".---",
"K":"-.-",
"L":".-..",
"M":"--",
"N":"-.",
"O":"---",
"P":".--.",
"Q":"--.-",
"R":".-.",
"S":"…",
"T":"-",
"U":"..-",
"V":"…-",
"W":".--",
"X":"-..-",
"Y":"-.--",
"Z":"--..",
" ":"_",
"1":".----",
"2":"..---",
"3":"…--",
"4":"….-",
"5":"…..",
"6":"-….",
"7":"--…",
"8":"---..",
"9":"----.",
"0":"-----",
",":"--..--",
".":".-.-.-",
"?":"..--..",
";":"-.-.-",
":":"---…",
"-":"-..-.",
"(":"-.--.",
")":"-.--.-",
"_":"..--.-",
"@":".--.-.",
"!":"-.-.--",
"&":".-…",
"+":".-.-.",
"$":"…-..-",
"'":""
}

# This is my input for text
mytext = input("type a message >")


# This is my code to convert the text to morse code.
mytext = mytext.upper()
myletters = list(mytext)
#print(myletters)
#mymorse = [mymorsedict3[x] for x in myletters]
#print(mymorse)
mymorse = [mymorsedict3[x] for x in myletters]
#print(mymorse)

#mymorsestring = "".join(mymorse)
#print(mymorsestring)


# This is my code for communicating my morse message via a blinking LED
Led = 11 # I'm using GPIO pin 11 for my Led
#dotlength = 0.25

def setup():
    GPIO.setmode(GPIO.BOARD) #Number according to the physical location
    GPIO.setup(Led, GPIO.OUT) # Set pin mode as output
    GPIO.output(Led, GPIO.HIGH) # Output high level

def communicate(message):
    for x in message:
        print(x)
        character = list(x)
        for y in character:
            print(y)
            if y == ".":
                GPIO.output(Led, GPIO.LOW) #Led dot
                time.sleep(0.15)
                GPIO.output(Led, GPIO.HIGH) #Led off
                time.sleep(0.45)
            elif y == "-":
                GPIO.output(Led, GPIO.LOW) #Led dash
                time.sleep(0.45)
                GPIO.output(Led, GPIO.HIGH) #Led off
                time.sleep(0.45)
            elif y == "_":
                time.sleep(1.45)
            else:
                time.sleep(0.01)

def destroy():
    GPIO.output(Led, GPIO.HIGH)
    GPIO.cleanup()


setup()
communicate(mymorse)
time.sleep(3.0)
communicate(mymorse)
time.sleep(3.0)
communicate(mymorse)
destroy()
