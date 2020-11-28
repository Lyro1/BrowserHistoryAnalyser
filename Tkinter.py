import tkinter
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
    root.event_generate("<<Param>>")

def modifParam_event(evt):
    main.config.modif_file(max_entries=20, path='src')
    '''response['limit-entries'] = limit_entries
    if limit_entries == "True":
        response['max-entries'] = max_entries
    else:
        response['max-entries'] = None'''
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
root.bind("<<Param>>", modifParam_event)
root.mainloop()