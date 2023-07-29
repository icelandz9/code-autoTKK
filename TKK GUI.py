from pyfirmata import Arduino
import time
board = Arduino("COM6")

Servo1 = board.get_pin("d:7:s")
Servo2 = board.get_pin("d:9:s")                                                                                                                              
Servo3 = board.get_pin("d:10:s")    
Servo4 = board.get_pin("d:12:s")
Servo1.write(0)
Servo2.write(0)
Servo3.write(0)
Servo4.write(0)

global s1
global s2
global s3
global s4

time.sleep(0.5)
print("RUN OK")

from tkinter import*
window = Tk()   
window.geometry("500x700")
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

# label1 = Label(window, text="Up-down", font=1000).place(x=85,y=45)
# label2 = Label(window, text="ใกล้-ไกล", font=1000).place(x=85,y=90)
# label3 = Label(window, text="Base", font=1000).place(x=85,y=135)
# label4 = Label(window, text="handle", font=1000).place(x=85,y=185)

B1 = Button(window,text="reset", command=reset)
B1.pack()

s1 = Scale(window, from_=90, to=0, width=20, length=180, orient=VERTICAL, command=servo1_worker,label="ขึ้นลง",font=1000)
s1.pack(anchor="ne")

s2 = Scale(window, from_=90, to=0 , width=20, length=180, orient=VERTICAL, command=servo2_worker,label="ใกล้ไกล",font=1000)
s2.pack(anchor="nw",side="top")

s3 = Scale(window, from_=180, to=0, width=20, length=180, orient=HORIZONTAL, command=servo3_worker,label="ฐาน",font=1000)
s3.pack(anchor="center")

s4 = Scale(window, from_=0, to=90, width=20, length=180, orient=HORIZONTAL, command=servo4_worker,label="คีบ",font=1000)
s4.pack()
reset()
window.mainloop()   	 