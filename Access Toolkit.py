#!/usr/bin/env python
# coding: utf-8

__author__ = "Monish Mohanan"
__version__ = "1.0"

try:
    from tkinter import Tk, ttk, Label, Button, \
        BOTH, END, Canvas, Menu, Toplevel, X, \
            Frame, INSERT, Text, WORD, Listbox, Scrollbar, ACTIVE, BOTTOM
    from tkinter.filedialog import askopenfile
    from functools import partial
    from os import startfile, path, listdir, remove
    from pathlib import PureWindowsPath
    from tkinter import messagebox
    from initializer import initialize
    import tkinter.scrolledtext as tkst
    import webbrowser
    import time
    import sqlite3
    import sys
except Exception as e:
    from tkinter import messagebox
    messagebox.showwarning(
        "Module Error", "Error in importing modules: "+str(e))
try:
    if 'accessData.db' not in listdir():
        initialize()
    else:
        print("The database is configured properly")
except Exception as e:
    user = messagebox.showwarning(
        'Database Error', 'Error in accessing the database:'+ str(e))
    sys.exit(0)
if 'accessData.db' in listdir():
    try:
        access = sqlite3.connect('accessData.db')
        cur = access.cursor()
        cur.execute('''SELECT Name, Link FROM LinkButtons''')
        Buttons = dict((col[0], col[1]) for col in cur.fetchall())
        cur.execute('''SELECT Width, Height FROM WindowManager''')
        window_dimensions = cur.fetchall()
        size = str(window_dimensions[0][0])+"x"+str(window_dimensions[0][1])
        width = int(window_dimensions[0][0])
        height = int(window_dimensions[0][1])
        back = "#9C2004"
        access.close()
    except Exception as e:
        user = messagebox.showwarning(
            "Database Error", "Error in parsing the database: "+ str(e))
        sys.exit(0)
else:
    sys.exit(0)
class Application(object):
    def __init__(self, master):
        self.master = master
        master.geometry(size)
        master.resizable(0,0)
        master.configure(background = 'white')
        master.title("Access Toolkit")
        self.font = ttk.Style()
        self.font.configure('my.TButton', font=('Helvetica 12 bold'))
        menu = Menu(self.master)
        self.master.config(menu = menu)
        file_menu = Menu(menu, tearoff = 0)
        file_menu.add_command(label = 'Settings', command = self.setting)
        file_menu.add_command(label = 'Exit', command = master.destroy)
        menu.add_cascade(label = 'File', menu = file_menu)
        help_menu = Menu(menu, tearoff = 0)
        help_menu.add_command(label = 'Documentation', command = self.documentation)
        help_menu.add_command(label = 'About...', command = self.about)
        help_menu.add_command(label = 'Reset', command = self.reset)
        menu.add_cascade(label = 'Help', menu = help_menu)
        Frame(
            master, width = 490, 
            height = 20, bg = 'white').pack(fill = X)
        Frame(
            master, width = 490, 
            height = 20, bg = 'white').pack(fill = X, side = BOTTOM)
        for key, value in Buttons.items():
            ttk.Button(master, text = key,style = 'my.TButton',
            command = partial(self.run, key)).pack( fill = BOTH, expand = True)
    def run(self, value):
        self.link = Buttons[value]
        self.win_path = PureWindowsPath(self.link)
        self.path = path.realpath(self.win_path)
        try:
            webbrowser.open(Buttons[value])
        finally:
            startfile(self.path)
    def setting(self):
        self.settings_window = Toplevel(self.master)
        self.app = Settings(self.settings_window)
    def reset(self):
        self.reset_message = """
        You are about to reset the Access Toolkit\n
        This action cannot be UNDONE\n
        Do you really want to continue?
        """
        self.reset_value = messagebox.askyesno("Confirmation", self.reset_message)
        if self.reset_value == True:
            try:
                self.master.destroy()
                remove("accessData.db")
                messagebox.showinfo(
                    "Success", "The Access Toolkit has been successfully reset")
                sys.exit(0)
            except Exception as e:
                messagebox.showwarning(
                    "Failure", "Sorry! The toolkit could not be reset "+ str(e))
        else:
            pass
    def documentation(self):
        try:
            startfile('AccessToolkit-docs.pdf')
        except Exception as e:
            messagebox.showwarning(
                "Not available", "Oops! Documentation cannot be accessed")
    def about(self):
        self.about_window = Toplevel(self.master)
        self.app = About(self.about_window)
