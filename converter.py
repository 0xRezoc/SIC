# customtkinter was imported as ctk for an easier approach
import customtkinter as ctk
from customtkinter import filedialog
from PIL import Image

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("dark-blue")


# Function to convert the image format
def convert_image():
    if selected_image:
        output_format = format_var.get()
        input_image = Image.open(selected_image)
        output_image = selected_image.replace(selected_image.split(".")[-1], output_format.lower())
        input_image.save(output_image)
        status_label.configure(text=f"Image converted to {output_format}")
    else:
        status_label.configure(text="Please select an image first")


# Function to update the selected image
def select_image():
    global selected_image
    selected_image = filedialog.askopenfilename(filetypes=[("Image Files", "*.jpg;*.jpeg;*.webp;*.png;*.bmp;*.avif")])
    if selected_image:
        convert_button.configure(state=ctk.NORMAL)
        status_label.configure(text=f"Selected Image: {selected_image}")
        # Remove the selected format from the dropdown if it's in the list
        format_var.set("Output Format")
        file_extension = selected_image.split(".")[-1]
        if file_extension.lower() in format_options:
            format_options.remove(file_extension.lower())
            format_combobox.configure(values=format_options)
    else:
        convert_button.configure(state=ctk.DISABLED)


# Create the main tkinter window
root = ctk.CTk()
root.iconbitmap("sic.ico")
root.title("Simple Image Converter")
root.geometry("475x310")
root.resizable(False, False)

# Global variable to store the selected image path
selected_image = None

# Create and configure widgets and packs
frame = ctk.CTkFrame(master=root)
frame.pack(pady=20, padx=20, fill="both", expand=True)

select_button = ctk.CTkButton(master=frame, text="Select Image", command=select_image)
select_button.pack(pady=20, padx=10)

status_label = ctk.CTkLabel(master=frame, text="Please select an image.")
status_label.pack(pady=5, padx=10)

format_var = ctk.StringVar(master=frame)
format_var.set("Output Format")
format_options = ["jpg", "webp", "png", "bmp", "avif", "jpeg"]
format_combobox = ctk.CTkComboBox(master=frame, variable=format_var, values=format_options)
format_combobox.pack(pady=12, padx=10)

convert_button = ctk.CTkButton(master=frame, text="Convert", command=convert_image, state=ctk.DISABLED)
convert_button.pack(pady=12, padx=10)

made_by = ctk.CTkLabel(master=frame, text="Made by 0xRezoc on GitHub", font=("Arial", 10))
made_by.pack(pady=24, padx=10)

# Start the customtkinter main loop
root.mainloop()
