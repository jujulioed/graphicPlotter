import tkinter as tk

def listbox_selection_changed(event):
    selection = event.widget.curselection()
    if selection:
        index = selection[0]
        print("Selected:", selection[0])
        event.widget.get(index)