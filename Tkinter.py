import tkinter
from tkinter import *
import main

from src.Entities.ConfigEntry import ConfigEntry
from src.Entities.HistoryEntryFlags import HistoryEntryFlags


def start_event():
    main.main()
    # test flag positif
    '''
    flags = HistoryEntryFlags()
    flags.url_haus = True
    entry = main.HistoryEntry("http://182.59.75.73:42447/bin.sh")
    entry.flagged = flags
    main.flaggedEntries.append(entry)
    '''
    result.config(text=main.result())
    button_start.config(state="disable")


def validParam_event(windows, limit_entries, max_entries, max_threads, url_haus_conf, virus_total_conf, virus_total_api):
    url_haus = ConfigEntry(url_haus_conf.get())
    virus_total = ConfigEntry(virus_total_conf.get(),virus_total_api.get())
    main.config.modif_file(limit_entries.get(), max_entries.get(), max_threads.get(), url_haus, virus_total, "src")
    windows.destroy()
    result.config(text="param modifié")


def annulParam_event(windows):
    windows.destroy()



def only_numeric_input(P):
    if P.isdigit() or P == "":
        return True
    return False

def add_api_key(paramWindows,api, api_zone, textzone):
    api_zone.config(textvariable=api)
    textzone.grid(row=5,column=0,sticky="e")
    api_zone.grid(row=5,column=1, columnspan=2, sticky="w")



def modifParam():
    paramWindows = tkinter.Toplevel(root)
    lab0 = tkinter.Label(paramWindows, text="Limit the number of entries: ")
    lab0.grid(row=0,column=0, sticky="e")
    limit_entries = tkinter.BooleanVar(paramWindows)
    limit_entries.set(True)
    limit_entries_checkbox = tkinter.Checkbutton(paramWindows, variable=limit_entries)
    limit_entries_checkbox.grid(row=0, column=1, columnspan=2, sticky="w")

    max_entries = tkinter.IntVar(paramWindows)
    max_entries.set(100)
    func_callback = paramWindows.register(only_numeric_input)
    lab = tkinter.Label(paramWindows, text="Number of max entries: ")
    lab.grid(row=1,column=0,sticky="e")
    max_entries_zone = tkinter.Entry(paramWindows, textvariable=max_entries, validate='all', validatecommand=(func_callback, "%P"))
    max_entries_zone.grid(row=1,column=1, columnspan=2,sticky="w")

    lab1 = tkinter.Label(paramWindows, text="Number of parallel threads: ")
    lab1.grid(row=2,column=0,sticky="e")
    max_threads = tkinter.IntVar(paramWindows)
    max_threads.set(32)
    max_threads_zone = tkinter.Scale(paramWindows, orient='horizontal', from_=0, to=64, resolution=2, tickinterval=8, length=350, variable=max_threads)
    max_threads_zone.grid(row=2,column=1, columnspan=2,sticky="w")

    lab2 = tkinter.Label(paramWindows, text="Check with URLHaus: ")
    lab2.grid(row=3,column=0,sticky="e")
    url_haus_conf = tkinter.BooleanVar(paramWindows)
    url_haus_conf.set(True)
    url_haus_conf_checkbox = tkinter.Checkbutton(paramWindows,
                                                 variable=url_haus_conf)
    url_haus_conf_checkbox.grid(row=3,column=1, columnspan=2,sticky="w")

    lab3 = tkinter.Label(paramWindows, text="Check with VirusTotal: ")
    lab3.grid(row=4,column=0,sticky="e")
    api = tkinter.StringVar(paramWindows)
    api_zone = tkinter.Entry(paramWindows)
    virus_total_conf = tkinter.BooleanVar(paramWindows)
    virus_total_conf.set(False)
    virus_total_conf_checkbox = tkinter.Checkbutton(paramWindows, variable=virus_total_conf, command=lambda: add_api_key(paramWindows,api, api_zone,textzone))
    virus_total_conf_checkbox.grid(row=4,column=1, columnspan=2,sticky="w")

    button_valid_param = tkinter.Button(paramWindows, text="Validate settings",
                                        command=lambda: validParam_event(paramWindows, limit_entries, max_entries,
                                                                         max_threads, url_haus_conf, virus_total_conf, api))
    button_valid_param.grid(row=6,column=1)
    button_reset_param = tkinter.Button(paramWindows, text="Cancel",
                                        command=lambda: annulParam_event(paramWindows))
    button_reset_param.grid(row=6,column=2)
    textzone = tkinter.Label(paramWindows, text="Insert an api-key for VirusTotal: ")
    paramWindows.mainloop()





root = tkinter.Tk()
root.title('Browser History Analyser')
root.geometry("500x200")



title = tkinter.Label(text="Welcome in Browser History Analyser")
title.pack()

button_start = tkinter.Button(text="Start analysis", command=start_event)
button_start.pack()

button_change_param = tkinter.Button(text="Change settings", command=modifParam)
button_change_param.pack()

button_close = tkinter.Button(text="Exit", command=root.destroy)
button_close.pack()

result = tkinter.Label()
result.pack()

root.mainloop()
