import tkinter
import main


def start():
    root.event_generate("<<start>>")


def perso(evt):
    main.main()
    if len(main.flaggedEntries) == 0:
        result.config(text="No warning")
        result.pack()
    else:
        result.config(text=main.flaggedEntries)
        result.pack()


root = tkinter.Tk()
title = tkinter.Label (text = "Welcome in Browser History Analyser")
title.pack()

result = tkinter.Label()
button = tkinter.Button (text = "START", command=start)
button.pack()

root.bind("<<start>>", perso)
root.mainloop()