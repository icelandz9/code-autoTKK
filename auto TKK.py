from tkinter import *
import time
from pyfirmata import Arduino
board = Arduino("COM10")

xServo = board.get_pin("d:7:s")
yServo = board.get_pin("d:8:s")
baseServo = board.get_pin("d:10:s")
handServo = board.get_pin("d:12:s")

print("READY!")

window = Tk()
window.geometry("500x500")
window.title("S-MAI @ Triamudomsuksapattanakarn Ratchada School")
window.resizable(0, 0)
window.pack_propagate(0)

xScale = IntVar()
yScale = IntVar()
baseScale = IntVar()
handScale = IntVar()

debugmode = True


def debug():
    valX = xScale.get()
    valY = yScale.get()
    valBase = baseScale.get()
    valHand = handScale.get()
    print(f'X: {valX}  |  Y: {valY}  |  B: {valBase}  |  H: {valHand}')


def xScaleHandler(_):
    val = xScale.get()
    xServo.write(val)
    if (debugmode):
        debug()


def yScaleHandler(_):
    val = yScale.get()
    yServo.write(val)
    if (debugmode):
        debug()


def baseScaleHandler(_):
    val = baseScale.get()
    baseServo.write(val)
    if (debugmode):
        debug()


def handScaleHandler(_):
    val = handScale.get()
    handServo.write(val)
    if (debugmode):
        debug()


def reset():
    xScale.set(0)
    yScale.set(0)
    baseScale.set(0)
    handScale.set(90)

    yServo.write(0)
    time.sleep(0.125)
    xServo.write(0)
    time.sleep(0.125)
    baseServo.write(0)
    handServo.write(90)


lastx = 0
lasty = 0
lastb = 0


def control(x, y, b, h, d, bx, by):
    global lastx, lasty, lastb
    if not bx:
        if (lastx <= x):
            for a in range(lastx, x, 1):
                xServo.write(a)
                time.sleep(0.00000000001)
        else:
            for a in range(lastx, x, -1):
                xServo.write(a)
                time.sleep(0.00000000001)
    else:
        xServo.write(x)
        # if (lastx <= x):
        #     for a in range(lastx, x, 1):
        #         xServo.write(a)
        #         time.sleep(0.00000000001)
        # else:
        #     for a in range(lastx, x, -1):
        #         xServo.write(a)
        #         time.sleep(0.00000000001)
    if not by:
        if (lasty <= y):
            for a in range(lasty, y, 1):
                yServo.write(a)
                time.sleep(0.00000000001)
        else:
            for a in range(lasty, y, -1):
                yServo.write(a)
                time.sleep(0.00000000001)
    else:
        yServo.write(y)
        # if (lasty <= y):
        #     for a in range(lasty, y, 1):
        #         yServo.write(a)
        #         time.sleep(0.00000000001)
        # else:
        #     for a in range(lasty, y, -1):
        #         yServo.write(a)
        #         time.sleep(0.00000000001)
    # if (lastb <= b):
    #     for a in range(lastb, b, 1):
    #         baseServo.write(a)
    #         time.sleep(0.00000000001)
    # else:
    #     for a in range(lastb, b, -1):
    #         baseServo.write(a)
    #         time.sleep(0.00000000001)

    # xScale.set(x)
    # yScale.set(y)
    # baseScale.set(b)
    # handScale.set(h)

    # xServo.write(x)
    # yServo.write(y)
    baseServo.write(b)
    handServo.write(h)
    time.sleep(d)

    lastx = x
    lasty = y
    lastb = b


