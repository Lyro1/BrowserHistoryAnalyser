import tkinter
from tkinter import ttk
import main

from src.Entities.ConfigEntry import ConfigEntry
from src.Entities.HistoryEntryFlags import HistoryEntryFlags

def start_event():
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
    button_start.config(state="disable")


def validParam_event(limit_entries, max_entries, windows):
    main.config.modif_file(limit_entries=limit_entries,max_entries=max_entries)
    print("toto")
    windows.destroy()



def modifParam():
    paramWindows = tkinter.Toplevel(root)
    button_limit_entries = ttk.Checkbutton(paramWindows, text="Limit entries")
    button_limit_entries.pack()
    print(button_limit_entries.instate(['selected']))

    #J'en suis ici
    #Il faut faire un bouton pour valider les paramètres
    ##il faut ensuite faire les boutons permettant de modifier les paramètre

    button_valid_param = tkinter.Button(paramWindows, text="valider param", command=lambda: validParam_event(limit_entries=True, max_entries=10, windows=paramWindows))
    button_valid_param.pack()
    result = tkinter.Label()
    result.config(text="param modifié")
    result.pack()




root = tkinter.Tk()

title = tkinter.Label (text = "Welcome in Browser History Analyser")
title.pack()


button_start = tkinter.Button(text = "START", command=start_event)
button_start.pack()



button_change_param = tkinter.Button(text="modifier param", command=modifParam)
button_change_param.pack()


button_close = tkinter.Button(text= "close", command=root.destroy)
button_close.pack()



root.mainloop()
