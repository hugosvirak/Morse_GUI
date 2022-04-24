import tkinter
import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

blueLedPinId = 25
timeUnit = 0.1

GPIO.setup(blueLedPinId,GPIO.OUT)

win = tkinter.Tk()
win.title("SENTENCE TO MORSE CONTROLLER")
win.minsize(500, 500)

tkinter.Label(win, text="Message").grid(row=0)

maxLength = 12
def maxLengthValidate(P):
    if len(P) > maxLength:
        return False
    return True

vcmd = (win.register(maxLengthValidate), '%P')

entry = tkinter.Entry(win, validate="key", validatecommand=vcmd)
entry.grid(row=0, column=1)

def ledOn(duration):
    GPIO.output(blueLedPinId,GPIO.HIGH)
    time.sleep(duration)
    GPIO.output(blueLedPinId,GPIO.LOW)
    
def ledOutput(morseString):
    for c in morseString:
        if c == '.':
            ledOn(timeUnit)
        if c == '-':
            ledOn(timeUnit * 3)
        time.sleep(timeUnit)

def displayMorse():
    for c in entry.get():
        if c == 'a':
            ledOutput(".-")
        if c == 'b':
            ledOutput("-...");
        if c == 'c':
            ledOutput("-.-.");
        if c == 'd':
            ledOutput("-..");
        if c == 'e':
            ledOutput(".");
        if c == 'f':
            ledOutput("..-.");
        if c == 'g':
            ledOutput("--.");
        if c == 'h':
            ledOutput("....");
        if c == 'i':
            ledOutput("..");
        if c == 'j':
            ledOutput(".---");
        if c == 'k':
            ledOutput("-.-");
        if c == 'l':
            ledOutput(".-..");
        if c == 'm':
            ledOutput("--");
        if c == 'n':
            ledOutput("-.");
        if c == 'o':
            ledOutput("---");
        if c == 'p':
            ledOutput(".--.");
        if c == 'q':
            ledOutput("--.-");
        if c == 'r':
            ledOutput(".-.");
        if c == 's':
            ledOutput("...");
        if c == 't':
            ledOutput("-");
        if c == 'u':
            ledOutput("..-");
        if c == 'v':
            ledOutput("...-");
        if c == 'w':
            ledOutput(".--");
        if c == 'x':
            ledOutput("-..-");
        if c == 'y':
            ledOutput("-.--");
        if c == 'z':
            ledOutput("--..");
        if c == '0':
            ledOutput("-----");
        if c == '1':
            ledOutput(".----");
        if c == '2':
            ledOutput("..---");
        if c == '3':
            ledOutput("...--");
        if c == '4':
            ledOutput("....-");
        if c == '5':
            ledOutput(".....");
        if c == '6':
            ledOutput("-....");
        if c == '7':
            ledOutput("--...");
        if c == '8':
            ledOutput("---..");
        if c == '9':
            ledOutput("----.");
        if c == ' ':
            time.sleep(timeUnit * 7)
        else:
            time.sleep(timeUnit * 3)


tkinter.Button(win, text="Enter", command=displayMorse).grid(row=0, column=2)

def onQuit():
    GPIO.cleanup()
    win.destroy()

win.protocol("WM_DELETE_WINDOW", onQuit)
win.mainloop()
