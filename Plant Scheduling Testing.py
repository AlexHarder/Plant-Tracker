import tkinter as tk
from tkinter import messagebox
import tkinter.ttk as ttk
import sqlite3 as sql
import datetime as dt


class PlantTracker(tk.Tk):
    def __init__(self, *args, **kwargs):

        tk.Tk.__init__(self, *args, **kwargs)
        tk.Tk.wm_title(self, 'Plant Tracker')

        container = tk.Frame(self)
        container.pack(side='top', fill='both', expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}

        for F in (StartPage, Table1, Table2, Table3, Table4, Table5, Table6,
                  Table7, Table8, Table9, Table10, Table11, Table12, Table13,
                  Table14, Table15, Table16, Table17, Table18, Table19,
                  Table20, Table21, Table22, Table23, Table24):

            frame = F(container, self)

            self.frames[F] = frame

            frame.grid(row=0, column=0, sticky='nsew')

            self.show_frame(StartPage)

    def show_frame(self, cont):

        frame = self.frames[cont]
        frame.tkraise()


class StartPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        greenhouse_1 = tk.Label(self, text='Greenhouse', font=(
            'Verdana 19 bold'), bg='lime green', relief='raised',
            borderwidth=4)
        greenhouse_1.grid(row=0, column=2, columnspan=2)

        # Setting the Table Buttons
        table1 = tk.Button(self, text='Table 1', borderwidth=2,
                           relief='raised', bg='lime green',
                           command=lambda: controller.show_frame(Table1))
        table2 = tk.Button(self, text='Table 2', borderwidth=2,
                           relief='raised', bg='lime green',
                           command=lambda: controller.show_frame(Table2))
        table3 = tk.Button(self, text='Table 3', borderwidth=2,
                           relief='raised', bg='lime green',
                           command=lambda: controller.show_frame(Table3))
        table4 = tk.Button(self, text='Table 4', borderwidth=2,
                           relief='raised', bg='lime green',
                           command=lambda: controller.show_frame(Table4))
        table5 = tk.Button(self, text='Table 5', borderwidth=2,
                           relief='raised', bg='lime green',
                           command=lambda: controller.show_frame(Table5))
        table6 = tk.Button(self, text='Table 6', borderwidth=2,
                           relief='raised', bg='lime green',
                           command=lambda: controller.show_frame(Table6))
        table7 = tk.Button(self, text='Table 7', borderwidth=2,
                           relief='raised', bg='lime green',
                           command=lambda: controller.show_frame(Table7))
        table8 = tk.Button(self, text='Table 8', borderwidth=2,
                           relief='raised', bg='lime green',
                           command=lambda: controller.show_frame(Table8))
        table9 = tk.Button(self, text='Table 9', borderwidth=2,
                           relief='raised', bg='lime green',
                           command=lambda: controller.show_frame(Table9))
        table10 = tk.Button(self, text='Table 10', borderwidth=2,
                            relief='raised', bg='lime green',
                            command=lambda: controller.show_frame(Table10))
        table11 = tk.Button(self, text='Table 11', borderwidth=2,
                            relief='raised', bg='lime green',
                            command=lambda: controller.show_frame(Table11))
        table12 = tk.Button(self, text='Table 12', borderwidth=2,
                            relief='raised', bg='lime green',
                            command=lambda: controller.show_frame(Table12))
        table13 = tk.Button(self, text='Table 13', borderwidth=2,
                            relief='raised', bg='lime green',
                            command=lambda: controller.show_frame(Table13))
        table14 = tk.Button(self, text='Table 14', borderwidth=2,
                            relief='raised', bg='lime green',
                            command=lambda: controller.show_frame(Table14))
        table15 = tk.Button(self, text='Table 15', borderwidth=2,
                            relief='raised', bg='lime green',
                            command=lambda: controller.show_frame(Table15))
        table16 = tk.Button(self, text='Table 16', borderwidth=2,
                            relief='raised', bg='lime green',
                            command=lambda: controller.show_frame(Table16))
        table17 = tk.Button(self, text='Table 17', borderwidth=2,
                            relief='raised', bg='lime green',
                            command=lambda: controller.show_frame(Table17))
        table18 = tk.Button(self, text='Table 18', borderwidth=2,
                            relief='raised', bg='lime green',
                            command=lambda: controller.show_frame(Table18))
        table19 = tk.Button(self, text='Table 19', borderwidth=2,
                            relief='raised', bg='lime green',
                            command=lambda: controller.show_frame(Table19))
        table20 = tk.Button(self, text='Table 20', borderwidth=2,
                            relief='raised', bg='lime green',
                            command=lambda: controller.show_frame(Table20))
        table21 = tk.Button(self, text='Table 21', borderwidth=2,
                            relief='raised', bg='lime green',
                            command=lambda: controller.show_frame(Table21))
        table22 = tk.Button(self, text='Table 22', borderwidth=2,
                            relief='raised', bg='lime green',
                            command=lambda: controller.show_frame(Table22))
        table23 = tk.Button(self, text='Table 23', borderwidth=2,
                            relief='raised', bg='lime green',
                            command=lambda: controller.show_frame(Table23))
        table24 = tk.Button(self, text='Table 24', borderwidth=2,
                            relief='raised', bg='lime green',
                            command=lambda: controller.show_frame(Table24))

        # Place Buttons(Tables) in Screen(self)
        table1.grid(row=1, column=0, ipadx=8, ipady=45,
                    padx=10, pady=10, sticky='nsew')
        table2.grid(row=1, column=1, ipadx=8, ipady=45,
                    padx=10, pady=10, sticky='nsew')
        table3.grid(row=1, column=2, ipadx=8, ipady=45,
                    padx=10, pady=10, sticky='nsew')
        table4.grid(row=1, column=3, ipadx=8, ipady=45,
                    padx=10, pady=10, sticky='nsew')
        table5.grid(row=1, column=4, ipadx=8, ipady=45,
                    padx=10, pady=10, sticky='nsew')
        table6.grid(row=1, column=5, ipadx=8, ipady=45,
                    padx=10, pady=10, sticky='nsew')
        table7.grid(row=2, column=0, ipadx=8, ipady=45,
                    padx=10, pady=10, sticky='nsew')
        table8.grid(row=2, column=1, ipadx=8, ipady=45,
                    padx=10, pady=10, sticky='nsew')
        table9.grid(row=2, column=2, ipadx=8, ipady=45,
                    padx=10, pady=10, sticky='nsew')
        table10.grid(row=2, column=3, ipadx=8, ipady=45,
                     padx=10, pady=10, sticky='nsew')
        table11.grid(row=2, column=4, ipadx=8, ipady=45,
                     padx=10, pady=10, sticky='nsew')
        table12.grid(row=2, column=5, ipadx=8, ipady=45,
                     padx=10, pady=10, sticky='nsew')
        table13.grid(row=3, column=0, ipadx=8, ipady=45,
                     padx=10, pady=10, sticky='nsew')
        table14.grid(row=3, column=1, ipadx=8, ipady=45,
                     padx=10, pady=10, sticky='nsew')
        table15.grid(row=3, column=2, ipadx=8, ipady=45,
                     padx=10, pady=10, sticky='nsew')
        table16.grid(row=3, column=3, ipadx=8, ipady=45,
                     padx=10, pady=10, sticky='nsew')
        table17.grid(row=3, column=4, ipadx=8, ipady=45,
                     padx=10, pady=10, sticky='nsew')
        table18.grid(row=3, column=5, ipadx=8, ipady=45,
                     padx=10, pady=10, sticky='nsew')
        table19.grid(row=4, column=0, ipadx=8, ipady=45,
                     padx=10, pady=10, sticky='nsew')
        table20.grid(row=4, column=1, ipadx=8, ipady=45,
                     padx=10, pady=10, sticky='nsew')
        table21.grid(row=4, column=2, ipadx=8, ipady=45,
                     padx=10, pady=10, sticky='nsew')
        table22.grid(row=4, column=3, ipadx=8, ipady=45,
                     padx=10, pady=10, sticky='nsew')
        table23.grid(row=4, column=4, ipadx=8, ipady=45,
                     padx=10, pady=10, sticky='nsew')
        table24.grid(row=4, column=5, ipadx=8, ipady=45,
                     padx=10, pady=10, sticky='nsew')


