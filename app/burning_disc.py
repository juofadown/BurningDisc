import sqlite3
from pathlib import Path
import tkinter as tk
from tkinter import ttk

BASE_DIR = Path(__file__).parent
ASSETS_DIR = BASE_DIR / "assets"
DB_DIR = BASE_DIR.parent / "database"
DB_FILE = DB_DIR / "burning_disc.db"

connect = sqlite3.connect(DB_FILE)
cursor = connect.cursor()

# btnstates: 0 = view, 1 = new, 2 = editing
btn_state = 0

COLOUR_BG = "#D9D9D9"
COLOUR_TOOLBAR = "#D9D9D9"

toolbar_btn_width = 6
toolbar_btn_height = 3

toolbar_padx = 10
toolbar_pady = 10

content_padx = (10, 5)
content_pady = 3
content_top_pady = (30, 3)

# gui
root = tk.Tk()
root.title("Burning Disc")
root.geometry("900x500")

icon = tk.PhotoImage(file=ASSETS_DIR / "burning_disc_logo70.png")
root.iconphoto(False, icon)

logo_img = tk.PhotoImage(file=ASSETS_DIR / "burning_disc_logo70.png")

# toolbar functions
def new():
    global btn_state
    print("New clicked")
    btn_state = 1
    manage_btnstate(btn_state)

def edit():
    global btn_state
    print("Edit clicked")
    btn_state = 2
    manage_btnstate(btn_state)

def save():
    global btn_state
    print("Save clicked")
    btn_state = 0
    manage_btnstate(btn_state)

def delete():
    global btn_state
    print("Delete clicked")
    btn_state = 0
    manage_btnstate(btn_state)

def cancel():
    global btn_state
    print("Cancel clicked")
    btn_state = 0
    manage_btnstate(btn_state)

# btnstate function
def manage_btnstate(state):
    global btn_state
    btn_state = state
    if btn_state == 0:
        btn_new.config(state="normal")
        btn_edit.config(state="normal")
        btn_save.config(state="disabled")
        btn_delete.config(state="normal")

        entry_title.config(state='disabled')
        entry_artist.config(state='disabled')
        entry_year.config(state='disabled')
        entry_reclabel.config(state='disabled')
        txt_description.config(state='disabled')
        dropdown_type.config(state='disabled')
        cb_ext.config(state='disabled')
        cb_mp3.config(state='disabled')
        cb_surface.config(state='disabled')
        cb_usb.config(state='disabled')
        
    elif btn_state == 1 or btn_state == 2:
        btn_new.config(state="disabled")
        btn_edit.config(state="disabled")
        btn_save.config(state="normal")
        btn_delete.config(state="disabled")

        entry_title.config(state='normal')
        entry_artist.config(state='normal')
        entry_year.config(state='normal')
        entry_reclabel.config(state='normal')
        txt_description.config(state='normal')
        dropdown_type.config(state='readonly')
        cb_ext.config(state='normal')
        cb_mp3.config(state='normal')
        cb_surface.config(state='normal')
        cb_usb.config(state='normal')

# toolbar
toolbar = tk.Frame(root, bg=COLOUR_TOOLBAR, height=100)
toolbar.pack(fill="x", side="top")

btn_new = tk.Button(toolbar, text='New', command=new, width=toolbar_btn_width, height=toolbar_btn_height)
btn_new.pack(side='left', padx=toolbar_padx, pady=toolbar_pady)

btn_edit = tk.Button(toolbar, text='Edit', command=edit, width=toolbar_btn_width, height=toolbar_btn_height)
btn_edit.pack(side='left', padx=toolbar_padx, pady=toolbar_pady)

btn_save = tk.Button(toolbar, text='Save', command=save, width=toolbar_btn_width, height=toolbar_btn_height)
btn_save.pack(side='left', padx=toolbar_padx, pady=toolbar_pady)

btn_delete = tk.Button(toolbar, text='Delete', command=delete, width=toolbar_btn_width, height=toolbar_btn_height)
btn_delete.pack(side='left', padx=toolbar_padx, pady=toolbar_pady)

btn_cancel = tk.Button(toolbar, text='<', command=cancel, width=toolbar_btn_width, height=toolbar_btn_height)
btn_cancel.pack(side='right', padx=toolbar_padx, pady=toolbar_pady)

logo_lbl = tk.Label(toolbar, image=logo_img, bg=COLOUR_TOOLBAR)
logo_lbl.pack(side="right")

