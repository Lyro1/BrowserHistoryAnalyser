import tkinter
from tkinter import ttk
import main

from src.Entities.ConfigEntry import ConfigEntry
from src.Entities.HistoryEntryFlags import HistoryEntryFlags


def start():
    root.event_generate("<<start>>")
    button_start.config(state="disable")

def start_event(evt):
    main.main()
    #test flag positif
    '''flags = HistoryEntryFlags()
    flags.url_haus = True
    entry = main.HistoryEntry("http://182.59.75.73:42447/bin.sh")
    entry.flagged = flags
    main.flaggedEntries.append(entry)'''
    result = tkinter.Label()
    result.config(text=main.result())
    result.pack()





def modifParam():
    paramWindows = tkinter.Toplevel(root)
    button_limit_entries = ttk.Checkbutton(paramWindows, text="Limit entries")
    button_limit_entries.pack()
    print(button_limit_entries.instate(['selected']))

    '''J'en suis ici
    Il faut faire un bouton pour valider les paramètres
    il faut ensuite faire les boutons permettant de modifier les paramètre'''

    button_valid_param = tkinter.Button(paramWindows,text="valider param", command=validParam)
    button_change_param.pack()

    result = tkinter.Label()
    result.config(text="param modifié")
    result.pack()


root = tkinter.Tk()

title = tkinter.Label (text = "Welcome in Browser History Analyser")
title.pack()


button_start = tkinter.Button(text = "START", command=start)
button_start.pack()

button_change_param = tkinter.Button(text="modifier param", command=modifParam)
button_change_param.pack()




root.bind("<<start>>", start_event)
root.mainloop()