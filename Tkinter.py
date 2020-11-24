import tkinter
import main


def start():
    root.event_generate("<<start>>")
def perso(evt):
    main.main()

root = tkinter.Tk()
title = tkinter.Label (text = "Bienvenue dans Browser History Analyser")
title.pack()

bouton = tkinter.Button (text = "START", command=start)
bouton.pack()

root.bind("<<start>>", perso)
root.mainloop()