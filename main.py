import tkinter as tk
from tkinter import ttk, messagebox
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import json
import os

# Configuration
ORDER_ITEMS = {
    "Burger Bun pack 13241": "24",
    "Focaccia pack 16201": "4",
    "Panini Sourdough 32162": "4",
    "Kid Burger 19128": ""
}

# Email Configuration
SMTP_SERVER = "smtp.gmail.com"
SMTP_PORT = 587
SENDER_EMAIL = "jcorio@gmail.com"  # Your Gmail address (e.g., "your.email@gmail.com")
SENDER_PASSWORD = "ckkuildgeysvmbsf"  # Your 16-character App Password from Google (no spaces)
RECIPIENT_EMAIL = "orders@turano.com"
ORDER_SUBJECT = "5389510"

class BreadOrderApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Turano Bread Order")
        self.root.geometry("400x400")
        
        # Configure style
        self.style = ttk.Style()
        self.style.configure('Modern.TFrame', background='#f0f0f0')
        self.style.configure('Modern.TLabel', background='#f0f0f0', font=('Segoe UI', 10))
        self.style.configure('Title.TLabel', background='#f0f0f0', font=('Segoe UI', 14, 'bold'))
        self.style.configure('Modern.TButton', 
                           font=('Segoe UI', 10),
                           padding=10)
        self.style.configure('Modern.TEntry', 
                           padding=5,
                           font=('Segoe UI', 10))
        
        # Create main frame with padding and background
        main_frame = ttk.Frame(root, padding="20", style='Modern.TFrame')
        main_frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))
        
        # Create widgets
        self.create_widgets(main_frame)
        
        # Configure grid
        root.columnconfigure(0, weight=1)
        root.rowconfigure(0, weight=1)
        main_frame.columnconfigure(1, weight=1)

    def create_widgets(self, parent):
        # Title with modern styling
        title_label = ttk.Label(parent, 
                              text="Turano Bread Order", 
                              style='Title.TLabel')
        title_label.grid(row=0, column=0, columnspan=2, pady=(0, 20))
        
        # Create entry fields for each item with modern styling
        self.entries = {}
        for i, (item, _) in enumerate(ORDER_ITEMS.items(), 1):
            ttk.Label(parent, 
                     text=item,
                     style='Modern.TLabel').grid(row=i, column=0, sticky=tk.W, pady=5)
            entry = ttk.Entry(parent, 
                            width=4,
                            style='Modern.TEntry')
            entry.grid(row=i, column=1, sticky=tk.W, pady=5, padx=(10, 0))
            self.entries[item] = entry
        
        # Send button with modern styling
        send_button = ttk.Button(parent, 
                               text="Send Order", 
                               command=self.send_order,
                               style='Modern.TButton')
        send_button.grid(row=len(ORDER_ITEMS) + 1, 
                        column=0, 
                        columnspan=2, 
                        pady=20)
        
        # Status label with modern styling
        self.status_label = ttk.Label(parent, 
                                    text="",
                                    style='Modern.TLabel')
        self.status_label.grid(row=len(ORDER_ITEMS) + 2, 
                             column=0, 
                             columnspan=2)

    def send_order(self):
        # Validate email settings
        if not SENDER_EMAIL or not SENDER_PASSWORD:
            messagebox.showerror("Error", "Please configure your email settings in the script")
            return
        
        # Build email content
        content = []
        for item, entry in self.entries.items():
            quantity = entry.get().strip()
            if quantity:
                content.append(f"{item} - {quantity}")
        
        if not content:
            messagebox.showwarning("Warning", "Please enter at least one quantity")
            return
        
        email_content = "\n".join(content)
        
        try:
            # Create message
            msg = MIMEMultipart()
            msg['From'] = SENDER_EMAIL
            msg['To'] = RECIPIENT_EMAIL
            msg['Subject'] = ORDER_SUBJECT
            
            msg.attach(MIMEText(email_content, 'plain'))
            
            # Send email
            with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
                server.starttls()
                server.login(SENDER_EMAIL, SENDER_PASSWORD)
                server.send_message(msg)
            
            # Show success message
            self.status_label.config(text="Order sent successfully!", foreground="green")
            messagebox.showinfo("Success", "Order sent successfully!")
            
        except Exception as e:
            self.status_label.config(text=f"Error: {str(e)}", foreground="red")
            messagebox.showerror("Error", f"Failed to send order: {str(e)}")

def main():
    root = tk.Tk()
    app = BreadOrderApp(root)
    root.mainloop()

if __name__ == "__main__":
    main() 