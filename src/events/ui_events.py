import tkinter as tk

def listbox_selection_changed(event):
    selection = event.widget.curselection()
    if selection:
        index = selection[0]
        print("Selected:", event.widget.get(index))
        event.widget.get(index)