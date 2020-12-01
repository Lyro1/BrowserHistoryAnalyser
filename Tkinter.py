import tkinter
from tkinter import ttk
import main

from src.Entities.ConfigEntry import ConfigEntry
from src.Entities.HistoryEntryFlags import HistoryEntryFlags


def start_event():
    main.main()
    # test flag positif
    '''flags = HistoryEntryFlags()
    flags.url_haus = True
    entry = main.HistoryEntry("http://182.59.75.73:42447/bin.sh")
    entry.flagged = flags
    main.flaggedEntries.append(entry)'''
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
    textzone.pack()
    api_zone.pack()



def modifParam():
    paramWindows = tkinter.Toplevel(root)
    limit_entries = tkinter.BooleanVar(paramWindows)
    limit_entries.set(True)
    limit_entries_checkbox = tkinter.Checkbutton(paramWindows, text="Limiter le nombre d'entrées", variable=limit_entries)
    limit_entries_checkbox.pack()
    max_entries = tkinter.IntVar(paramWindows)
    max_entries.set(100)
    func_callback = paramWindows.register(only_numeric_input)
    lab = tkinter.Label(paramWindows, text="Nombre d'entrées limites : ")
    lab.pack()
    max_entries_zone = tkinter.Entry(paramWindows, textvariable=max_entries, validate='all', validatecommand=(func_callback, "%P"))
    max_entries_zone.pack()
    max_threads = tkinter.IntVar(paramWindows)
    max_threads.set(32)
    max_threads_zone = tkinter.Scale(paramWindows, orient='horizontal', from_=0, to=64, resolution=2, tickinterval=8, length=350, label='Nb threads parallèle', variable=max_threads)
    max_threads_zone.pack()

    url_haus_conf = tkinter.BooleanVar(paramWindows)
    url_haus_conf.set(True)
    url_haus_conf_checkbox = tkinter.Checkbutton(paramWindows, text="vérifier avec url-Haus",
                                                 variable=url_haus_conf)
    url_haus_conf_checkbox.pack()

    api = tkinter.StringVar(paramWindows)
    api_zone = tkinter.Entry(paramWindows)
    max_entries_zone.pack()
    virus_total_conf = tkinter.BooleanVar(paramWindows)
    virus_total_conf.set(False)
    virus_total_conf_checkbox = tkinter.Checkbutton(paramWindows, text="vérifier avec Virus-Total",
                                                 variable=virus_total_conf, command=lambda: add_api_key(paramWindows,api, api_zone,textzone))
    virus_total_conf_checkbox.pack()


    button_valid_param = tkinter.Button(paramWindows, text="valider param",
                                        command=lambda: validParam_event(paramWindows, limit_entries, max_entries,
                                                                         max_threads, url_haus_conf, virus_total_conf, api))
    button_valid_param.pack()
    button_reset_param = tkinter.Button(paramWindows, text="Annuler modification",
                                        command=lambda: annulParam_event(paramWindows))
    button_reset_param.pack()
    textzone = tkinter.Label(paramWindows, text="insérer une key api pour virus-total")
    paramWindows.mainloop()





root = tkinter.Tk()
root.title('Browser History Analyser')

title = tkinter.Label(text="Welcome in Browser History Analyser")
title.pack()

button_start = tkinter.Button(text="START", command=start_event)
button_start.pack()

button_change_param = tkinter.Button(text="modifier param", command=modifParam)
button_change_param.pack()

button_close = tkinter.Button(text="close", command=root.destroy)
button_close.pack()

result = tkinter.Label()
result.pack()

root.mainloop()
