import tkinter as tk
from tkinter import messagebox
from manager import save_password, get_password

# Initialize window
root = tk.Tk()
root.title("🔐 Password Manager")
root.geometry("400x300")
root.config(padx=20, pady=20)

# ------------------ Save Password ------------------
def save():
    service = service_entry.get()
    username = username_entry.get()
    password = password_entry.get()

    if not service or not username or not password:
        messagebox.showwarning("Missing Fields", "Please fill in all fields.")
        return

    save_password(service, username, password)
    messagebox.showinfo("Saved", f"Password for '{service}' saved successfully!")
    service_entry.delete(0, tk.END)
    username_entry.delete(0, tk.END)
    password_entry.delete(0, tk.END)

# ------------------ Retrieve Password ------------------
def retrieve():
    service = service_entry.get()
    if not service:
        messagebox.showwarning("Missing Service", "Please enter a service to search.")
        return

    username, password = get_password(service)
    if username:
        result_text.set(f"Username: {username}\nPassword: {password}")
    else:
        result_text.set("❌ No entry found for this service.")

# ------------------ GUI Layout ------------------

# Labels
tk.Label(root, text="Service:").grid(row=0, column=0, sticky="w")
tk.Label(root, text="Username:").grid(row=1, column=0, sticky="w")
tk.Label(root, text="Password:").grid(row=2, column=0, sticky="w")

# Entry Fields
service_entry = tk.Entry(root, width=30)
service_entry.grid(row=0, column=1)

username_entry = tk.Entry(root, width=30)
username_entry.grid(row=1, column=1)

password_entry = tk.Entry(root, width=30, show="*")
password_entry.grid(row=2, column=1)

# Buttons
tk.Button(root, text="💾 Save Password", width=20, command=save).grid(row=3, column=0, pady=10)
tk.Button(root, text="🔍 Retrieve Password", width=20, command=retrieve).grid(row=3, column=1)

# Result Display
result_text = tk.StringVar()
result_label = tk.Label(root, textvariable=result_text, justify="left", fg="blue")
result_label.grid(row=4, column=0, columnspan=2, pady=20)

# Run the GUI app
root.mainloop()
