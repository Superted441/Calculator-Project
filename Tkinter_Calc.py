from tkinter import *
#from numpy import *


root = Tk()


def basicbuttons(): # Basic Operations window
    Basic = Tk()


    def Quitb():
        Basic.destroy()

    global x
    x = 0
    global y
    y = 0
    global z
    z = 0
    global x1
    x1 = False
    global decimal
    decimal = False

    bf1 = Frame(Basic) # bf1 is for text
    bf2 = Frame(Basic) # other frames are for button placment
    bf3 = Frame(Basic)
    bf4 = Frame(Basic)
    bf5 = Frame(Basic)


    bf1.pack()
    bf2.pack()
    bf3.pack()
    bf4.pack()
    bf5.pack()

    global Textbox1
    Textbox1 = Text(bf1, height = 2, width = 24)
    Textbox1.insert(INSERT, "Please limit your sum to 2 numbers.")
    Textbox1.pack(side = LEFT)

    def clearTextInput():
        Textbox1.delete("1.0","end")

    def ONE():
        if x1: # if on num 1
            global y
            y = str(y)
            if decimal == False: #and not a decimal
                y.replace(".0", "") # remove the point to continue as whole number
            else:
                if d1 == True:
                    y.replace([-1], "") # remove the Zero
                    d1 = False
                else:
                    pass
            y = y + "1"
            y = float(y)
        else: # no2
            global x
            x = str(x)
            if decimal == False:
                x.replace(".0", "")
            else:
                pass
            x = x  + "1"
            x = float(x)
            clearTextInput()
            Textbox1.insert(INSERT, "{0} {1} {2}".format(x, z, y))
            Textbox1.pack()




    One = Button(bf4, text = "1", command = ONE, height = 2, width = 8)
    Two = Button(bf4, text = "2", command = apass, height = 2, width = 8)
    Three = Button(bf4, text = "3", command = apass, height = 2, width = 8)
    Four = Button(bf3, text = "4", command = apass, height = 2, width = 8)
    Five = Button(bf3, text = "5", command = apass, height = 2, width = 8)
    Six = Button(bf3, text = "6", command = apass, height = 2, width = 8)
    Seven = Button(bf2, text = "7", command = apass, height = 2, width = 8)
    Eight = Button(bf2, text = "8", command = apass, height = 2, width = 8)
    Nine = Button(bf2, text = "9", command = apass, height = 2, width = 8)
    Zero = Button(bf5, text = "0", command = apass, height = 2, width = 8)
    Times = Button(bf2, text = "X", command = apass, height = 2, width = 8)
    Divide = Button(bf3, text = "/", command = apass, height = 2, width = 8)
    Add = Button(bf4, text = "+", command = apass, height = 2, width = 8)
    Point = Button(bf5, text = ".", command = apass, height = 2, width = 8)
    Minus = Button(bf5, text = "-", command = apass, height = 2, width = 8)
    Equals = Button(bf5, text = "=", command = apass, height = 2, width = 8)
    GoBack = Button(bf1, text = "Go Back", command = Quitb, height = 2, width = 8)


    One.pack(side = LEFT)
    Two.pack(side = LEFT)
    Three.pack(side = LEFT)
    Four.pack(side = LEFT)
    Five.pack(side = LEFT)
    Six.pack(side = LEFT)
    Seven.pack(side = LEFT)
    Eight.pack(side = LEFT)
    Nine.pack(side = LEFT)
    Zero.pack(side = LEFT)
    Times.pack(side = LEFT)
    Divide.pack(side = LEFT)
    Add.pack(side = LEFT)
    Minus.pack(side = LEFT)
    Point.pack(side = LEFT)
    Equals.pack(side = LEFT)
    GoBack.pack(side = RIGHT)


    Basic.mainloop()

def ops():
    opschoice = Tk()


    def opsquit():
        opschoice.destroy()


    frameops = Frame(opschoice)
    frameops.pack()

    button2 = Button(frameops, text = "Buttons", command = basicbuttons, height = 3, width = 20)
    button3 = Button(frameops, text = "Go Back", command = opsquit, height = 3, width = 10)
    button1.pack(side = LEFT)
    button3.pack(side = LEFT)
    button2.pack(side = LEFT)

    opschoice.mainloop()


def Quitmainc(): # quit feature for quit button
    root.destroy()

def apass(): # empty func for testing buttons and other features
    pass

frame0 = Frame(root) # Frames to hold button positions
frame1 = Frame(root)
frame2 = Frame(root)


frame0.pack()
frame1.pack()
frame2.pack()

Textbox = Text(frame0, height = 1, state = NORMAL)
Textbox.insert(INSERT, "Welcome Please make a Choice") # welcoming text
Textbox.pack()


Choice1 = Button(frame1, text = "Basic Operations", command = ops, height = 3, width = 20) # buttons to access different features
Choice2 = Button(frame1, text = "X to the Power of Y", command = apass, height = 3, width = 20)
Choice3 = Button(frame1, text = "Circle Operations", command = apass, height = 3, width = 20)
Choice4 = Button(frame1, text = "The Square Root", command = apass, height = 3, width = 20)


Choice1.pack(side = LEFT)
Choice2.pack(side = LEFT)
Choice3.pack(side = LEFT)
Choice4.pack(side = LEFT)


Quitmain = Button(master = frame2, text = "Exit", command = Quitmainc, height = 2, width = 10) # quit button
Quitmain.pack()

root.mainloop()
