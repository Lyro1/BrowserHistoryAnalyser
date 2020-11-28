import tkinter
import main
from src.Entities.ConfigEntry import ConfigEntry
from src.Entities.HistoryEntryFlags import HistoryEntryFlags


def start():
    root.event_generate("<<start>>")


def perso(evt):
    main.main()
    modifParam(evt)
    #test flag positif
    """ flags = HistoryEntryFlags() 
    flags.url_haus = True
    entry = main.HistoryEntry("http://182.59.75.73:42447/bin.sh")
    entry.flagged = flags
    main.flaggedEntries.append(entry)"""
    result.config(text=main.result())
    result.pack()

def modifParam(evt):
    main.config.modif_file(None,None,None,None,None,'src')
    '''response['limit-entries'] = limit_entries
    if limit_entries == "True":
        response['max-entries'] = max_entries
    else:
        response['max-entries'] = None'''



root = tkinter.Tk()
title = tkinter.Label (text = "Welcome in Browser History Analyser")
title.pack()

result = tkinter.Label()
button = tkinter.Button (text = "START", command=start)
button.pack()

root.bind("<<start>>", perso)
root.mainloop()