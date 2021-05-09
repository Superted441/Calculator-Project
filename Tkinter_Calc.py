from tkinter import *
#from numpy import *



root = Tk()


def basicbuttons(): # Basic Operations window
    Basic = Tk()


    def Quitb():
        Basic.destroy()
        basicbuttons()

    global x
    x = 0
    global y
    y = 0
    global z
    z = 0
    global x1
    x1 = True
    global decimal
    decimal = False
    global d1
    d1 = False

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
        global d1
        if x1: # if on num 1
            global y
            y = str(y)
            if decimal == False: #and not a decimal
                y = y.replace(".0", "") # remove the point to continue as whole number
            else:

                if d1 == True:
                    y = y.replace(".0", ".") # remove the Zero
                    d1 = False
                else:
                    pass
            y = y + "1"
            y = float(y)
        else: # no2
            global x
            x = str(x)
            if decimal == False: #and not a decimal
                x = x.replace(".0", "") # remove the point to continue as whole number
            else:

                if d1 == True:
                    x = x.replace(".0", ".") # remove the Zero
                    d1 = False
                else:
                    pass
            x = x  + "1"
            x = float(x)
        clearTextInput()
        Textbox1.insert(INSERT, "{0} {2} {1}".format(y, x, z))
        Textbox1.pack()


    def TWO():
        global d1
        if x1: # if on num 1
            global y
            y = str(y)
            if decimal == False: #and not a decimal
                y = y.replace(".0", "") # remove the point to continue as whole number
            else:

                if d1 == True:
                    y = y.replace(".0", ".") # remove the Zero
                    d1 = False
                else:
                    pass
            y = y + "2"
            y = float(y)
        else: # no2
            global x
            x = str(x)
            if decimal == False: #and not a decimal
                x = x.replace(".0", "") # remove the point to continue as whole number
            else:

                if d1 == True:
                    x = x.replace(".0", ".") # remove the Zero
                    d1 = False
                else:
                    pass
            x = x  + "2"
            x = float(x)
        clearTextInput()
        Textbox1.insert(INSERT, "{0} {2} {1}".format(y, x, z))
        Textbox1.pack()


    def THREE():
        global d1
        if x1: # if on num 1
            global y
            y = str(y)
            if decimal == False: #and not a decimal
                y = y.replace(".0", "") # remove the point to continue as whole number
            else:

                if d1 == True:
                    y = y.replace(".0", ".") # remove the Zero
                    d1 = False
                else:
                    pass
            y = y + "3"
            y = float(y)
        else: # no2
            global x
            x = str(x)
            if decimal == False: #and not a decimal
                x = x.replace(".0", "") # remove the point to continue as whole number
            else:

                if d1 == True:
                    x = x.replace(".0", ".") # remove the Zero
                    d1 = False
                else:
                    pass
            x = x  + "3"
            x = float(x)
        clearTextInput()
        Textbox1.insert(INSERT, "{0} {2} {1}".format(y, x, z))
        Textbox1.pack()


    def FOUR():
        global d1
        if x1: # if on num 1
            global y
            y = str(y)
            if decimal == False: #and not a decimal
                y = y.replace(".0", "") # remove the point to continue as whole number
            else:

                if d1 == True:
                    y = y.replace(".0", ".") # remove the Zero
                    d1 = False
                else:
                    pass
            y = y + "4"
            y = float(y)
        else: # no2
            global x
            x = str(x)
            if decimal == False: #and not a decimal
                x = x.replace(".0", "") # remove the point to continue as whole number
            else:

                if d1 == True:
                    x = x.replace(".0", ".") # remove the Zero
                    d1 = False
                else:
                    pass
            x = x  + "4"
            x = float(x)
        clearTextInput()
        Textbox1.insert(INSERT, "{0} {2} {1}".format(y, x, z))
        Textbox1.pack()


    def FIVE():
        global d1
        if x1: # if on num 1
            global y
            y = str(y)
            if decimal == False: #and not a decimal
                y = y.replace(".0", "") # remove the point to continue as whole number
            else:

                if d1 == True:
                    y = y.replace(".0", ".") # remove the Zero
                    d1 = False
                else:
                    pass
            y = y + "5"
            y = float(y)
        else: # no2
            global x
            x = str(x)
            if decimal == False: #and not a decimal
                x = x.replace(".0", "") # remove the point to continue as whole number
            else:

                if d1 == True:
                    x = x.replace(".0", ".") # remove the Zero
                    d1 = False
                else:
                    pass
            x = x  + "5"
            x = float(x)
        clearTextInput()
        Textbox1.insert(INSERT, "{0} {2} {1}".format(y, x, z))
        Textbox1.pack()


    def SIX():
        global d1
        if x1: # if on num 1
            global y
            y = str(y)
            if decimal == False: #and not a decimal
                y = y.replace(".0", "") # remove the point to continue as whole number
            else:

                if d1 == True:
                    y = y.replace(".0", ".") # remove the Zero
                    d1 = False
                else:
                    pass
            y = y + "6"
            y = float(y)
        else: # no2
            global x
            x = str(x)
            if decimal == False: #and not a decimal
                x = x.replace(".0", "") # remove the point to continue as whole number
            else:

                if d1 == True:
                    x = x.replace(".0", ".") # remove the Zero
                    d1 = False
                else:
                    pass
            x = x  + "6"
            x = float(x)
        clearTextInput()
        Textbox1.insert(INSERT, "{0} {2} {1}".format(y, x, z))
        Textbox1.pack()

    def SEVEN():
        global d1
        if x1: # if on num 1
            global y
            y = str(y)
            if decimal == False: #and not a decimal
                y = y.replace(".0", "") # remove the point to continue as whole number
            else:

                if d1 == True:
                    y = y.replace(".0", ".") # remove the Zero
                    d1 = False
                else:
                    pass
            y = y + "7"
            y = float(y)
        else: # no2
            global x
            x = str(x)
            if decimal == False: #and not a decimal
                x = x.replace(".0", "") # remove the point to continue as whole number
            else:

                if d1 == True:
                    x = x.replace(".0", ".") # remove the Zero
                    d1 = False
                else:
                    pass
                x = x  + "7"
                x = float(x)
        clearTextInput()
        Textbox1.insert(INSERT, "{0} {2} {1}".format(y, x, z))
        Textbox1.pack()


    def EIGHT():
        global d1
        if x1: # if on num 1
            global y
            y = str(y)
            if decimal == False: #and not a decimal
                y = y.replace(".0", "") # remove the point to continue as whole number
            else:

                if d1 == True:
                    y = y.replace(".0", ".") # remove the Zero
                    d1 = False
                else:
                    pass
            y = y + "8"
            y = float(y)
        else: # no2
            global x
            x = str(x)
            if decimal == False: #and not a decimal
                x = x.replace(".0", "") # remove the point to continue as whole number
            else:

                if d1 == True:
                    x = x.replace(".0", ".") # remove the Zero
                    d1 = False
                else:
                    pass
            x = x  + "8"
            x = float(x)
        clearTextInput()
        Textbox1.insert(INSERT, "{0} {2} {1}".format(y, x, z))
        Textbox1.pack()

    def NINE():
        global d1
        if x1: # if on num 1
            global y
            y = str(y)
            if decimal == False: #and not a decimal
                y = y.replace(".0", "") # remove the point to continue as whole number
            else:

                if d1 == True:
                    y = y.replace(".0", ".") # remove the Zero
                    d1 = False
                else:
                    pass
            y = y + "9"
            y = float(y)
        else: # no2
            global x
            x = str(x)
            if decimal == False: #and not a decimal
                x = x.replace(".0", "") # remove the point to continue as whole number
            else:

                if d1 == True:
                    x = x.replace(".0", ".") # remove the Zero
                    d1 = False
                else:
                    pass
            x = x  + "9"
            x = float(x)
        clearTextInput()
        Textbox1.insert(INSERT, "{0} {2} {1}".format(y, x, z))
        Textbox1.pack()

    def ZERO():
        global d1
        h = 0
        i = 0
        if x1: # if on num 1
            global y
            y = str(y)
            if decimal == False: #and not a decimal
                y = y.replace(".0", "") # remove the point to continue as whole number
            else:

                if d1 == True:
                    y = y.replace(".0", ".") # remove the Zero
                    d1 = False
                else:
                    pass
            y = y + "0"
            h = float(y)
        else: # no2
            global x
            x = str(x)
            if decimal == False: #and not a decimal
                x = x.replace(".0", "") # remove the point to continue as whole number
            else:

                if d1 == True:
                    x = x.replace(".0", ".") # remove the Zero
                    d1 = False
                else:
                    pass
            x = x  + "0"
            i = float(x)
        clearTextInput()
        Textbox1.insert(INSERT, "{0} {1} {2}".format(h, z, i))
        Textbox1.pack()


    def POINT():
        global decimal
        global d1
        decimal = True
        d1 = True

    def PLUS():
        global decimal
        global x1
        global z
        global function
        z = "+"
        x1 = False
        decimal = False
        function = "add"

    def MINUS():
        global decimal
        global x1
        global z
        global function
        z = "-"
        x1 = False
        decimal = False
        function = "minus"


    def TIMES():
        global decimal
        global x1
        global z
        global function
        z = "x"
        x1 = False
        decimal = False
        function = "times"

    def DIVIDE():
        global decimal
        global x1
        global z
        global function
        z = "/"
        x1 = False
        decimal = False
        function = "divide"

    def EQUALS():
        try:
            if function == "divide":
                k = y / x
            elif function == "add":
                k = y + a
            elif function == "minus":
                k = y - x
            elif function == "times":
                k= y * x
            else:
                pass
            clearTextInput()
            Textbox1.insert(INSERT, "{}".format(k))
            Textbox1.pack()
        except:
            pass

    One = Button(bf4, text = "1", command = ONE, height = 2, width = 8)
    Two = Button(bf4, text = "2", command = TWO, height = 2, width = 8)
    Three = Button(bf4, text = "3", command = THREE, height = 2, width = 8)
    Four = Button(bf3, text = "4", command = FOUR, height = 2, width = 8)
    Five = Button(bf3, text = "5", command = FIVE, height = 2, width = 8)
    Six = Button(bf3, text = "6", command = SIX, height = 2, width = 8)
    Seven = Button(bf2, text = "7", command = SEVEN, height = 2, width = 8)
    Eight = Button(bf2, text = "8", command = EIGHT, height = 2, width = 8)
    Nine = Button(bf2, text = "9", command = NINE, height = 2, width = 8)
    Zero = Button(bf5, text = "0", command = ZERO, height = 2, width = 8)
    Times = Button(bf2, text = "X", command = TIMES, height = 2, width = 8)
    Divide = Button(bf3, text = "/", command = DIVIDE, height = 2, width = 8)
    Add = Button(bf4, text = "+", command = PLUS, height = 2, width = 8)
    Point = Button(bf5, text = ".", command = POINT, height = 2, width = 8)
    Minus = Button(bf5, text = "-", command = MINUS, height = 2, width = 8)
    Equals = Button(bf5, text = "=", command = EQUALS, height = 2, width = 8)
    GoBack = Button(bf1, text = "Reset", command = Quitb, height = 2, width = 8)


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


