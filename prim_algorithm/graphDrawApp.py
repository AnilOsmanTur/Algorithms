from graphClass import Graph
from prim import mst_prim ,mst_to_edges
from drawGraphtoCanvas import drawGraphtoCanvas
from takeInput import takeFileInput, takeInstInput
from tkinter import *
from tkinter import filedialog as tkfd
from tkinter import messagebox as mbox
import numpy as np

class graphDrawApp:
    def __init__(self, master):
        self.master = master
        master.title("Prim Draw Graph - Anil Osman TUR - 12290551")

        # some need globals
        # canvas changes
        self.canvasItems = []
        self.canvasStep = 0 # has to be between 0 to stepCnt
        self.stepCnt = 0
        self.changes = []
        self.changeToggle = []
        self.startV = 0
        # # # #
        self.canvasSize = 400
        self.edges = []
        self.nodes = 0
        self.outputText = StringVar()
        self.graph = None
        self.mst_g = None

        # graph frame that contains the drawing part that has canvas and a label
        self.graphFrame = LabelFrame(master, labelanchor='nw', text="Graph")
        self.graphCanvas = Canvas(self.graphFrame, bg="white", height=self.canvasSize, width=self.canvasSize)

        # input frame that has the input areas
        self.inputFrame = LabelFrame(master, labelanchor='nw', text="Input")
        # take the edges from file
        self.readFileLabel = Label(self.inputFrame, text="Read from file")
        self.browseButton = Button(self.inputFrame, text="Browse", command=self.openFile)
        # take the edges from user
        self.inputLabel = Label(self.inputFrame, text="Type in the edges")
        vcmd = master.register(self.validate)  # we have to wrap the command
        self.inputEntry = Entry(self.inputFrame, bg="white", validate="focusout", validatecommand=(vcmd, "%P"))
        self.inputEntry.insert(0, "(0,1,1) (1,2,3) (0,2,2) (3,1,3)")
        # compute graph part
        self.drawButton = Button(self.inputFrame, text="Draw", command=self.draw)
        self.listLabel = Label(self.inputFrame, text="Choose a starting point")
        self.startPoints = Listbox(self.inputFrame, selectmode=SINGLE)
        self.startPoints.bind("<Double-Button-1>", self.choosePoint)
        self.computeButton = Button(self.inputFrame, text="Compute", command=self.compute)
        self.labelOutput = Label(self.inputFrame, bg="white", textvariable=self.outputText)
        # graph changes next and previous
        self.changeLabel = Label(self.inputFrame, text="Click next or prev to see steps.")
        self.prevButton = Button(self.inputFrame, text="Prev", command=self.prevGraph)
        self.nextButton = Button(self.inputFrame, text="Next", command=self.nextGraph)
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
        self.drawButton.grid(row=3, column=0, columnspan=2)
        self.listLabel.grid(row=4, column=0, columnspan=2)
        self.startPoints.grid(row=5, column=0, columnspan=2)
        self.computeButton.grid(row=6, column=0, columnspan=2)
        self.labelOutput.grid(row=7, column=0, rowspan=3, columnspan=2)
        self.changeLabel.grid(row=10, column=0, columnspan=2)
        self.prevButton.grid(row=11, column=0)
        self.nextButton.grid(row=11, column=1)
        self.closeButton.grid(row=12, column=0, columnspan=2)
        # graph frame
        self.graphCanvas.pack()


    # to take input from chosen file
    def openFile(self):
        fileName = tkfd.askopenfilename()
        if fileName != '' :
            inStr ,self.edges = takeFileInput(fileName)
            self.outputText.set("Read input:\n"+inStr)
            self.graph = Graph(self.edges)
            self.inputEntry.insert(0, '')
        else:
            self.outputText.set("There isn't any input.\nPlease, choose a file.")
            mbox.showerror("No Input", "There isn't any input.\nPlease, choose a file.")


    # user input validation
    def validate(self, text):
        if text == '':
            self.outputText.set("There isn't any input.\nPlease, Enter a edge array.")
            self.inputEntry.insert(0, '')
            return False
        try:
            self.edges = takeInstInput(text)
            print( "edges: ",self.edges)
            if self.edges != []:
                self.graph = Graph(self.edges)
                return True
        except ValueError:
            self.outputText.set("Wrong input format")
            mbox.showerror("Wrong Format", "Wrong input format")
            return False

    # draw the graph
    def draw(self):
        if not self.edges:
            if self.validate(self.inputEntry.get()):
                if not self.edges:
                    self.graphCanvas.delete("all")
                    self.outputText.set("There isn't any input.\nPlease, Enter a edges array.")
                    showerror("No Input", "There isn't any input.\nPlease, Enter a edges array.")
                else:
                    self.draw()
        else:
            edges = self.edges
            if edges != -1:
                self.graph = Graph(self.edges)
                self.edges = np.copy(self.graph.edges)
                self.graphCanvas.delete("all")
                self.canvasItems = drawGraphtoCanvas(self.graphCanvas, self.edges, self.graph.vertex_n, self.canvasSize)
                # print self.canvasItems
                for item in range(self.graph.vertex_n):
                    self.startPoints.insert(END, item)
            else:
                graphCheck = "ERROR : edges -1 There isn't a graph."
                mbox.showerror('No Graph', graphCheck)

    # computing is there a graph and if there is draws it
    def compute(self):
        if self.edges == []:
            self.draw()
            if self.edges != []:
                self.compute()
        else:
            edges = self.edges
            if edges != []:
                # calculating the mst with prim algorithm
                prim, keys = mst_prim(self.graph, self.startV)
                self.mst_g = Graph(mst_to_edges(prim, keys))
                self.find_changes()
                self.changeToggle = np.zeros(self.stepCnt)
                self.inputEntry.delete(0, END)
                self.edges = []
                self.startPoints.delete(0,END)
            else:
                graphCheck = "ERROR : edges is empty There isn't a graph."
                mbox.showerror('No Graph', graphCheck)

    def find_changes(self):
        if self.graph == None or self.mst_g == None:
            return False
        else:
            self.stepCnt = 0
            self.canvasStep = 0
            e_n = len(self.graph.edges)
            t_n = len(self.mst_g.edges)

            self.changes = []
            for i in range(e_n):
                for j in range(t_n):
                    if np.array_equal(self.graph.edges[i], self.mst_g.edges[j]):
                        self.changes.append(i)
                        self.stepCnt += 1
            self.outputText.set("There is %d step.\n This is step %d" % (self.stepCnt, self.canvasStep))

    # changing the canvas
    def makeChanges(self):
        if self.changeToggle[self.canvasStep] == 0:
            self.changeToggle[self.canvasStep] = 1
            j = self.changes[self.canvasStep]
            item = self.canvasItems[0]
            self.graphCanvas.itemconfig(item[j], fill='red')
        else:
            self.changeToggle[self.canvasStep] = 0
            j = self.changes[self.canvasStep]
            item = self.canvasItems[0]
            self.graphCanvas.itemconfig(item[j], fill='blue')


    # changing the canvas
    def prevGraph(self):
        if self.canvasStep > 0:
            self.canvasStep -= 1
            self.outputText.set("There is %d step.\n This is step %d" % (self.stepCnt, self.canvasStep))
            self.makeChanges()
        else:
            self.outputText.set("There isn't any step back.\nThere is %d step.\n This is step %d" % (self.stepCnt, self.canvasStep))

    def nextGraph(self):
        if self.canvasStep < self.stepCnt:
            self.outputText.set("There is %d step.\n This is step %d" % (self.stepCnt, self.canvasStep))
            self.makeChanges()
            self.canvasStep += 1
        else:
            self.outputText.set("There isn't any step further.\nThere is %d step.\n This is step %d" % (self.stepCnt, self.canvasStep))

    def choosePoint(self, x):
        w = x.widget
        index = int(w.curselection()[0])
        value = w.get(index)
        print( 'You selected item %d: "%s"' % (index, value))
        self.startV = value


###############
root = Tk()
app = graphDrawApp(root)
root.mainloop()
