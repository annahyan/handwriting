import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
import os

image_dir = "/home/anna/ClusterProjects/handwriting/data_processing/0386_230410150714_001.pdf-04"


class ImageGUI:
    def __init__(self, master):
        self.master = master
        self.image_dir = image_dir
        self.image_list = os.listdir(self.image_dir)
        self.current_image_index = 0
        
        # create label to display image
        self.image_label = tk.Label(self.master)
        self.image_label.pack()
        
        # load first image
        self.load_image()
        
        # create checkbox to mark image as checked
        self.checked_var = tk.BooleanVar()
        self.checked_var.set(False)
        self.check_button = tk.Checkbutton(self.master, text="Mark as checked",
                                            variable=self.checked_var)
        self.check_button.pack()
        
        # create input box for text
        self.input_var = tk.StringVar()
        self.input_entry = tk.Entry(self.master, textvariable=self.input_var, 
                                    width = 100)
        self.input_entry.pack()
        
        # create button to show next image
        self.next_button = tk.Button(self.master, text="Next", 
                                     command=self.show_next_image)
        self.next_button.pack()
    
    def load_image(self):
        # load current image and display it in the label
        current_image_path = os.path.join(self.image_dir, 
                                          self.image_list[self.current_image_index])
        image = Image.open(current_image_path)
        photo = ImageTk.PhotoImage(image)
        self.image_label.config(image=photo)
        self.image_label.image = photo  # prevent garbage collection
    
    def show_next_image(self):
        # write name of image and input to file if checkbox is checked
        if self.checked_var.get():
            self.write_checked_image()
        
        # Clear the checkbox and the input string
        self.checked_var.set(False)
        self.input_var.set("")
        
        # increment image index and load next image
        self.current_image_index += 1
        if self.current_image_index >= len(self.image_list):
            self.current_image_index = 0
        self.load_image()
    
    def write_checked_image(self):
        # write name of current image and input to file
        checked_image = self.image_list[self.current_image_index]
        checked_input = self.input_var.get()
        image_inputs_file = "image_inputs.txt"
        with open(image_inputs_file, "a") as f:
            f.write(f"{checked_image},{checked_input}\n")
        messagebox.showinfo("Image Checked", f"The image {checked_image} with input '{checked_input}' has been marked as checked.")

if __name__ == "__main__":
    root = tk.Tk()
    app = ImageGUI(root)
    root.mainloop()