def auto():
    # reset()

    control(0, 18, 74, 90, 0, False, False)
    # control(20, 19, 74, 90, 0,False, False)
    control(31, 18, 74, 90, 0, False, False)
    control(31, 18, 74, 0, 0.15, False, False)  # keep
    control(31, 60, 74, 0, 0, False, True)
    control(0, 60, 74, 0, 0, True, False)
    control(20, 60, 91  , 0, 0, False, False)
    control(20, 32, 91  , 0, 0, False, False)
    control(20, 32, 91  , 90, 0.15, False, False)  # drop
    control(0, 32, 91   , 90, 0, False, False)
    control(0, 30, 91   , 90, 0.15, False, False)

    control(0, 30, 57, 90, 0, False, False)
    control(0, 23, 57, 90, 0, False, False)
    # control(26, 23, 57, 90, 0,False, False)
    control(35, 23, 57, 90, 0, False, False)
    control(35, 23, 57, 0, 0.15, False, False)  # keep
    control(35, 80, 57, 0, 0, False, True)
    control(0, 80, 57, 0, 0, True, False)
    control(12, 80, 90, 0, 0, False, False)
    control(12, 48, 90, 0, 0, False, False)
    control(12, 48, 90, 90, 0.15, False, False)  # drop
    control(0, 48, 90, 90, 0, False, False)
    control(0, 30, 90, 90, 0.15, False, False)

    control(0, 30, 117, 90, 0,False, False)
    control(0, 19, 117, 90, 0,False, False)
    # control(20, 19, 117, 90, 0,False, False)
    control(30, 20, 117, 90, 0,False, False)
    control(30, 20, 117, 0, 0.15,False, False)  # keep
    control(30, 90, 117, 0, 0,False, True)
    control(0, 90, 117, 0, 0,True, False)
    control(11, 90, 91, 0, 0,False, False)
    control(11, 64, 91, 0, 0,False, False)
    control(11, 64, 91, 90, 0,False, False)  # drop
    control(11, 64, 91, 90, 0.15,False, False)
    control(0, 66, 91, 90, 0,True, False)
    control(0, 61, 91, 90, 0.1,False, True)
    control(0, 30, 91, 90, 0,False, True)

    reset()


Scale(showvalue=False, bd=0, activebackground="LIGHTBLUE", cursor="dot", highlightbackground="BLUE",
      troughcolor="WHITE", width=50, length=180, to=0, from_=90, variable=xScale, command=xScaleHandler).place(x=100, y=50)
Scale(showvalue=False, bd=0, activebackground="LIGHTBLUE", cursor="dot", highlightbackground="BLUE",
      troughcolor="WHITE", width=50, length=180, to=0, from_=90, variable=yScale, command=yScaleHandler).place(x=350, y=50)
Scale(showvalue=False, bd=0, activebackground="LIGHTBLUE", cursor="dot", orient=HORIZONTAL, highlightbackground="BLUE",
      troughcolor="WHITE", width=50, length=360, to=0, from_=180, variable=baseScale, command=baseScaleHandler).place(x=70, y=300)
Scale(showvalue=False, bd=0, activebackground="LIGHTBLUE", cursor="dot", orient=HORIZONTAL, highlightbackground="BLUE",
      troughcolor="WHITE", width=50, length=180, to=90, from_=0, variable=handScale, command=handScaleHandler).place(x=160, y=400)

Label(window, bd=0, text="FAR").place(x=115, y=30)
Label(window, bd=0, text="NEAR").place(x=110, y=235)
Label(window, bd=0, text="UP").place(x=367.5, y=30)
Label(window, bd=0, text="DOWN").place(x=357, y=235)
Label(window, bd=0, text="180").place(x=40, y=317.5)
Label(window, bd=0, text="0").place(x=445, y=317.5)
Label(window, bd=0, text="HOLD").place(x=120, y=417.5)
Label(window, bd=0, text="DROP").place(x=350, y=417.5)

Button(window, bd=0, bg="GREY", fg="WHITE", activebackground="RED", cursor="dot",
       text="RESET", width=10, height=5, command=reset).place(x=215, y=50)

Button(window, bd=0, bg="BLUE", fg="WHITE", activebackground="LIGHTBLUE",
       cursor="dot", text="AUTO", width=10, height=5, command=auto).place(x=215, y=150)

reset()
window.mainloop()
print("BYE!")
