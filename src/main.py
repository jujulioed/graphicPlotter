from tkinter import *
from tkinter import ttk
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk

def plot(parent):
    fig = Figure(figsize=(5,5), dpi=100)

    #list of squares
    y = [i**2 for i in range(101)]

    #adding the subplot
    plot1 = fig.add_subplot(111)

    #plotting the graph
    plot1.plot(y)

    #creating the tkinter canvas containing the Matplotlib figure
    canvas = FigureCanvasTkAgg(fig, master=parent)

    canvas.draw()

    # placing the canvas on the Tkinter window
    canvas.get_tk_widget().grid(column=0, row=1, columnspan=2, sticky="nsew")

    # creating the matplotlib toolbar
    toolbar = NavigationToolbar2Tk(canvas, parent, pack_toolbar=False)
    toolbar.update()

    # placing the toolbar on the tkinter window
    toolbar.grid(
        column=0,
        row=2,
        columnspan=2,
        sticky="ew"
    )



def main():
    root = Tk()
    frame = ttk.Frame(root, padding=10)
    frame.grid()
    ttk.Label(frame, text="Hello World").grid(column=0, row=0)
    ttk.Button(frame, text="Quit", command=root.destroy).grid(column=1, row=0)

    plot(root)

    root.mainloop()

if  __name__ == "__main__":
    main()