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


def validParam_event(windows,limit_entries, max_entries, max_threads, url_haus_conf, virus_total_conf):
    main.config.modif_file(limit_entries.get(), max_entries, max_threads, url_haus_conf, virus_total_conf, "src")
    windows.destroy()
    result = tkinter.Label()
    result.config(text="param modifié")
    result.pack()

def annulParam_event(windows):
    windows.destroy()


def modifParam():
    paramWindows = tkinter.Toplevel(root)
    var_case = tkinter.BooleanVar(paramWindows)
    var_case.set(True)
    case = tkinter.Checkbutton(paramWindows, text="Limiter le nombre d'entrées", variable=var_case)
    case.pack()



    max_entries=10
    max_threads=50
    url_haus_conf=None
    virus_total_conf=None
    button_valid_param = tkinter.Button(paramWindows, text="valider param", command=lambda: validParam_event(paramWindows,var_case, max_entries, max_threads, url_haus_conf, virus_total_conf))
    button_valid_param.pack()
    button_reset_param = tkinter.Button(paramWindows, text="Annuler modification", command=lambda: annulParam_event(paramWindows))
    button_reset_param.pack()
    paramWindows.mainloop()




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