class Settings(Application):
    def __init__(self, master):
        self.master = master
        master.geometry('500x460')
        master.title('Settings')
        master.configure(background = 'white')
        master.resizable(0,0)
        Frame(
                master, width = 490, 
                height = 40, highlightthickness = 4,
                bg = '#9B240A').pack(fill = X)
        Label(master, text = 'Configured Buttons', font = ('helvetica 15 bold'),
                bg = '#9B240A', fg = 'white').place(x = 150, y = 5)
        Frame(
                master, width = 490, 
                height = 170, highlightthickness = 4, 
                bg = 'white').pack()
        self.buttonbox = Listbox(
            master, bg = 'white', 
            width = 73, height = 6, cursor = 'hand2')
        self.sr = Scrollbar(master)
        self.buttonbox.config(yscrollcommand = self.sr.set)
        self.sr.config(command = self.buttonbox.yview)
        self.sr.place(x = 467, y = 65, height = 92)
        for key, value in Buttons.items():
            self.buttonbox.insert(END, str(key)+ "   :   "+str(value))
        self.buttonbox.place(x = 20, y = 60)
        ttk.Button(
                    master, text = "Add", 
                    command = self.add_button).place(x = 160, y = 170)
        ttk.Button(
                    master, text = "Remove", 
                    command = self.remove_button).place(x = 250, y = 170)
        Frame(
                master, width = 490, 
                height = 40, highlightthickness = 4,
                bg = '#9B240A').pack(fill = X)
        Frame(
                master, width = 490, 
                height = 160, highlightthickness = 4,
                bg = 'white').pack()
        Label(master, text = "Window Resizing", font = ('helvetica 15 bold'),
                bg = "#9B240A", fg = 'white').place(x = 150, y = 215)
        Label(
                master, text = "Width: ", 
                font = ('helvetica 12 bold'),
                bg = 'white').place(x = 20, y = 270)
        Label(
                master, text = "Info:", 
                font = ('helvetica 10 bold'),
                bg = 'white').place(x = 20, y = 330)
        Label(
                master, text = "Width range: 280 - 700", 
                font = ('helvetica 10 italic'),
                bg = 'white').place(x = 30, y = 350)
        Label(
                master, text = "Height range: 450 - 1000", 
                font = ('helvetica 10 italic'),
                bg = 'white').place(x = 30, y = 370)
        self.width = Text(master, width = 5, height = 1, bd = 1.5)
        self.width.insert(INSERT, width)
        self.width.place(x = 90, y = 271.5)
        Label(
                master, text = "Height: ", 
                font = ('helvetica 12 bold'),
                bg = 'white').place(x = 20, y = 300)
        self.height = Text(master, width = 5, height = 1, bd = 1.5)
        self.height.insert(INSERT, height)
        self.height.place(x = 90, y = 301.5)
        ttk.Button(
                    master, text = "Preview", 
                    command = self.preview).place(x = 220, y = 280)
        ttk.Button(
                    master, text = "Save", 
                    command = self.save).place(x = 310, y = 420)
        ttk.Button(
                    master, text = "Cancel", 
                    command = lambda: master.destroy()).place(x = 410, y = 420) 
    def add_button(self):
        self.add_button_window = Toplevel(self.master)
        self.add = addButton(self.add_button_window)
    def remove_button(self):
        self.remove_button_window = Toplevel(self.master)
        self.remove = removeButton(self.remove_button_window)
    def save(self):
        self.window_width = int(self.width.get("1.0", "end-1c"))
        self.window_height = int(self.height.get("1.0", "end-1c"))
        self.success = '''
        The window size has been successfully modified.
        Kindly restart the application
        '''
        if (self.window_width != width) or (self.window_height != height):
            self.window_value = messagebox.askyesno(
                "Confirmation", "Do you really want to change the window size ?")
            if self.window_value == True:
                if self.window_width in range(280, 701) and \
                    self.window_height in range(450, 1001):
                    try:
                        access_database = sqlite3.connect('accessData.db')
                        cur = access_database.cursor()
                        cur.execute('''
                        UPDATE WindowManager SET Width = ?, Height = ? WHERE Id = ?''',
                            (str(self.window_width), str(self.window_height), 1))
                        access_database.commit()
                        access_database.close()
                        messagebox.showinfo("Success", self.success)
                        sys.exit(0)
                    except Exception as e:
                        messagebox.showwarning(
                                "Database Error", 
                                "The window size could not be changed: "+str(e))
                    self.master.destroy()
                else:
                    messagebox.showwarning(
                                "Resizing Error", 
                                "Resizing values are not in acceptable range")
            else:
                self.master.destroy()
        else:
            self.master.destroy()
    def preview(self):
        self.w = int(self.width.get("1.0", "end-1c"))
        self.h = int(self.height.get("1.0", "end-1c"))
        if self.w in range(280, 701) and self.h in range(450, 1001):
            if (self.w != width) or (self.h != height):
                try:
                    self.canvas.destroy()
                except:
                    pass
                if self.h in range(450, 701):
                    self.canvas = Canvas(
                                            self.master, width = self.w/5, 
                                            height = self.h/5, bg = 'red')
                    self.canvas.place(x = 320, y = 260)
                else:
                    self.canvas = Canvas(
                                            self.master, width = self.w/8, 
                                            height = self.h/8, bg = 'red')
                    self.canvas.place(x = 320, y = 260)
            else:
                try:
                    self.canvas.destroy()
                except:
                    pass
                if self.h in range(450, 701):
                    self.canvas = Canvas(
                                            self.master, width = width/5, 
                                            height = height/5, bg = 'red')
                    self.canvas.place(x = 320, y = 260)
                else:
                    self.canvas = Canvas(
                                            self.master, width = self.w/8, 
                                            height = height/8, bg = 'red')
                    self.canvas.place(x = 320, y = 260)
        else:
            messagebox.showwarning(
                                    "Resizing Error", 
                                    "Resizing values are not in acceptable range")