def Power():

    powerwin = Tk()

    def mainpowertextclear():
        powermaintext.delete("1.0","end")

    framep1 = Frame(powerwin)
    framep2 = Frame(powerwin)
    framep3 = Frame(powerwin)
    framep1.pack()
    framep2.pack()
    framep3.pack()

    powermaintext = Text(framep1, height = 2, width = 52)
    powermaintext.insert(INSERT, "In box one enter the number and in box two the power you would like then procede to hit calculate.")
    powermaintext.pack()

    powerwin.mainloop()

def quitmain(): # quit feature for quit button
    root.destroy()

def apass(): # empty func for testing buttons and other features
    pass

frame0 = Frame(root) # Frames to hold button positions
frame1 = Frame(root)
frame2 = Frame(root)


frame0.pack()
frame1.pack()
frame2.pack()

Textbox = Text(frame0, height = 2, state = NORMAL)
Textbox.insert(INSERT, "Welcome please make a choice as to which feature you will use today.") # welcoming text
Textbox.pack()


Choice1 = Button(frame1, text = "Basic Operations", command = basicbuttons, height = 3, width = 20) # buttons to access different features
Choice2 = Button(frame1, text = "X to the Power of Y", command = Power, height = 3, width = 20)
Choice3 = Button(frame1, text = "Circle Operations", command = apass, height = 3, width = 20)
Choice4 = Button(frame1, text = "The Square Root", command = apass, height = 3, width = 20)


Choice1.pack(side = LEFT)
Choice2.pack(side = LEFT)
Choice3.pack(side = LEFT)
Choice4.pack(side = LEFT)


Quitmain = Button(master = frame2, text = "Exit", command = quitmain, height = 2, width = 10) # quit button
Quitmain.pack()

root.mainloop()
