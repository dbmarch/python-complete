# Write a GUI program to create a simple calculator
# layout that looks like the screenshot.
#
# Try to be as Pythonic as possible - it's ok if you
# end up writing repeated Button and Grid statements,
# but consider using lists and a for loop.
#
# There is no need to store the buttons in variables.
#
# As an optional extra, refer to the documentation to
# work out how to use minsize() to prevent your window
# from being shrunk so that the widgets vanish from view.
#
# Hint: You may want to use the widgets .winfo_height() and
# winfo_width() methods, in which case you should know that
# they will not return the correct results unless the window
# has been forced to draw the widgets by calling its .update()
# method first.
#
# If you are using Windows you will probably find that the
# width is already constrained and can't be resized too small.
# The height will still need to be constrained, though.
try:
    import tkinter
except ImportError:
    import Tkinter as tkinter

import os

mainWindow = tkinter.Tk()
mainWindow.title("Calculator")
mainWindow.geometry('400x400')  #width height right down
mainWindow['padx'] = 8
mainWindow['pady'] = 8
mainWindow.update()
mainWindow.minsize(mainWindow.winfo_width(), mainWindow.winfo_height())
#mainWindow.minsize(400)

mainWindow.columnconfigure(0,weight=1)
mainWindow.columnconfigure(1,weight=1)
mainWindow.columnconfigure(2,weight=1)
mainWindow.columnconfigure(3,weight=1)

mainWindow.rowconfigure(0,weight=1)
mainWindow.rowconfigure(1,weight=1)
mainWindow.rowconfigure(2,weight=1)
mainWindow.rowconfigure(3,weight=1)
mainWindow.rowconfigure(4,weight=1)
mainWindow.rowconfigure(5,weight=1)


resultFrame = tkinter.Entry(mainWindow)
resultFrame.grid(row=0, column=0, columnspan=4, sticky='nw')

keypad = [
        [('C', 1), ('CE', 1)],
        [('7', 1), ('8', 1), ('9', 1), ('+', 1)],
        [('4', 1), ('5', 1), ('6', 1), ('-', 1)],
        [('1', 1), ('2', 1), ('3', 1), ('*', 1)],
        [('0', 1), ('=', 2), ('/', 1)],
]


y = 0
for row in keypad:
    x = 0
    for c in row:
        # print ("{} is in row {}".format(c, row))
        # print ("{} {} {}".format (c, c[0], c[1]))
        key = c[0]
        size = c[1]

        print ("{} takes up {} spaces and is placed at ({},{})".format(key,size, x, y))
        b = tkinter.Button(mainWindow, text = key)
        b.grid(row = y, column = x, columnspan=size, sticky='news')
        x = x + size
    y +=  1

mainWindow.mainloop()