class addButton(Settings):
    def __init__(self, master):
        self.master = master
        master.geometry('400x200')
        master.title("Add Button")
        master.resizable(0,0)
        master.configure(background = 'white')
        Frame(
                master, width = 380, 
                height = 150, highlightthickness = 4,
                bg = 'white').pack()
        Label(
                master, text = "Name: ", 
                font = ('helvetica 13 bold'),
                bg = 'white').place(x = 25, y = 15)
        self.name = Text(master, width = 20, height = 1.2, bd = 1.5)
        self.name.place(x = 100, y = 16.5)
        Label(
                master, text = "Link: ", 
                font = ('helvetica 13 bold'),
                bg = 'white').place(x = 25, y = 50)
        self.link = Text(master, width = 43, height = 2.5, bd = 1.5)
        self.link.place(x = 25, y = 80)
        ttk.Button(
                    master, text = 'Cancel', 
                    command = lambda: master.destroy()).place(x = 312, y = 162)
        ttk.Button(master, text = 'Add', command = self.add).place(x = 220, y = 162)
    def add(self):
        add_result = messagebox.askyesno("Confirmation", "Are you sure ?")
        if add_result == True:
            name = self.name.get("1.0", "end-1c")
            link = self.link.get("1.0", "end-1c")
            self.success = '''The button has been successfully added.
            Kindly restart the application
            '''
            try:
                access_database = sqlite3.connect('accessData.db')
                cur = access_database.cursor()
                cur.execute('''
                            INSERT INTO LinkButtons(Name, Link)VALUES(?, ?)''',
                            (str(name), str(link)))
                access_database.commit()
                access_database.close()
                messagebox.showinfo("Success", self.success)
                sys.exit(0)
            except Exception as e:
                messagebox.showwarning(
                    "Failure", "Cannot add a new button: "+ str(e))
            self.master.destroy()
        else:
            self.master.destroy()
