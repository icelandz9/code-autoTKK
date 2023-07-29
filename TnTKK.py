from pyfirmata import Arduino
import time
board = Arduino("COM7")

Servo1 = board.get_pin("d:8:s")
Servo2 = board.get_pin("d:9:s")
Servo3 = board.get_pin("d:10:s")    
Servo4 = board.get_pin("d:12:s")

global s1
global s2
global s3
global s4

time.sleep(0.5)
print("RUN OK")

from tkinter import*
window = Tk()
window.geometry("500x500")
window.title("Robot_arm")

def reset():
    Servo1.write(0)
    Servo2.write(0)
    Servo3.write(0)
    Servo4.write(0)

def servo1_worker(vul):
    global scale_value1
    scale_value1 =s1.get()
    Servo1.write(scale_value1)
    
def servo2_worker(vul):
    global scale_value2
    scale_value2 =s2.get()
    Servo2.write(scale_value2)

def servo3_worker(vul):
    global scale_value3
    scale_value3 =s3.get()
    Servo3.write(scale_value3)

def servo4_worker(vul):
    global scale_value4
    scale_value4 =s4.get()
    Servo4.write(scale_value4)   



label1 = Label(window, text="Up-down", font=1000).place(x=85,y=45)
label2 = Label(window, text="ใกล้-ไกล", font=1000).place(x=85,y=90)
label3 = Label(window, text="Base", font=1000).place(x=85,y=135)
label4 = Label(window, text="handle", font=1000).place(x=85,y=185)

B1 = Button(window,text="reset", command=reset)
B1.pack()

s1 = Scale(window, from_=0, to=90, width=20, length=180, orient=HORIZONTAL, command=servo1_worker)
s1.pack()

s2 = Scale(window, from_=0, to=70, width=20, length=180, orient=HORIZONTAL, command=servo2_worker)
s2.pack()

s3 = Scale(window, from_=0, to=180, width=20, length=180, orient=HORIZONTAL, command=servo3_worker)
s3.pack()

s4 = Scale(window, from_=0, to=90, width=20, length=180, orient=HORIZONTAL, command=servo4_worker)
s4.pack()

reset()

window.mainloop()   	