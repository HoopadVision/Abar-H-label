import tkinter as tk
from PIL import Image, ImageTk
import os
import random
import shutil
from tkinter import messagebox


directory = "images"
unknown = "unknown"
output_directory = "output_dir"

characters = {
    "A" : "الف",
    "B" : "ب",
    "C" : "ج",
    "D" : "ل",
    "E" : "م",
    "F" : "ن",
    "G" : "ق",
    "H" : "و",
    "I" : "ه",
    "J" : "ی",
    "K" : "د",
    "L" : "س",
    "M" : "ص",
    "N" : "معلول",
    "N" : "ژ",
    "O" : "ت",
    "P" : "ط",
    "Q" : "ع",
    "R" : "D",
    "S" : "S",
    "T" : "پ",
    "U" : "تشریفات",
    "V" : "ث",
    "W" : "ز",
    "X" : "ش",
    "Y" : "ف",
    "Z" : "ک",
    "_" : "گ"
}

# for i in list(characters.keys()):

def show_random_image():
    try:
        image_files = [f for f in os.listdir(directory)]
        random_image = random.choice(image_files)
        image_path = os.path.join(directory, random_image)
        image = Image.open(image_path)
        width = 300
        aspect_ratio = image.width / image.height
        height = int(width / aspect_ratio)
        image = image.resize((width, height))

        photo = ImageTk.PhotoImage(image)
        label.config(image=photo)
        label.image = photo
        image_name_entry.delete(0, tk.END)  
        image_name_entry.insert(0, random_image)  
        image_label['text'] = random_image
        en1.delete(0, tk.END)
        en2.delete(0, tk.END)
        en3.delete(0, tk.END)
        en4.delete(0, tk.END)
        for i in list(characters.keys()):
            x = random_image.split("_")[0].split(i)
            if len(x) != 1:
                # x[0] : رقم سمت چپ پلاک
                # x[1] : رقم سمت راست پلاک
                en1.insert(0, x[0])
                en2.insert(0, characters[i])
                en3.insert(0, x[1][0:3])
                en4.insert(0, x[1][-2:])
    except:
        messagebox.showerror('Error reading images', """This error is caused by two possibilities:
1. The images folder not exists.
2. There is a problem with the scanned image. 

To fix the possible problem, option 2 on the unknown button.""")
            
        
    
    # shutil.copy(image_path, new_image_path)

def convert():
    e1 = en1.get()
    e2 = en2.get()
    e3 = en3.get()
    e4 = en4.get()
    x = 0
    for i in list(characters.values()):
        if e2 == i:
            e2 = list(characters.keys())[x]
        x += 1
    return f"{e1}_{e2}_{e3}_{e4}"



def unknown_image():
    global unknown
    os.makedirs(unknown, exist_ok=True)
    new_image_name = image_name_entry.get()
    image = image_label['text']
    image_dir = f"{directory}/{image}"
    new_image_dir = f"{unknown}/{new_image_name}"
    shutil.copy(image_dir, new_image_dir)
    os.remove(image_dir)
    show_random_image()

def next():
    global output_directory
    os.makedirs(output_directory, exist_ok=True)
    text = convert()
    image = image_label['text']
    file_format = image.split(".")
    file_format = file_format[-1]
    image_dir = f"{directory}/{image}"
    new_image_dir = f"{output_directory}/{text}.{file_format}"
    shutil.copy(image_dir, new_image_dir)
    os.remove(image_dir)
    show_random_image()

def number_label():
    Labels = len(os.listdir(directory))
    outputs = len(os.listdir(output_directory))
    unknowns = len(os.listdir(unknown))
    messagebox.showinfo("Number of Labels",
    f"""
    Number of labels: {Labels}
    Number of output labels: {outputs}
    Number of unknown labels: {unknowns}
    """)

def file_structure():
    messagebox.showinfo("Folder Structure",
'''
There should be 3 folders next to the program.
The main folder of labels is called images.
The modified photos folder is called output_dir.
Unknown fold labels are called unknown.
The labels whose values are reviewed and recorded are stored in the output_dir folder.
Labels whose values are unrecognizable are put in the unknown folder.
''')

def structure():
    messagebox.showinfo("Structure",
"""
The functionality of the program is designed for the labels of HOOPAD VISION

The function of the program is that the labels inside the images folder are read along with their exclusive names.
Different license plates are displayed with their string, and the string must be set based on the license plates themselves.
If the license plate and string are readable and set, the next button will set the photo of these plates with the name of the set string stored
If the license plate and string are unreadable, by pressing the unknown button, the license plate will be transferred to the same folder
""")

def about():
    messagebox.showinfo("About US", 'Designed by ABARVISION CO for HOOPADVISION CO labels, all rights are reserved and belong to the collaboration of these two companies')

root = tk.Tk()
root.title("Abar-H-Label")
menubar = tk.Menu(root)
root.config(menu=menubar)
file = tk.Menu(menubar, tearoff=0)
menubar.add_cascade(label="Action", menu=file)
file.add_command(label="Number of labels", command=number_label)
file.add_command(label="Skip", command=show_random_image)
file.add_command(label="Next photo", command=next)
file.add_command(label="Unknown", command=unknown_image)
num_of_labels = tk.Menu(menubar, tearoff=0)
help = tk.Menu(menubar, tearoff=0)
menubar.add_cascade(label="help", menu=help)
help.add_command(label="Folder structure", command=file_structure)
help.add_command(label="Structure", command=structure)
help.add_command(label="About", command=about)
frame = tk.Frame(root)
plate_frame = tk.Frame(root)
label = tk.Label(root)
image_label = tk.Label(root)

en1 = tk.Entry(plate_frame, width=3, font=('b traffic', 30))
en2 = tk.Entry(plate_frame, width=2, font=('b traffic', 30))
en3 = tk.Entry(plate_frame, width=4, font=('b traffic', 30))
en4 = tk.Entry(plate_frame, width=3, font=('b traffic', 30))
en1.grid(row=0, column=0)
en2.grid(row=0, column=1)
en3.grid(row=0, column=2)
en4.grid(row=0, column=3)



image_name_entry = tk.Entry(root)
image_label.pack()

space = tk.Label(frame, text="", width=1)
space1 = tk.Label(frame, text="", width=1)
button = tk.Button(frame, text="Next Image", width=15, height=3, command=next)
unknows_btn = tk.Button(frame, text="Unknown", height=3, width=7, command=unknown_image)
skip_btn = tk.Button(frame, text="Skip", height=3, width=7, command=show_random_image)

label.pack()
plate_frame.pack()


unknows_btn.grid(row=0, column=4)
space.grid(row=0, column=1)
button.grid(row=0, column=2)
space1.grid(row=0, column=3)
skip_btn.grid(row=0, column=0)
frame.pack()

os.makedirs(output_directory, exist_ok=True)
show_random_image()
root.mainloop()
