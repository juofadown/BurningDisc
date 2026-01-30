import sqlite3
from pathlib import Path
import tkinter as tk
from tkinter import ttk

BASE_DIR = Path(__file__).parent
ASSETS_DIR = BASE_DIR / "assets"
DB_DIR = BASE_DIR.parent / "database"
DB_FILE = DB_DIR / "burning_disc.db"

COLOUR_BG = "#D9D9D9"
COLOUR_TOOLBAR = "#D9D9D9"

class BurningDiscApp():
    def __init__(self, root):
        # gui
        self.root = root
        self.root.title("Burning Disc")
        self.root.geometry("900x500")

        #app icon
        self.icon = tk.PhotoImage(file=ASSETS_DIR / "burning_disc_logo70.png")
        self.root.iconphoto(False, self.icon)

        #db
        self.connect = sqlite3.connect(DB_FILE)
        self.cursor = self.connect.cursor()

        #variables
        self.id = tk.IntVar()
        self.title = tk.StringVar()
        self.artist = tk.StringVar()
        self.year = tk.StringVar()
        self.reclabel = tk.StringVar()
        self.type = tk.StringVar()

        self.b_mp3 = tk.BooleanVar()
        self.b_surface = tk.BooleanVar()
        self.b_ext = tk.BooleanVar()
        self.b_usb = tk.BooleanVar()

        #layout
        self.toolbar_btn_width = 6
        self.toolbar_btn_height = 3
        self.toolbar_padx = 10
        self.toolbar_pady = 10
        self.content_padx = (10, 5)
        self.content_pady = 3
        self.content_top_pady = (30, 3)

        self.build_toolbar()
        self.build_content()
        self.startup()

    def build_toolbar(self):
        # toolbar
        toolbar = tk.Frame(self.root, bg=COLOUR_TOOLBAR, height=100)
        toolbar.pack(fill="x", side="top")

        self.btn_new = tk.Button(toolbar, text='New', command=self.new, width=self.toolbar_btn_width, height=self.toolbar_btn_height)
        self.btn_new.pack(side='left', padx=self.toolbar_padx, pady=self.toolbar_pady)

        self.btn_edit = tk.Button(toolbar, text='Edit', command=self.edit, width=self.toolbar_btn_width, height=self.toolbar_btn_height)
        self.btn_edit.pack(side='left', padx=self.toolbar_padx, pady=self.toolbar_pady)

        self.btn_save = tk.Button(toolbar, text='Save', command=self.save, width=self.toolbar_btn_width, height=self.toolbar_btn_height)
        self.btn_save.pack(side='left', padx=self.toolbar_padx, pady=self.toolbar_pady)

        self.btn_delete = tk.Button(toolbar, text='Delete', command=self.delete, width=self.toolbar_btn_width, height=self.toolbar_btn_height)
        self.btn_delete.pack(side='left', padx=self.toolbar_padx, pady=self.toolbar_pady)

        self.btn_cancel = tk.Button(toolbar, text='<', command=self.cancel, width=self.toolbar_btn_width, height=self.toolbar_btn_height)
        self.btn_cancel.pack(side='right', padx=self.toolbar_padx, pady=self.toolbar_pady)

        self.logo_img = tk.PhotoImage(file=ASSETS_DIR / "burning_disc_logo70.png")
        self.logo_lbl = tk.Label(toolbar, image=self.logo_img, bg=COLOUR_TOOLBAR)
        self.logo_lbl.pack(side="right")

        self.toolbar_lbl = tk.Label(toolbar, text="Burning Disc", font=("Prociono", 32, "bold"), bg=COLOUR_TOOLBAR)
        self.toolbar_lbl.pack(side="right", pady=(7, 0))
    
    def build_content(self):
        # content frame
        content_frame = tk.Frame(self.root)
        content_frame.pack(fill="both", expand=True)

        # id
        self.lbl_id = tk.Label(content_frame, text="ID")
        self.lbl_id.grid(row=0, column=0, sticky="e", padx=self.content_padx, pady=self.content_top_pady)

        self.entry_id = ttk.Entry(content_frame, state='readonly', textvariable=self.id, width=10)
        self.entry_id.grid(row=0, column=1, sticky="w", pady=self.content_top_pady)

        # title
        self.lbl_title = tk.Label(content_frame, text='Title')
        self.lbl_title.grid(row=1, column=0, sticky='e', padx=self.content_padx, pady=self.content_pady)

        self.entry_title = ttk.Entry(content_frame, textvariable=self.title, width=30)
        self.entry_title.grid(row=1, column=1, sticky="w", pady=self.content_pady)

        # artist
        self.lbl_artist = tk.Label(content_frame, text='Artist')
        self.lbl_artist.grid(row=2, column=0, sticky='e', padx=self.content_padx, pady=self.content_pady)

        self.entry_artist = ttk.Entry(content_frame, textvariable=self.artist, width=30)
        self.entry_artist.grid(row=2, column=1, sticky="w", pady=self.content_pady)

        # description
        self.lbl_description = tk.Label(content_frame, text='Description')
        self.lbl_description.grid(row=3, column=0, sticky='ne', padx=self.content_padx, pady=self.content_pady)

        self.txt_description = tk.Text(content_frame, width=30, height=7)
        self.txt_description.grid(row=3, column=1, sticky='w', pady=self.content_pady)

        # year
        self.lbl_year = tk.Label(content_frame, text='Year')
        self.lbl_year.grid(row=0, column=2, sticky='e',padx=self.content_padx, pady=self.content_top_pady)

        self.entry_year = ttk.Entry(content_frame, textvariable=self.year,width=30)
        self.entry_year.grid(row=0, column=3, sticky="w", pady=self.content_top_pady)

        # record label
        self.lbl_reclabel = tk.Label(content_frame, text='Record Label')
        self.lbl_reclabel.grid(row=1, column=2, sticky='e',padx=self.content_padx, pady=self.content_pady)

        self.entry_reclabel = ttk.Entry(content_frame, textvariable=self.reclabel, width=30)
        self.entry_reclabel.grid(row=1, column=3, sticky="w", pady=self.content_pady)

        # dropdown type
        self.lbl_type = tk.Label(content_frame, text='Type')
        self.lbl_type.grid(row=2, column=2, sticky='e',padx=self.content_padx, pady=self.content_pady)

        self.dropdown_type = ttk.Combobox(content_frame, values=['MP3', 'FLAC', 'CD'], textvariable=self.type, width=20, state='readonly')
        self.dropdown_type.grid(row=2, column=3, sticky='w', pady=self.content_pady)

        # location
        self.lbl_location = tk.Label(content_frame, text='Location')
        self.lbl_location.grid(row=3, column=2, sticky='ne', padx=self.content_padx, pady=self.content_pady)

        # mother frame for checkboxes
        frame_location = tk.Frame(content_frame)
        frame_location.grid(row=3, column=3, sticky='w', pady=self.content_pady)

        # checkboxes
        self.cb_mp3 = tk.Checkbutton(frame_location, text="MP3 Player", variable=self.b_mp3)
        self.cb_mp3.grid(row=0, column=0, sticky='w', pady=2)

        self.cb_surface = tk.Checkbutton(frame_location, text="Surface", variable=self.b_surface)
        self.cb_surface.grid(row=1, column=0, sticky='w', pady=2)

        self.cb_ext = tk.Checkbutton(frame_location, text="External Disk", variable=self.b_ext)
        self.cb_ext.grid(row=2, column=0, sticky='w', pady=2)

        self.cb_usb = tk.Checkbutton(frame_location, text="USB Stick", variable=self.b_usb)
        self.cb_usb.grid(row=3, column=0, sticky='w', pady=2)

    # toolbar functions
    def new(self):
        self.btn_state = 1
        self.manage_btnstate(self.btn_state)
        self.clear_fields()

    def edit(self):
        self.btn_state = 2
        self.manage_btnstate(self.btn_state)

    def save(self):
        title = self.title.get().strip()
        year = self.year.get().strip()
        label = self.reclabel.get().strip()
        description = self.txt_description.get("1.0", tk.END)

        try:
            self.cursor.execute(
                """
                INSERT INTO ALBUM 
                (title, release_year, label, description)
                VALUES (?, ?, ?, ?)
                """,
                (title, int(year), label, description)
            )
            self.connect.commit()

        except sqlite3.Error as error:
            print("database error: ", error)
        
        self.btn_state = 0
        self.manage_btnstate(self.btn_state)

    def delete(self):
        self.btn_state = 0
        self.manage_btnstate(self.btn_state)

    def cancel(self):
        self.btn_state = 0
        self.manage_btnstate(self.btn_state)

    def clear_fields(self):
        self.title.set("")
        self.artist.set("")
        self.year.set("")
        self.reclabel.set("")
        self.type.set("")
        self.txt_description.delete("1.0", tk.END)

        self.b_mp3.set(False)
        self.b_ext.set(False)
        self.b_surface.set(False)
        self.b_usb.set(False)

    # btnstate function
    def manage_btnstate(self, state):
        self.btn_state = state
        if self.btn_state == 0:
            self.btn_new.config(state="normal")
            self.btn_edit.config(state="normal")
            self.btn_save.config(state="disabled")
            self.btn_delete.config(state="normal")

            self.entry_title.config(state='disabled')
            self.entry_artist.config(state='disabled')
            self.entry_year.config(state='disabled')
            self.entry_reclabel.config(state='disabled')
            self.txt_description.config(state='disabled')
            self.dropdown_type.config(state='disabled')
            self.cb_ext.config(state='disabled')
            self.cb_mp3.config(state='disabled')
            self.cb_surface.config(state='disabled')
            self.cb_usb.config(state='disabled')
        
        elif self.btn_state == 1 or self.btn_state == 2:
            self.btn_new.config(state="disabled")
            self.btn_edit.config(state="disabled")
            self.btn_save.config(state="normal")
            self.btn_delete.config(state="disabled")

            self.entry_title.config(state='normal')
            self.entry_artist.config(state='normal')
            self.entry_year.config(state='normal')
            self.entry_reclabel.config(state='normal')
            self.txt_description.config(state='normal')
            self.dropdown_type.config(state='readonly')
            self.cb_ext.config(state='normal')
            self.cb_mp3.config(state='normal')
            self.cb_surface.config(state='normal')
            self.cb_usb.config(state='normal')

    # startup
    def startup(self):
        self.btn_state = 0 #0 = view, 1 = new, 2 = editing

        self.btn_new.config(state="normal")
        self.btn_edit.config(state="normal")
        self.btn_save.config(state="disabled")
        self.btn_delete.config(state="normal")

        self.entry_id.config(state='readonly')
        self.entry_title.config(state='disabled')
        self.entry_artist.config(state='disabled')
        self.entry_year.config(state='disabled')
        self.entry_reclabel.config(state='disabled')
        self.txt_description.config(state='disabled')
        self.cb_ext.config(state='disabled')
        self.cb_mp3.config(state='disabled')
        self.cb_surface.config(state='disabled')
        self.cb_usb.config(state='disabled')

root = tk.Tk()
app = BurningDiscApp(root)
root.mainloop()