from havelHakimi import havelHakimi
from drawGraphtoCanvas import drawGraphtoCanvas
from takeInput import takeFileInput, takeInstInput
from tkinter import *
from tkinter import filedialog as tkfd
from tkinter import messagebox as mbox

class graphDrawApp:
    def __init__(self, master):
        self.master = master
        master.title("Havel-Hakimi Draw Graph - Anil Osman TUR - 12290551")

        # some need globals
        self.canvasSize = 400
        self.degrees = []
        self.outputText = StringVar()

        # graph frame that contains the drawing part that has canvas and a label
        self.graphFrame = LabelFrame(master, labelanchor='nw', text="Graph")
        self.graphCanvas = Canvas(self.graphFrame, bg="white", height=self.canvasSize, width=self.canvasSize)

        # input frame that has the input areas
        self.inputFrame = LabelFrame(master, labelanchor='nw', text="Input")
        # take the degrees from file
        self.readFileLabel = Label(self.inputFrame, text="Read from file")
        self.browseButton = Button(self.inputFrame, text="Browse", command=self.openFile)
        # take the degrees from user
        self.inputLabel = Label(self.inputFrame, text="Type in the degrees")
        vcmd = master.register(self.validate)  # we have to wrap the command
        self.inputEntry = Entry(self.inputFrame, bg="white", validate="focusout", validatecommand=(vcmd, "%P"))
        self.inputEntry.insert(0, "4 4 3 3 2 2")
        # compute graph part

        self.computeButton = Button(self.inputFrame, text="Compute", command=self.compute)
        self.labelOutput = Label(self.inputFrame, bg="white", textvariable=self.outputText)
        # closing
        self.closeButton = Button(self.inputFrame, text="Close", command=master.quit)

        # LAYOUT
        self.inputFrame.grid(row=0, column=0, sticky=N+S)
        self.graphFrame.grid(row=0, column=1)
        # input frame
        self.readFileLabel.grid(row=0, column=0)
        self.browseButton.grid(row=0, column=1)
        self.inputLabel.grid(row=1, column=0, columnspan=2)
        self.inputEntry.grid(row=2, column=0, columnspan=2)
        self.computeButton.grid(row=3, column=0, columnspan=2)
        self.labelOutput.grid(row=4, column=0, rowspan=2, columnspan=2)
        self.closeButton.grid(row=6, column=0, columnspan=2)
        # graph frame
        self.graphCanvas.pack()


    # to take input from chosen file
    def openFile(self):
        fileName = tkfd.askopenfilename()
        if fileName != '' :
            inStr ,self.degrees = takeFileInput(fileName)
            self.inputEntry.insert(0, inStr)
        else:
            self.outputText.set("There isn't any input.\nPlease, choose a file.")
            mbox.showerror("No Input", "There isn't any input.\nPlease, choose a file.")

    # user input validation
    def validate(self, text):
        if text == '':
            self.outputText.set("There isn't any input.\nPlease, Enter a degree array.")
            self.inputEntry.insert(0, '')
            return False
        try:
            self.degrees = takeInstInput(text)
            print( self.degrees )
            return True
        except ValueError:
            self.outputText.set("Wrong input format")
            mbox.showerror("Wrong Format", "Wrong input format")
            return False

    # computing is there a graph and if there is draws it
    def compute(self):
        if self.validate(self.inputEntry.get()):
            pass
        if not self.degrees:
            self.graphCanvas.delete("all")
            self.outputText.set("There isn't any input.\nPlease, Enter a degree array.")
            mbox.showerror("No Input", "There isn't any input.\nPlease, Enter a degree array.")
        else:
            node = len(self.degrees)
            edges = havelHakimi(self.degrees)
            if edges != -1:
                self.graphCanvas.delete("all")
                self.outputText.set("There is a graph")
                drawGraphtoCanvas(self.graphCanvas, edges, node, self.canvasSize)
                self.inputEntry.delete(0, END)
                self.degrees = []
            else:
                graphCheck = "There isn't a graph."
                showerror('No Graph', graphCheck)

###############
root = Tk()
app = graphDrawApp(root)
root.mainloop()