class Table1(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        def connect():
            conn = sql.connect("Table 1.db")
            cur = conn.cursor()
            cur.execute("""CREATE TABLE IF NOT EXISTS profile
                       (id INTEGER PRIMARY KEY, Name TEXT, Planted TEXT,
                       Harvested TEXT)""")
            conn.commit()
            conn.close()

        def View():
            conn = sql.connect("Table 1.db")
            cur = conn.cursor()
            for i in tree.get_children():
                tree.delete(i)
            cur.execute("SELECT * FROM profile ORDER BY id DESC")
            rows = cur.fetchall()
            for row in rows:
                print(row)  # it print all records in the database
                tree.insert("", tk.END, values=row)
            conn.close()

        def insert():
            Planted_i = Planted.get()
            Name_i = Name.get()

            def pop_up():
                messagebox.showerror('Error', 'Please select a name.')
                insert_window()

            if Name_i == 'Select Name':
                print('error')
                pop_up()
            else:

                conn = sql.connect("Table 1.db")
                with conn:
                    cur = conn.cursor()
                    cur.execute('''INSERT INTO profile(Name, Planted)
                    VALUES(?, ?)''', (Name_i, Planted_i))
                    lis = cur.execute(
                        'SELECT Name, Planted, Harvested FROM profile')
                    for item in lis:
                        list.insert(tk.END, item)
                conn.close()
                Name.set('Select Name')

        def insert_window():
            inwin = tk.Toplevel()
            inwin.title('Insert')
            inwin.grab_set()
            inwin.focus()
            now = dt.date.today()
            now = now.strftime('%d/%m/%Y')
            Planted.set(now)

            de = tk.OptionMenu(inwin, Name, 'Albahaca', 'Rucula',
                               'Perejil', 'Lechuga', 'Morada', 'Mantecosa')
            pe = tk.Entry(inwin, textvariable=Planted)
            pe_en = tk.Label(inwin, text='Planted')
            de_en = tk.Label(inwin, text='Name')

            button = tk.Button(inwin, text='Insert',
                               command=lambda: [insert(), View(),
                                                close_window()])

            inwin.bind('<Return>', lambda x: [insert(), View(),
                                              close_window()])

            de.grid(row=0, column=1)
            de.configure(takefocus=1)

            pe.grid(row=1, column=1)
            de_en.grid(row=0)
            pe_en.grid(row=1)
            button.grid(row=4, column=1)

            def close_window():
                inwin.destroy()

        def clear():
            conn = sql.connect("Table 1.db")
            cur = conn.cursor()
            cur.execute('DELETE FROM profile')
            conn.commit()
            conn.close()

        def clear_screen():
            for i in tree.get_children():
                tree.delete(i)

        def update_harvested():
            Harvested_i = Harvested.get()
            id_i = id.get()

            conn = sql.connect("Table 1.db")
            cur = conn.cursor()
            cur.execute('''UPDATE profile SET Harvested = ?
                        WHERE id = ?''', (Harvested_i, id_i))
            conn.commit()
            conn.close()

        def insert_window_harvested():
            inwin = tk.Toplevel()
            inwin.title('Insert')
            inwin.grab_set()
            inwin.focus()
            now = dt.date.today()
            now = now.strftime('%d/%m/%Y')
            Harvested.set(now)

            conn = sql.connect("Table 1.db")
            cur = conn.cursor()
            cur.execute('SELECT MAX(id) AS TEXT FROM profile')
            ID = cur.fetchone()[0]

            id.set(ID)

            se = tk.Entry(inwin, textvariable=Harvested)
            de = tk.Entry(inwin, textvariable=id)
            se_en = tk.Label(inwin, text='Harvested')
            de_en = tk.Label(inwin, text='Id')

            button = tk.Button(
                inwin, text='Insert', command=lambda: [update_harvested(),
                                                       close_window(), View()])

            inwin.bind('<Return>', lambda x: [update_harvested(),
                                              close_window(), View()])

            se.grid(row=2, column=1)
            de.grid(row=0, column=1)
            se_en.grid(row=2)
            de_en.grid(row=0)
            button.grid(row=4, column=1)

            def close_window():
                inwin.destroy()

        connect()  # this to create the db

        list = tk.Listbox(self)

        Planted = tk.StringVar()
        Harvested = tk.StringVar()
        Name = tk.StringVar()
        Name.set('Select Name')
        id = tk.StringVar()

        tree = ttk.Treeview(self, column=(
            'column1', 'column2', 'column3', 'column4'), show='headings')
        tree.column('#1', stretch=True, width=40)
        tree.heading("#1", text="Id")
        tree.column('#2', stretch=True, width=105)
        tree.heading("#2", text="Name")
        tree.column('#3', stretch=True, width=200)
        tree.heading("#3", text="Planted")
        tree.column('#4', stretch=True, width=200)
        tree.heading("#4", text="Harvested")

        tree.grid(row=0, sticky='n')
        View()

        back_button = tk.Button(self, text='Greenhouse',
                                command=lambda:
                                controller.show_frame(StartPage))
        back_button.grid(row=1, sticky='se')

        ibutton = tk.Button(self, text='Planted', command=insert_window)
        ibutton.grid(row=1, sticky='sw')

        ibutton_update = tk.Button(
            self, text='Harvested', command=insert_window_harvested)
        ibutton_update.grid(row=2, sticky='sw')

        clear_button = tk.Button(
            self, text='Clear ALL Data', command=clear)
        clear_button.grid(row=2, sticky='se')


class Table2(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text='Table 2')
        label.pack()

        back_button = tk.Button(self, text='Greenhouse',
                                command=lambda:
                                controller.show_frame(StartPage))
        back_button.pack()


class Table3(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text='Table 3')
        label.pack()

        back_button = tk.Button(self, text='Greenhouse',
                                command=lambda:
                                controller.show_frame(StartPage))
        back_button.pack()


class Table4(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text='Table 4')
        label.pack()

        back_button = tk.Button(self, text='Greenhouse',
                                command=lambda:
                                controller.show_frame(StartPage))
        back_button.pack()


class Table5(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text='Table 5')
        label.pack()

        back_button = tk.Button(self, text='Greenhouse',
                                command=lambda:
                                controller.show_frame(StartPage))
        back_button.pack()


class Table6(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text='Table 6')
        label.pack()

        back_button = tk.Button(self, text='Greenhouse',
                                command=lambda:
                                controller.show_frame(StartPage))
        back_button.pack()


class Table7(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text='Table 7')
        label.pack()

        back_button = tk.Button(self, text='Greenhouse',
                                command=lambda:
                                controller.show_frame(StartPage))
        back_button.pack()


class Table8(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text='Table 8')
        label.pack()

        back_button = tk.Button(self, text='Greenhouse',
                                command=lambda:
                                controller.show_frame(StartPage))
        back_button.pack()


class Table9(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text='Table 9')
        label.pack()

        back_button = tk.Button(self, text='Greenhouse',
                                command=lambda:
                                controller.show_frame(StartPage))
        back_button.pack()


class Table10(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text='Table 10')
        label.pack()

        back_button = tk.Button(self, text='Greenhouse',
                                command=lambda:
                                controller.show_frame(StartPage))
        back_button.pack()


class Table11(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text='Table 11')
        label.pack()

        back_button = tk.Button(self, text='Greenhouse',
                                command=lambda:
                                controller.show_frame(StartPage))
        back_button.pack()


class Table12(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text='Table 12')
        label.pack()

        back_button = tk.Button(self, text='Greenhouse',
                                command=lambda:
                                controller.show_frame(StartPage))
        back_button.pack()


class Table13(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text='Table 13')
        label.pack()

        back_button = tk.Button(self, text='Greenhouse',
                                command=lambda:
                                controller.show_frame(StartPage))
        back_button.pack()


class Table14(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text='Table 14')
        label.pack()

        back_button = tk.Button(self, text='Greenhouse',
                                command=lambda:
                                controller.show_frame(StartPage))
        back_button.pack()


class Table15(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text='Table 15')
        label.pack()

        back_button = tk.Button(self, text='Greenhouse',
                                command=lambda:
                                controller.show_frame(StartPage))
        back_button.pack()


class Table16(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text='Table 16')
        label.pack()

        back_button = tk.Button(self, text='Greenhouse',
                                command=lambda:
                                controller.show_frame(StartPage))
        back_button.pack()


class Table17(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text='Table 17')
        label.pack()

        back_button = tk.Button(self, text='Greenhouse',
                                command=lambda:
                                controller.show_frame(StartPage))
        back_button.pack()


class Table18(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text='Table 18')
        label.pack()

        back_button = tk.Button(self, text='Greenhouse',
                                command=lambda:
                                controller.show_frame(StartPage))
        back_button.pack()


class Table19(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text='Table 19')
        label.pack()

        back_button = tk.Button(self, text='Greenhouse',
                                command=lambda:
                                controller.show_frame(StartPage))
        back_button.pack()


class Table20(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text='Table 20')
        label.pack()

        back_button = tk.Button(self, text='Greenhouse',
                                command=lambda:
                                controller.show_frame(StartPage))
        back_button.pack()


class Table21(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text='Table 21')
        label.pack()

        back_button = tk.Button(self, text='Greenhouse',
                                command=lambda:
                                controller.show_frame(StartPage))
        back_button.pack()


class Table22(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text='Table 22')
        label.pack()

        back_button = tk.Button(self, text='Greenhouse',
                                command=lambda:
                                controller.show_frame(StartPage))
        back_button.pack()


class Table23(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text='Table 23')
        label.pack()

        back_button = tk.Button(self, text='Greenhouse',
                                command=lambda:
                                controller.show_frame(StartPage))
        back_button.pack()


class Table24(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text='Table 24')
        label.pack()

        back_button = tk.Button(self, text='Greenhouse',
                                command=lambda:
                                controller.show_frame(StartPage))
        back_button.pack()


app = PlantTracker()
app.mainloop()
