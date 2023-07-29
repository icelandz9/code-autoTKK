from pyfirmata import Arduino
board = Arduino("COM7")

xServo = board.get_pin("d:7:s")
yServo = board.get_pin("d:9:s")
baseServo = board.get_pin("d:10:s") hd
handServo = board.get_pin("d:12:s")

print("RUN OK")

import time
from tkinter import *
window = Tk()
window.geometry("500x500")
window.title("Robot_arm")
window.resizable(0, 0)
window.pack_propagate(0)

xScale = IntVar()
yScale = IntVar()
baseScale = IntVar()
handScale = IntVar()


def xScaleHandler(_):
    val = xScale.get()
    xServo.write(val)


def yScaleHandler(_):
    val = yScale.get()
    yServo.write(val)


def baseScaleHandler(_):
    val = baseScale.get()
    baseServo.write(val)


def handScaleHandler(_):
    val = handScale.get()
    handServo.write(val)

def clear():
    xScale.set(0)   
    yScale.set(0)
    baseScale.set(0)
    handScale.set(90)
    yServo.write(0)
    time.sleep(0.5)
    xServo.write(0)
    time.sleep(0.5)
    baseServo.write(0)
    handServo.write(90)
    
Scale(showvalue=False, bd=0, activebackground="LIGHTGREEN", cursor="dot",
      highlightbackground="GREEN", troughcolor="WHITE", width=50, length=180, to=0, from_=90, variable=xScale, command=xScaleHandler).place(x=100, y=50)
Scale(showvalue=False, bd=0, activebackground="LIGHTGREEN", cursor="dot",
      highlightbackground="GREEN", troughcolor="WHITE", width=50, length=180, to=0, from_=90, variable=yScale, command=yScaleHandler).place(x=350, y=50)
Scale(showvalue=False, bd=0, activebackground="LIGHTGREEN", cursor="dot", orient=HORIZONTAL,
      highlightbackground="GREEN", troughcolor="WHITE", width=50, length=360, to=0, from_=180, variable=baseScale, command=baseScaleHandler).place(x=70, y=300)
Scale(showvalue=False, bd=0, activebackground="LIGHTGREEN", cursor="dot", orient=HORIZONTAL,
      highlightbackground="GREEN", troughcolor="WHITE", width=50, length=180, to=90, from_=0, variable=handScale, command=handScaleHandler).place(x=160, y=400)

Label(bd=0, text="FAR").place(x=115, y=30)
Label(bd=0, text="SHORT").place(x=107.5, y=235)
Label(bd=0, text="UP").place(x=367.5, y=30)
Label(bd=0, text="DOWN").place(x=357.5, y=235)
Label(bd=0, text="180").place(x=40, y=317.5)
Label(bd=0, text="0").place(x=445, y=317.5)
Label(bd=0, text="HOLD").place(x=120, y=417.5)
Label(bd=0, text="DROP").place(x=350, y=417.5)

Button(bd=0, bg="GREEN", activebackground="RED", cursor="dot",
       text="CLEAR", width=10, height=5,command=clear).pack(anchor=CENTER)

clear()
window.mainloop()