toolbar_lbl = tk.Label(toolbar, text="Burning Disc", font=("Prociono", 32, "bold"), bg=COLOUR_TOOLBAR)
toolbar_lbl.pack(side="right", pady=(7, 0))

# content frame
content_frame = tk.Frame(root)
content_frame.pack(fill="both", expand=True)

# id
lbl_id = tk.Label(content_frame, text="ID")
lbl_id.grid(row=0, column=0, sticky="e", padx=content_padx, pady=content_top_pady)

entry_id = ttk.Entry(content_frame, state='readonly',width=10)
entry_id.grid(row=0, column=1, sticky="w", pady=content_top_pady)

# title
lbl_title = tk.Label(content_frame, text='Title')
lbl_title.grid(row=1, column=0, sticky='e',padx=content_padx, pady=content_pady)

entry_title = ttk.Entry(content_frame, width=30)
entry_title.grid(row=1, column=1, sticky="w", pady=content_pady)

# artist
lbl_artist = tk.Label(content_frame, text='Artist')
lbl_artist.grid(row=2, column=0, sticky='e', padx=content_padx, pady=content_pady)

entry_artist = ttk.Entry(content_frame, width=30)
entry_artist.grid(row=2, column=1, sticky="w", pady=content_pady)

# description
lbl_description = tk.Label(content_frame, text='Description')
lbl_description.grid(row=3, column=0, sticky='ne', padx=content_padx, pady=content_pady)

txt_description = tk.Text(content_frame, width=30, height=7)
txt_description.grid(row=3, column=1, sticky='w', pady=content_pady)

# year
lbl_year = tk.Label(content_frame, text='Year')
lbl_year.grid(row=0, column=2, sticky='e',padx=content_padx, pady=content_top_pady)

entry_year = ttk.Entry(content_frame, width=30)
entry_year.grid(row=0, column=3, sticky="w", pady=content_top_pady)

# record label
lbl_reclabel = tk.Label(content_frame, text='Record Label')
lbl_reclabel.grid(row=1, column=2, sticky='e',padx=content_padx, pady=content_pady)

entry_reclabel = ttk.Entry(content_frame, width=30)
entry_reclabel.grid(row=1, column=3, sticky="w", pady=content_pady)

# dropdown type
lbl_type = tk.Label(content_frame, text='Type')
lbl_type.grid(row=2, column=2, sticky='e',padx=content_padx, pady=content_pady)

dropdown_type = ttk.Combobox(content_frame, values=['MP3', 'FLAC', 'CD'], width=20, state='readonly')
dropdown_type.grid(row=2, column=3, sticky='w', pady=content_pady)

# location
lbl_location = tk.Label(content_frame, text='Location')
lbl_location.grid(row=3, column=2, sticky='ne', padx=content_padx, pady=content_pady)

# mother frame for checkboxes
frame_location = tk.Frame(content_frame)
frame_location.grid(row=3, column=3, sticky='w', pady=content_pady)

# checkboxes:
b_mp3 = tk.BooleanVar()
cb_mp3 = tk.Checkbutton(frame_location, text="MP3 Player", variable=b_mp3)
cb_mp3.grid(row=0, column=0, sticky='w', pady=2)

b_surface = tk.BooleanVar()
cb_surface = tk.Checkbutton(frame_location, text="Surface", variable=b_surface)
cb_surface.grid(row=1, column=0, sticky='w', pady=2)

b_ext = tk.BooleanVar()
cb_ext = tk.Checkbutton(frame_location, text="External Disk", variable=b_ext)
cb_ext.grid(row=2, column=0, sticky='w', pady=2)

b_usb = tk.BooleanVar()
cb_usb = tk.Checkbutton(frame_location, text="USB Stick", variable=b_usb)
cb_usb.grid(row=3, column=0, sticky='w', pady=2)

# startup
btn_new.config(state="normal")
btn_edit.config(state="normal")
btn_save.config(state="disabled")
btn_delete.config(state="normal")

entry_id.config(state='readonly')
entry_title.config(state='disabled')
entry_artist.config(state='disabled')
entry_year.config(state='disabled')
entry_reclabel.config(state='disabled')
txt_description.config(state='disabled')
cb_ext.config(state='disabled')
cb_mp3.config(state='disabled')
cb_surface.config(state='disabled')
cb_usb.config(state='disabled')

root.mainloop()