class removeButton(Settings):
    def __init__(self, master):
        self.master = master
        master.geometry('250x190')
        master.title("Remove Button")
        master.resizable(0,0)
        master.configure(background = 'white')
        Label(
                master, text = "Select the Button the remove", 
                font = ('helvetica 10 bold'),
                bg = 'white').place(x = 18, y = 3)
        self.buttonbox = Listbox(
            master, bg = 'white', width = 33, height = 6, cursor = 'hand2')
        self.sr = Scrollbar(master)
        self.buttonbox.config(yscrollcommand = self.sr.set)
        self.sr.config(command = self.buttonbox.yview)
        self.sr.place(x = 225, y = 32, height = 92)
        for key in Buttons.keys():
            self.buttonbox.insert(END, str(key))
        self.buttonbox.place(x = 20, y = 30)
        ttk.Button(
                    master, text = 'Cancel', 
                    command = lambda: master.destroy()).place(x = 162, y = 145)
        ttk.Button(
                    master, text = 'Remove', 
                    command = self.remove).place(x = 70, y = 145)
    def remove(self):
        result = messagebox.askyesno(
            "Confirmation", "Are you sure to remove %s?"%(self.buttonbox.get(ACTIVE)))
        self.success = '''The button has been successfully removed.
        Kindly restart the application
        '''
        if result == True:
            self.value = str(self.buttonbox.get(ACTIVE))
            print(self.value)
            try:
                access_database = sqlite3.connect('accessData.db')
                cur = access_database.cursor()
                cur.execute('''
                DELETE FROM LinkButtons WHERE Name = ?''', (self.value,))
                access_database.commit()
                access_database.close()
                messagebox.showinfo("Success", self.success)
                sys.exit(0)
            except Exception as e:
                messagebox.showwarning(
                    "Database Error", "The button cannot be removed: "+str(e))
            self.master.destroy()
        else:
            self.master.destroy()
class About(Application):
    def __init__(self, master):
        self.master = master
        master.geometry('500x300')
        master.title('About')
        master.configure(background = back)
        master.resizable(0,0)
        self.longtext = """        The tool can be used for mapping all the
        important links of folders, files and urls as specific 
        buttons which can be accessed later at ease"""
        Label(
                master, text = "Access Toolkit", 
                font = ('arial bold', 20),
                fg = 'white', bg = back).pack(fill = X)
        Label(
                master, text = self.longtext, 
                font = ('helvetica', 14),
                justify = 'left', 
                fg = 'white', bg = back).place(x = 1, y = 60)
        Label(
                master, text = "Contact Info:", 
                font = ('arial bold', 14),
                fg = 'white', bg = back).place(x = 45, y = 150)
        Label(
                master, text = "Author: ", 
                font = ('arial bold', 13),
                fg = 'white', bg = back).place(x = 45, y = 180)
        Label(
                master, text = "Monish Mohanan", 
                font = ('helvetica', 13),
                fg = 'white', bg = back).place(x = 120, y = 180)
        Label(
                master, 
                text = "This tool was developed using python",
                font = ('helvetica 12 italic'), 
                fg = 'white', bg = back).place(x = 90, y = 250)  
                  
window = Tk()
app = Application(window)
window.mainloop()