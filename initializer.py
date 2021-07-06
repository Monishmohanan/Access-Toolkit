#!/usr/bin/env python
# coding: utf-8

# In[2]:
def initialize():
    try:
        from tkinter import Text, Label, Frame, ttk, Tk, INSERT
        import sys
        import sqlite3
        import time
    except Exception as e:
        from tkinter import messagebox
        messagebox.showwarning("Import Error", "Error in importing modules: "+str(e))
    def write_database():
        button_names = (button1.get("1.0", "end-1c"), button2.get("1.0", "end-1c"), \
                       button3.get("1.0","end-1c"), button4.get("1.0","end-1c"), \
                       button5.get("1.0","end-1c"))
        links = (link1.get("1.0", "end-1c"), link2.get("1.0", "end-1c"), link3.get("1.0", "end-1c"), \
                link4.get("1.0", "end-1c"), link5.get("1.0", "end-1c"))
        access_db = sqlite3.connect('accessData.db')
        cur = access_db.cursor()
        cur.execute('''CREATE TABLE IF NOT EXISTS LinkButtons(Id INTEGER PRIMARY KEY NOT NULL,
        Name TEXT NOT NULL, Link TEXT NOT NULL)''')
        for button, link in zip(button_names, links):
            cur.execute('''INSERT INTO LinkButtons(Name, Link)VALUES(?, ?)''',(str(button), str(link)))
        cur.execute('''CREATE TABLE IF NOT EXISTS WindowManager(Id INTEGER PRIMARY KEY NOT NULL,
        Width TEXT NOT NULL, Height TEXT NOT NULL)''')
        cur.execute('''INSERT INTO WindowManager(Width, Height)VALUES(?, ?)''', (str(280), str(450)))
        access_db.commit()
        access_db.close()
        window.destroy()
        time.sleep(1)
    greetings = '''Greetings..!
    Kindly configure the application for initialization
    '''
    window = Tk()        
    window.geometry('600x570')
    window.title("Initializing Access Toolkit")
    window.configure(background = 'white')
    window.resizable(0,0)
    Frame(window, width = 560, height = 130, bg = 'white', highlightthickness = 4).pack()
    Label(window, text = "Hey there...", font = ('Brush Script MT', 19), \
         bg = 'white', fg = '#7A1802').place(x = 30, y = 5)
    Label(window, text = greetings, font = ('Brush Script MT', 19), \
         bg = 'white', fg = '#7A1802').place(x = 30, y = 30)
    Frame(window, width = 560, height = 40, bg = 'white', highlightthickness = 4).pack()
    Label(window, text = 'Buttons', font = ('helvetica 15 bold'), bg = 'white').place(x = 90, y=135)
    Label(window, text = 'Links', font = ('helvetica 15 bold'), bg = 'white').place(x = 370, y=135)
    Frame(window, width = 560, height = 340, bg = 'white', highlightthickness = 4).pack()
    #-------------------Button Boxes------------------------
    button1 = Text(window, width = 20, height = 1.2, bd = 1.5)
    button1.place(x = 50, y = 207)
    button1.insert(INSERT, "Button 1")
    button2 = Text(window, width = 20, height = 1.2, bd = 1.5)
    button2.place(x = 50, y = 267)
    button2.insert(INSERT, "Button 2")
    button3 = Text(window, width = 20, height = 1.2, bd = 1.5)
    button3.place(x = 50, y = 327)
    button3.insert(INSERT, "Button 3")
    button4 = Text(window, width = 20, height = 1.2, bd = 1.5)
    button4.place(x = 50, y = 387)
    button4.insert(INSERT, "Button 4")
    button5 = Text(window, width = 20, height = 1.2, bd = 1.5)
    button5.place(x = 50, y = 447)
    button5.insert(INSERT, "Button 5")
    #--------------------Link Boxes---------------------------
    link1 = Text(window, width = 35, height = 2.3, bd = 1.5)
    link1.place(x = 265, y = 200)
    link2 = Text(window, width = 35, height = 2.3, bd = 1.5)
    link2.place(x = 265, y = 260)
    link3 = Text(window, width = 35, height = 2.3, bd = 1.5)
    link3.place(x = 265, y = 320)
    link4 = Text(window, width = 35, height = 2.3, bd = 1.5)
    link4.place(x = 265, y = 380)
    link5 = Text(window, width = 35, height = 2.3, bd = 1.5)
    link5.place(x = 265, y = 440)
    ttk.Button(window, text = 'Cancel', command = lambda: sys.exit(0)).place(x = 500, y = 530)
    ttk.Button(window, text = 'Save', command = write_database).place(x = 400, y = 530)
    window.mainloop()