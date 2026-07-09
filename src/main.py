from tkinter import *
from tkinter import ttk
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk

from events.ui_events import listbox_selection_changed 

#def points_menu(parent:ttk.Frame):
    


def plot(parent):
    fig = Figure(figsize=(5,5), dpi=100)

    #list of squares
    #y = [i**2 for i in range(101)]

    #adding the subplot
    plot1 = fig.add_subplot(111)

    #plotting the graph
    # plot([x coordinates], [y coordinates])
    plot1.plot([10, 20], [5, 6])
    # each time we plot, we can see a new line in the graph
    plot1.plot([40, 50], [8, 9])

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
    root.title("Graph Plotter")
    frame = ttk.Frame(root, padding=10)
    frame.grid()
    ttk.Label(frame, text="Hello World").grid(column=0, row=0)
    ttk.Button(frame, text="Quit", command=root.destroy).grid(column=1, row=0)

    ttk.Frame(root, padding=10)
    ttk.Label(frame, text="Hello World").grid(column=0, row=0)

    listbox = Listbox(root)
    for item in ["Coord 1", "Coord 2", "Coord 3"]:
        listbox.insert(END, item)

    listbox.bind("<<ListboxSelect>>", listbox_selection_changed)
    listbox.grid(column=0, row=3, columnspan=2, sticky="nsew")
    
    plot(root)

    root.mainloop()

if  __name__ == "__main__":
    main()