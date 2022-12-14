#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec 14 15:39:18 2022

@author: eujean
"""




import tkinter as tk
import tkinter.font as tkFont
from tkinter import *
from PIL import Image, ImageTk
import sqlite3
import datetime
import os
import string
import random


conn = sqlite3.connect('iPark.db')
c = conn.cursor()

#c.execute("""CREATE TABLE user (first_name text,last_name text,address text,contact_number text)""")
#c.execute("""CREATE TABLE reservation (first_name text,last_name text,address text,contact_number text,time_start text)""")
#c.execute("""CREATE TABLE admin (username text, password text)""")

class Menu:
    def __init__(self, root):
        #Title
        root.title("Parking system - IPARK")
        #Main Window size
        app_width=500
        app_height=600
        screenwidth = root.winfo_screenwidth()
        screenheight = root.winfo_screenheight()
        
        x = (screenwidth / 2) - (app_width / 2)
        y = (screenheight / 2) - (app_height / 2)
        root.geometry(f'{app_width}x{app_height}+{int(x)}+{int(y)}')
        
    
        root.resizable(width=False, height=False)
        
        Available_Button=tk.Button(root)
        Available_Button["bg"] = "#efefef"
        ft = tkFont.Font(family='Tahoma',size=15)
        Available_Button["font"] = ft
        Available_Button["fg"] = "#000000"
        Available_Button["justify"] = "center"
        Available_Button["text"] = "Check Available Slots"
        Available_Button.place(x=165,y=400,width=170,height=50)
        Available_Button["command"] = self.Available_Button_command
        
        Available_Button=tk.Button(root)
        Available_Button["bg"] = "#efefef"
        ft = tkFont.Font(family='Tahoma',size=12)
        Available_Button["font"] = ft
        Available_Button["fg"] = "#000000"
        Available_Button["justify"] = "center"
        Available_Button["text"] = "Admin"
        Available_Button.place(x=440,y=10,width=50,height=30)
        Available_Button["command"] = self.main_screen
        
        Availableslot=tk.Label(root)
        ft = tkFont.Font(family='Tahoma',size=22)
        Availableslot["font"] = ft
        Availableslot["fg"] = "#333333"
        Availableslot["justify"] = "center"
        Availableslot["text"] = "Parking System"
        Availableslot.place(x=150,y=100,width=200,height=120)
        
        
        image = Image.open("/Users/eujean/Documents/iParking/LOGO.png")
        resize_image = image.resize((370,300))
        img = ImageTk.PhotoImage(resize_image)
        label1 = Label(image=img)
        label1.image = img
        label1.pack()
        
        
        
    
        
    
#Button for slots

    def Available_Button_command(self):
        #App = Toplevel()---register = Toplevel(mainscreen)
        root = Toplevel()
        app_width=500
        app_height=600
        screenwidth = root.winfo_screenwidth()
        screenheight = root.winfo_screenheight()
        
        x = (screenwidth / 2) - (app_width / 2)
        y = (screenheight / 2) - (app_height / 2)
        root.geometry(f'{app_width}x{app_height}+{int(x)}+{int(y)}')
        
        Button1=tk.Button(root)
        Button1["bg"] = "#efefef"
        ft = tkFont.Font(family='Tahoma',size=16)
        Button1["font"] = ft
        Button1["fg"] = "#000000"
        Button1["justify"] = "center"
        Button1["text"] = "Slot 1"
        Button1.place(x=90,y=80,width=90,height=35)
        Button1["command"] = self.Button1_command

        Button2=tk.Button(root)
        Button2["bg"] = "#efefef"
        ft = tkFont.Font(family='Tahoma',size=16)
        Button2["font"] = ft
        Button2["fg"] = "#000000"
        Button2["justify"] = "center"
        Button2["text"] = "Slot 2"
        Button2.place(x=90,y=180,width=90,height=35)
        Button2["command"] = self.Button2_command

        Button3=tk.Button(root)
        Button3["bg"] = "#efefef"
        ft = tkFont.Font(family='Tahoma',size=16)
        Button3["font"] = ft
        Button3["fg"] = "#000000"
        #Button3['bg'] = "#8B8B83"
        Button3["justify"] = "center"
        Button3["text"] = "Slot 3"
        Button3.place(x=90,y=280,width=90,height=35)
        Button3["command"] = self.Button3_command
        
        Button7=tk.Button(root)
        Button7["bg"] = "#efefef"
        ft = tkFont.Font(family='Tahoma',size=16)
        Button7["font"] = ft
        Button7["fg"] = "#000000"
        Button7["justify"] = "center"
        Button7["text"] = "Slot 7"
        Button7.place(x=90,y=380,width=90,height=35)
        Button7["command"] = self.Button7_command
        
        Button9=tk.Button(root)
        Button9["bg"] = "#efefef"
        ft = tkFont.Font(family='Tahoma',size=16)
        Button9["font"] = ft
        Button9["fg"] = "#000000"
        Button9["justify"] = "center"
        Button9["text"] = "Slot 9"
        Button9.place(x=90,y=480,width=90,height=35)
        Button9["command"] = self.Button9_command

        Button4=tk.Button(root)
        Button4["bg"] = "#efefef"
        ft = tkFont.Font(family='Tahoma',size=16)
        Button4["font"] = ft
        Button4["fg"] = "#000000"
        Button4["justify"] = "center"
        Button4["text"] = "Slot 4"
        Button4.place(x=340,y=80,width=90,height=35)
        Button4["command"] = self.Button4_command

        Button5=tk.Button(root)
        Button5["bg"] = "#efefef"
        ft = tkFont.Font(family='Tahoma',size=16)
        Button5["font"] = ft
        Button5["fg"] = "#000000"
        Button5["justify"] = "center"
        Button5["text"] = "Slot 5"
        Button5.place(x=340,y=180,width=90,height=35)
        Button5["command"] = self.Button5_command

        Button6=tk.Button(root)
        Button6["bg"] = "#efefef"
        ft = tkFont.Font(family='Tahoma',size=16)
        Button6["font"] = ft
        Button6["fg"] = "#000000"
        Button6["justify"] = "center"
        Button6["text"] = "Slot 6"
        Button6.place(x=340,y=280,width=90,height=35)
        Button6["command"] = self.Button6_command
        
        
        Button8=tk.Button(root)
        Button8["bg"] = "#efefef"
        ft = tkFont.Font(family='Tahoma',size=16)
        Button8["font"] = ft
        Button8["fg"] = "#000000"
        Button8["justify"] = "center"
        Button8["text"] = "Slot 8"
        Button8.place(x=340,y=380,width=90,height=35)
        Button8["command"] = self.Button8_command
        
        Button10=tk.Button(root)
        Button10["bg"] = "#efefef"
        ft = tkFont.Font(family='Tahoma',size=16)
        Button10["font"] = ft
        Button10["fg"] = "#000000"
        Button10["justify"] = "center"
        Button10["text"] = "Slot 10"
        Button10.place(x=340,y=480,width=90,height=35)
        Button10["command"] = self.Button10_command
        
        
        
        
        
        
#Button Commands for slots

    def Button1_command(self):
        root = Toplevel()
        Availableslot=tk.Label(root)
        ft = tkFont.Font(family='Tahoma',size=16)
        Availableslot["font"] = ft
        Availableslot["fg"] = "#333333"
        Availableslot["justify"] = "center"
        Availableslot["text"] = "Slot 1 Available \n \n \n Click to reserve the spot"
        Availableslot.place(x=150,y=120,width=200,height=120)
        app_width=500
        app_height=600
        screenwidth = root.winfo_screenwidth()
        screenheight = root.winfo_screenheight()
        
        x = (screenwidth / 2) - (app_width / 2)
        y = (screenheight / 2) - (app_height / 2)
        root.geometry(f'{app_width}x{app_height}+{int(x)}+{int(y)}')
        #root.geometry("500x600")
        
        Button1A=tk.Button(root)
        Button1A["bg"] = "#efefef"
        ft = tkFont.Font(family='Tahoma',size=16)
        Button1A["font"] = ft
        Button1A["fg"] = "#000000"
        Button1A["justify"] = "center"
        Button1A["text"] = "Reserve Slot"
        Button1A.place(x=190,y=225,width=120,height=50)
        Button1A["command"] = self.Button1A_command
        
        
    def Button2_command(self):
        root = Toplevel()
        Availableslot=tk.Label(root)
        ft = tkFont.Font(family='Tahoma',size=16)
        Availableslot["font"] = ft
        Availableslot["fg"] = "#333333"
        Availableslot["justify"] = "center"
        Availableslot["text"] = "Slot 2 Available \n \n \n Click to reserve the spot"
        Availableslot.place(x=150,y=120,width=200,height=120)
        app_width=500
        app_height=600
        screenwidth = root.winfo_screenwidth()
        screenheight = root.winfo_screenheight()
        
        x = (screenwidth / 2) - (app_width / 2)
        y = (screenheight / 2) - (app_height / 2)
        root.geometry(f'{app_width}x{app_height}+{int(x)}+{int(y)}')
        #root.geometry("500x600")
        
        Button1A=tk.Button(root)
        Button1A["bg"] = "#efefef"
        ft = tkFont.Font(family='Tahoma',size=16)
        Button1A["font"] = ft
        Button1A["fg"] = "#000000"
        Button1A["justify"] = "center"
        Button1A["text"] = "Reserve Slot"
        Button1A.place(x=190,y=240,width=120,height=50)
        Button1A["command"] = self.Button1A_command


    def Button3_command(self):
        root = Toplevel()
        Availableslot=tk.Label(root)
        ft = tkFont.Font(family='Tahoma',size=16)
        Availableslot["font"] = ft
        Availableslot["fg"] = "#333333"
        Availableslot["justify"] = "center"
        Availableslot["text"] = "Slot 3 Available \n \n \n Click to reserve the spot"
        Availableslot.place(x=150,y=120,width=200,height=120)
        app_width=500
        app_height=600
        screenwidth = root.winfo_screenwidth()
        screenheight = root.winfo_screenheight()
        
        x = (screenwidth / 2) - (app_width / 2)
        y = (screenheight / 2) - (app_height / 2)
        root.geometry(f'{app_width}x{app_height}+{int(x)}+{int(y)}')
        #root.geometry("500x600")
        
        Button1A=tk.Button(root)
        Button1A["bg"] = "#efefef"
        ft = tkFont.Font(family='Tahoma',size=16)
        Button1A["font"] = ft
        Button1A["fg"] = "#000000"
        Button1A["justify"] = "center"
        Button1A["text"] = "Reserve Slot"
        Button1A.place(x=190,y=240,width=100,height=50)
        Button1A["command"] = self.Button1A_command
        

    def Button4_command(self):
        root = Toplevel()
        Availableslot=tk.Label(root)
        ft = tkFont.Font(family='Tahoma',size=16)
        Availableslot["font"] = ft
        Availableslot["fg"] = "#333333"
        Availableslot["justify"] = "center"
        Availableslot["text"] = "Slot 4 Available \n \n \n  Click to reserve the spot"
        Availableslot.place(x=150,y=120,width=200,height=120)
        app_width=500
        app_height=600
        screenwidth = root.winfo_screenwidth()
        screenheight = root.winfo_screenheight()
        
        x = (screenwidth / 2) - (app_width / 2)
        y = (screenheight / 2) - (app_height / 2)
        root.geometry(f'{app_width}x{app_height}+{int(x)}+{int(y)}')
        #root.geometry("500x600")
        
        Button1A=tk.Button(root)
        Button1A["bg"] = "#efefef"
        ft = tkFont.Font(family='Tahoma',size=16)
        Button1A["font"] = ft
        Button1A["fg"] = "#000000"
        Button1A["justify"] = "center"
        Button1A["text"] = "Reserve Slot"
        Button1A.place(x=190,y=240,width=120,height=50)
        Button1A["command"] = self.Button1A_command


    def Button5_command(self):
        root = Toplevel()
        Availableslot=tk.Label(root)
        ft = tkFont.Font(family='Tahoma',size=16)
        Availableslot["font"] = ft
        Availableslot["fg"] = "#333333"
        Availableslot["justify"] = "center"
        Availableslot["text"] = "Slot 5 Available \n \n \n  Click to reserve the spot"
        Availableslot.place(x=150,y=120,width=200,height=120)
        app_width=500
        app_height=600
        screenwidth = root.winfo_screenwidth()
        screenheight = root.winfo_screenheight()
        
        x = (screenwidth / 2) - (app_width / 2)
        y = (screenheight / 2) - (app_height / 2)
        root.geometry(f'{app_width}x{app_height}+{int(x)}+{int(y)}')
        #root.geometry("500x600")
        
        Button1A=tk.Button(root)
        Button1A["bg"] = "#efefef"
        ft = tkFont.Font(family='Tahoma',size=16)
        Button1A["font"] = ft
        Button1A["fg"] = "#000000"
        Button1A["justify"] = "center"
        Button1A["text"] = "Reserve Slot"
        Button1A.place(x=190,y=240,width=120,height=50)
        Button1A["command"] = self.Button1A_command


    def Button6_command(self):
        root = Toplevel()
        Availableslot=tk.Label(root)
        ft = tkFont.Font(family='Tahoma',size=16)
        Availableslot["font"] = ft
        Availableslot["fg"] = "#333333"
        Availableslot["justify"] = "center"
        Availableslot["text"] = "Slot 6 Available \n \n \n  Click to reserve the spot"
        Availableslot.place(x=150,y=120,width=200,height=120)
        app_width=500
        app_height=600
        screenwidth = root.winfo_screenwidth()
        screenheight = root.winfo_screenheight()
        
        x = (screenwidth / 2) - (app_width / 2)
        y = (screenheight / 2) - (app_height / 2)
        root.geometry(f'{app_width}x{app_height}+{int(x)}+{int(y)}')
        #root.geometry("500x600")
        
        Button1A=tk.Button(root)
        Button1A["bg"] = "#efefef"
        ft = tkFont.Font(family='Tahoma',size=16)
        Button1A["font"] = ft
        Button1A["fg"] = "#000000"
        Button1A["justify"] = "center"
        Button1A["text"] = "Reserve Slot"
        Button1A.place(x=190,y=240,width=120,height=50)
        Button1A["command"] = self.Button1A_command
        #Menu.destroy(self)
        
    def Button7_command(self):
        root = Toplevel()
        Availableslot=tk.Label(root)
        ft = tkFont.Font(family='Tahoma',size=16)
        Availableslot["font"] = ft
        Availableslot["fg"] = "#333333"
        Availableslot["justify"] = "center"
        Availableslot["text"] = "Slot 7 Available \n \n \n  Click to reserve the spot"
        Availableslot.place(x=150,y=120,width=200,height=120)
        app_width=500
        app_height=600
        screenwidth = root.winfo_screenwidth()
        screenheight = root.winfo_screenheight()
        
        x = (screenwidth / 2) - (app_width / 2)
        y = (screenheight / 2) - (app_height / 2)
        root.geometry(f'{app_width}x{app_height}+{int(x)}+{int(y)}')
        #root.geometry("500x600")
        
        Button1A=tk.Button(root)
        Button1A["bg"] = "#efefef"
        ft = tkFont.Font(family='Tahoma',size=16)
        Button1A["font"] = ft
        Button1A["fg"] = "#000000"
        Button1A["justify"] = "center"
        Button1A["text"] = "Reserve Slot"
        Button1A.place(x=190,y=240,width=120,height=50)
        Button1A["command"] = self.Button1A_command
        #Menu.destroy(self)
        
    def Button8_command(self):
        root = Toplevel()
        Availableslot=tk.Label(root)
        ft = tkFont.Font(family='Tahoma',size=16)
        Availableslot["font"] = ft
        Availableslot["fg"] = "#333333"
        Availableslot["justify"] = "center"
        Availableslot["text"] = "Slot 8 Available \n \n \n  Click to reserve the spot"
        Availableslot.place(x=150,y=120,width=200,height=120)
        app_width=500
        app_height=600
        screenwidth = root.winfo_screenwidth()
        screenheight = root.winfo_screenheight()
        
        x = (screenwidth / 2) - (app_width / 2)
        y = (screenheight / 2) - (app_height / 2)
        root.geometry(f'{app_width}x{app_height}+{int(x)}+{int(y)}')
        #root.geometry("500x600")
        
        Button1A=tk.Button(root)
        Button1A["bg"] = "#efefef"
        ft = tkFont.Font(family='Tahoma',size=16)
        Button1A["font"] = ft
        Button1A["fg"] = "#000000"
        Button1A["justify"] = "center"
        Button1A["text"] = "Reserve Slot"
        Button1A.place(x=190,y=240,width=120,height=50)
        Button1A["command"] = self.Button1A_command
        #Menu.destroy(self)
        
        
        
    def Button9_command(self):
        root = Toplevel()
        Availableslot=tk.Label(root)
        ft = tkFont.Font(family='Tahoma',size=16)
        Availableslot["font"] = ft
        Availableslot["fg"] = "#333333"
        Availableslot["justify"] = "center"
        Availableslot["text"] = "Slot 9 Available \n \n \n  Click to reserve the spot"
        Availableslot.place(x=150,y=120,width=200,height=120)
        app_width=500
        app_height=600
        screenwidth = root.winfo_screenwidth()
        screenheight = root.winfo_screenheight()
        
        x = (screenwidth / 2) - (app_width / 2)
        y = (screenheight / 2) - (app_height / 2)
        root.geometry(f'{app_width}x{app_height}+{int(x)}+{int(y)}')
        #.geometry("500x600")
        
        Button1A=tk.Button(root)
        Button1A["bg"] = "#efefef"
        ft = tkFont.Font(family='Tahoma',size=16)
        Button1A["font"] = ft
        Button1A["fg"] = "#000000"
        Button1A["justify"] = "center"
        Button1A["text"] = "Reserve Slot"
        Button1A.place(x=190,y=240,width=120,height=50)
        Button1A["command"] = self.Button1A_command
        #Menu.destroy(self)
        
        
    def Button10_command(self):
        root = Toplevel()
        Availableslot=tk.Label(root)
        ft = tkFont.Font(family='Tahoma',size=16)
        Availableslot["font"] = ft
        Availableslot["fg"] = "#333333"
        Availableslot["justify"] = "center"
        Availableslot["text"] = "Slot 10 Available \n \n \n  Click to reserve the spot"
        Availableslot.place(x=150,y=120,width=200,height=120)
        app_width=500
        app_height=600
        screenwidth = root.winfo_screenwidth()
        screenheight = root.winfo_screenheight()
        
        x = (screenwidth / 2) - (app_width / 2)
        y = (screenheight / 2) - (app_height / 2)
        root.geometry(f'{app_width}x{app_height}+{int(x)}+{int(y)}')
        #root.geometry("500x600")
        
        Button1A=tk.Button(root)
        Button1A["bg"] = "#efefef"
        ft = tkFont.Font(family='Tahoma',size=16)
        Button1A["font"] = ft
        Button1A["fg"] = "#000000"
        Button1A["justify"] = "center"
        Button1A["text"] = "Reserve Slot"
        Button1A.place(x=190,y=240,width=120,height=50)
        Button1A["command"] = self.Button1A_command
        
        
#Billing for Customer
    
    def Button1A_command(self):
        root = Toplevel()
        
        global f_name
        global l_name
        global address
        global contact_number
        
        f_name = Entry(root, width=30)
        f_name.place(x=180,y=55,width=250,height=30)
        l_name = Entry(root, width=30)
        l_name.place(x=180,y=95,width=250,height=30)
        address = Entry(root, width=30)
        address.place(x=180,y=135,width=250,height=30)
        contact_number = Entry(root, width=30)
        contact_number.place(x=180,y=175,width=250,height=30)
    
        f_name_label = Label(root, text="First Name:")
        f_name_label.place(x=50,y=40,width=100,height=60)
        l_name_label = Label(root, text="Last Name:")
        l_name_label.place(x=50,y=80,width=100,height=60)
        address_label = Label(root, text="Address:")
        address_label.place(x=50,y=120,width=100,height=60)
        contact_number_label = Label(root, text="Contact Number:")
        contact_number_label.place(x=50,y=160,width=120,height=60)
    
        submit_btn = Button(root, text="Submit", command=menu.submit)
        submit_btn.place(x=200,y=220,width=100,height=40)
        
        app_width=500
        app_height=600
        screenwidth = root.winfo_screenwidth()
        screenheight = root.winfo_screenheight()
        
        x = (screenwidth / 2) - (app_width / 2)
        y = (screenheight / 2) - (app_height / 2)
        root.geometry(f'{app_width}x{app_height}+{int(x)}+{int(y)}')
        #root.geometry("500x600")
    
    def submit(self):
        
        final = Toplevel()
        app_width=500
        app_height=600
        screenwidth = root.winfo_screenwidth()
        screenheight = root.winfo_screenheight()
        
        x = (screenwidth / 2) - (app_width / 2)
        y = (screenheight / 2) - (app_height / 2)
        final.geometry(f'{app_width}x{app_height}+{int(x)}+{int(y)}')
        
        
        Label(final, text="Thank you for reserving with iParking!").pack(ipadx=30, ipady=50)
        Button(final, text="Exit Program", command = menu.end).pack()
        
        now = datetime.datetime.now()
        time_start = now.strftime("%Y-%m-%d %H:%M:%S")
        
        conn = sqlite3.connect('iPark.db')
        c = conn.cursor()
        c.execute("INSERT INTO user VALUES (:f_name, :l_name, :address, :contact_number)",
                  {
                      'f_name': f_name.get(),
                      'l_name': l_name.get(),
                      'address': address.get(),
                      'contact_number': contact_number.get()
                
                  }    
                )
        
        c.execute("INSERT INTO reservation VALUES (:f_name, :l_name, :address, :contact_number, :time_start)",
                  {
                      'f_name': f_name.get(),
                      'l_name': l_name.get(),
                      'address': address.get(),
                      'contact_number': contact_number.get(),
                      'time_start' : time_start
                  }    
                )
        
        f_name.delete(0,END)
        l_name.delete(0,END)
        address.delete(0,END)
        contact_number.delete(0,END)
        
        conn.commit()
        conn.close()

    
    
    def end(self):
        root.destroy()
        
#Inside the Administration

    def admin_menu():
        global menu_admin
        
        menu_admin = Toplevel()
        app_width=500
        app_height=600
        screenwidth = root.winfo_screenwidth()
        screenheight = root.winfo_screenheight()
        
        x = (screenwidth / 2) - (app_width / 2)
        y = (screenheight / 2) - (app_height / 2)
        menu_admin.geometry(f'{app_width}x{app_height}+{int(x)}+{int(y)}')
        #menu_admin.geometry("500x600")
        
        Label(menu_admin, text = "Administration Menu:").pack()
        Button(menu_admin, text = "View Record/s", command = menu.query_window).pack()
        Button(menu_admin, text = "Delete Record/s", command = menu.delete_window).pack()
        Button(menu_admin, text = "Update Record/s", command = menu.edit).pack()
        
    def query_window(self):
        global window_query
        
        window_query = Toplevel()
        app_width=500
        app_height=600
        screenwidth = root.winfo_screenwidth()
        screenheight = root.winfo_screenheight()
        
        x = (screenwidth / 2) - (app_width / 2)
        y = (screenheight / 2) - (app_height / 2)
        window_query.geometry(f'{app_width}x{app_height}+{int(x)}+{int(y)}')
       # window_query.geometry("500x600")
        
        Button(window_query, text = "Press to show customers", command = menu.query).pack()

    def query(self): 
        conn = sqlite3.connect('iPark.db')
        c = conn.cursor()
        
        c.execute("SELECT *, oid FROM reservation")
        records = c.fetchall()
        
        print_records = ''
        for record in records:
            print_records += str(record[0]) + " " + str(record[1]) + "\t" + str(record[4]) + "\t" + str(record[5]) + "\n"
        
        query_label = Label(window_query, text=print_records).pack()
        
        conn.commit()
        conn.close()
    
    def delete_window_update(self):
        c.execute("SELECT *, oid FROM reservation")
        records = c.fetchall()        
        print_records = ''
        for record in records:
            print_records += str(record[5]) + "\t" + str(record) + "\n"
        query_label = Label(window_delete, text=print_records)
        query_label.place(x=10,y=70,width=480,height=200)

    def delete(self):
        conn = sqlite3.connect('iPark.db')
        c = conn.cursor()
        
        c.execute("DELETE from history WHERE oid = " + delete_entry.get())
        
        conn.commit()
        conn.close()  
    
    def delete_window(self):
        global window_delete
        
        window_delete = Toplevel()
        app_width=500
        app_height=600
        screenwidth = root.winfo_screenwidth()
        screenheight = root.winfo_screenheight()
        
        x = (screenwidth / 2) - (app_width / 2)
        y = (screenheight / 2) - (app_height / 2)
        window_delete.geometry(f'{app_width}x{app_height}+{int(x)}+{int(y)}')
        #window_delete.geometry("500x600")
        
        global delete_entry
        
        delete_label = Label(window_delete, text="Input Record ID for deletion:")
        delete_label.place(x=20,y=15,width=200,height=30)
        delete_entry = Entry(window_delete)
        delete_entry.place(x=220,y=12,width=200,height=30)
        
        delete_record = Button(window_delete, text = "Delete Record", command = menu.delete)
        delete_record.place(x=120,y=50,width=120,height=30)
        update_record = Button(window_delete, text = "Update", command = menu.delete_window_update)
        update_record.place(x=270,y=50,width=120,height=30)
    
    #UPDATE
    
    
        
        
    def edit(self):
        
        conn = sqlite3.connect('iPark.db')
        c = conn.cursor()        
        
        global editor
        editor = Toplevel()
        
        global update
        
        global f_name
        global l_name
        global address
        global contact_number
        global select_id

    
        select_id_label = Label(editor, text="UPDATE")
        select_id_label.place(x=200,y=10,width=100,height=30)
        select_id_label = Label(editor, text="Input ID Number: ")
        select_id_label.place(x=17,y=40,width=120,height=20)
        select_id = Entry(editor, width=10)
        select_id.place(x=140,y=40,width=250,height=30)
        select_id_button = Button(editor, text = "Check", command = menu.update)
        select_id_button.place(x=400,y=40,width=70,height=30)
        
        
    def edit_window(self):
        global editor
        editor = Toplevel()
        
        app_width=500
        app_height=600
        screenwidth = root.winfo_screenwidth()
        screenheight = root.winfo_screenheight()
        
        x = (screenwidth / 2) - (app_width / 2)
        y = (screenheight / 2) - (app_height / 2)
        edit_window.geometry(f'{app_width}x{app_height}+{int(x)}+{int(y)}')
        
        
        
        
        
    

    def update_history(self):
        conn = sqlite3.connect('iPark.db')
        c = conn.cursor()

        record_id = select_id.get()
        c.execute("""UPDATE user SET
                  first_name = :first,
                  last_name = :last,
                  address = :address,
                  contact_number = :contact_number
                  
                  WHERE oid = :oid""",
                  {
                   'first': f_name_editor.get(),
                   'last': l_name_editor.get(),
                   'address': address_editor.get(),
                   'contact_number': contact_number_editor.get(),
                   
                   'oid': record_id
                   }
                  )

        f_name_editor.delete(0,END)        
        l_name_editor.delete(0,END)
        address_editor.delete(0,END)
        contact_number_editor.delete(0,END)
        
        conn.commit()
        conn.close()
        
    def update(self):
        conn = sqlite3.connect('iPark.db')
        c = conn.cursor()
        
        global updated
        
        global f_name
        global l_name
        global address
        global contact_number
        
        f_name_updated = Entry(editor, width=30)
        f_name_updated.place(x=140,y=90,width=250,height=30)
        l_name_updated = Entry(editor, width=30)
        l_name_updated.place(x=140,y=130,width=250,height=30)
        address_updated = Entry(editor, width=30)
        address_updated.place(x=140,y=170,width=250,height=30)
        contact_number_updated = Entry(editor, width=30)
        contact_number_updated.place(x=140,y=210,width=250,height=30)
    
        f_name_label_editor = Label(editor, text="First Name:")
        f_name_label_editor.place(x=15,y=75,width=100,height=60)
        l_name_label_editor = Label(editor, text="Last Name:")
        l_name_label_editor.place(x=15,y=115,width=100,height=60)
        address_label_editor = Label(editor, text="Address:")
        address_label_editor.place(x=15,y=155,width=100,height=60)
        contact_number_label_editor = Label(editor, text="Contact Number:")
        contact_number_label_editor.place(x=15,y=195,width=110,height=60)    
        
        idrecord = select_id.get()
        
        c.execute("SELECT * FROM user WHERE oid = " + idrecord)
        records = c.fetchall()
        
        global f_name_editor
        global l_name_editor
        global address_editor
        global contact_number_editor
        
      
    
        
        
        f_name_editor = Entry(editor, width=30)
        f_name_editor.place(x=140,y=90,width=250,height=30)
        l_name_editor = Entry(editor, width=30)
        l_name_editor.place(x=140,y=130,width=250,height=30)
        address_editor = Entry(editor, width=30)
        address_editor.place(x=140,y=170,width=250,height=30)
        contact_number_editor = Entry(editor, width=30)
        contact_number_editor.place(x=140,y=210,width=250,height=30)
    
        f_name_label_editor = Label(editor, text="First Name:")
        f_name_label_editor.place(x=15,y=75,width=100,height=60)
        l_name_label_editor = Label(editor, text="Last Name:")
        l_name_label_editor.place(x=15,y=115,width=100,height=60)
        address_label_editor = Label(editor, text="Address:")
        address_label_editor.place(x=15,y=155,width=100,height=60)
        contact_number_label_editor = Label(editor, text="Contact Number:")
        contact_number_label_editor.place(x=15,y=195,width=110,height=60)
        
        for record in records:
            f_name_editor.insert(0, record[0])
            l_name_editor.insert(0, record[1])
            address_editor.insert(0, record[2])
            contact_number_editor.insert(0, record[3])
        
        update_btn = Button(editor, text="Update", command=menu.update_history)
        update_btn.place(x=150,y=270,width=200,height=30)
        
        conn.commit()
        conn.close()
        
        
        def edit_window(self):
            global editor
            editor = Toplevel()
            
            app_width=500
            app_height=600
            screenwidth = root.winfo_screenwidth()
            screenheight = root.winfo_screenheight()
            
            x = (screenwidth / 2) - (app_width / 2)
            y = (screenheight / 2) - (app_height / 2)
            edit_window.geometry(f'{app_width}x{app_height}+{int(x)}+{int(y)}')
        
#ADMINISTRATOR

    def main_screen(self):
        global mainscreen

        mainscreen = Toplevel()
        app_width=500
        app_height=600
        screenwidth = root.winfo_screenwidth()
        screenheight = root.winfo_screenheight()
        
        x = (screenwidth / 2) - (app_width / 2)
        y = (screenheight / 2) - (app_height / 2)
        mainscreen.geometry(f'{app_width}x{app_height}+{int(x)}+{int(y)}')
        #mainscreen.geometry("500x600")
        
        
        ft = tkFont.Font(family='Tahoma',size=26)
        main1 = Label(mainscreen, text = "ADMINISTRATOR")
        #main1.place(x=140,y=55,width=250,height=30)
        main1.pack(ipadx=30, ipady=30)
      
        Button(mainscreen, text = "LOGIN", command=Menu.user_login).pack()
        Button(mainscreen, text = "REGISTER", command=Menu.user_register).pack()
        
        mainscreen.mainloop()
        
    


        
        
        #
        
    def user_register():
        global register
        
        register = Toplevel(mainscreen)
        app_width=500
        app_height=600
        screenwidth = root.winfo_screenwidth()
        screenheight = root.winfo_screenheight()
        
        x = (screenwidth / 2) - (app_width / 2)
        y = (screenheight / 2) - (app_height / 2)
        register.geometry(f'{app_width}x{app_height}+{int(x)}+{int(y)}')
        #register.geometry("500x600")
        
        global username
        global password
        global inputuser
        global inputpass
        
        username = StringVar()
        password = StringVar()
        
        Label(register, text="Username:").pack()
        inputuser = Entry(register)
        inputuser.pack()
        
        Label(register, text="Password:").pack()
        inputpass = Entry(register)
        inputpass.pack()
                
        Button(register, text = "Register", command = Menu.register_user).pack()
        
        
    def register_user():
        
         
         conn = sqlite3.connect('iPark.db')
         c = conn.cursor()
         c.execute("INSERT INTO admin VALUES (:inputuser, :inputpass)",
                   {
                       'inputuser': inputuser.get(),
                       'inputpass': inputpass.get()
                   }    
                 )
     
         
         inputuser.delete(0,END)
         inputpass.delete(0, END)
         conn.commit()
         conn.close()
         
         Label(register, text = "Registration Complete!", fg = "green").pack()

    def user_login():
        global login
        login = Toplevel(mainscreen)
        app_width=500
        app_height=600
        screenwidth = root.winfo_screenwidth()
        screenheight = root.winfo_screenheight()
        
        x = (screenwidth / 2) - (app_width / 2)
        y = (screenheight / 2) - (app_height / 2)
        login.geometry(f'{app_width}x{app_height}+{int(x)}+{int(y)}')
        #login.geometry("500x600")
        
        global username_verify
        global password_verify
        global username_entry1
        global password_entry1
        
        username_verify = StringVar()
        password_verify = StringVar()
        
        Label(login, text="Username:").pack()
        username_entry1 = Entry(login, textvariable = username_verify)
        username_entry1.pack()
        
        Label(login, text="Password:").pack()
        password_entry1 = Entry(login, textvariable = password_verify)
        password_entry1.pack()
        
        Button(login, text = "Login", command = Menu.login_verify).pack()
        
        

    def login_verify():
      
        username1 = username_verify.get()
        password1 = password_verify.get()
        username_entry1.delete(0, END)
        password_entry1.delete(0, END)

        list_of_files = os.listdir()
        if username1 in list_of_files:
          file1 = open(username1, "r")
          verify = file1.read().splitlines()
          if password1 in verify:
             Menu.admin_menu()
          else:
             Menu.fail_pass()
        else:
             Menu.fail_user()
        
    def login_success_destroy():
        success_login.destroy()

    def fail_pass():
        global pass_fail
        
        pass_fail = Toplevel(mainscreen)
        app_width=500
        app_height=600
        screenwidth = root.winfo_screenwidth()
        screenheight = root.winfo_screenheight()
        
        x = (screenwidth / 2) - (app_width / 2)
        y = (screenheight / 2) - (app_height / 2)
        pass_fail.geometry(f'{app_width}x{app_height}+{int(x)}+{int(y)}')
        #pass_fail.geometry("500x600")

        Label(pass_fail, text = "Invalid Password.").pack() 
        Button(pass_fail, text = "OK", command = Menu.pass_fail_destroy).pack()    
        
    def pass_fail_destroy():
        pass_fail.destroy()

    def fail_user():
        global user_fail
        
        user_fail = Toplevel(mainscreen)
        app_width=500
        app_height=600
        screenwidth = root.winfo_screenwidth()
        screenheight = root.winfo_screenheight()
        
        x = (screenwidth / 2) - (app_width / 2)
        y = (screenheight / 2) - (app_height / 2)
        user_fail.geometry(f'{app_width}x{app_height}+{int(x)}+{int(y)}')
        #user_fail.geometry("500x600")

        Label(user_fail, text = "User does not exist.").pack(ipadx=30, ipady=30)
        Button(user_fail, text = "OK", command = Menu.user_fail_destroy).pack()    
        
    def user_fail_destroy():
        user_fail.destroy()


        

if __name__ == "__main__":
    root = tk.Tk()
    menu = Menu(root)
    root.mainloop()