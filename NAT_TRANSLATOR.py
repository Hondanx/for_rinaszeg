import os
import sys
import platform
import subprocess
import tkinter as tk
from tkinter import messagebox
from ldap3 import Server, Connection, ALL, NTLM
import re
import logging

# Configure Logging
logging.basicConfig(filename="nat_config.log", level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

# Active Directory Configuration (Modify as needed)
AD_SERVER = "ldap://SELF-AD"
AD_DOMAIN = "self.local"

# Function to validate IP address
def is_valid_ip(ip):
    pattern = r"^(?:[0-9]{1,3}\.){3}[0-9]{1,3}$"
    return re.match(pattern, ip) is not None

# Function to authenticate user with Active Directory
def authenticate(username, password):
    user_dn = f"{AD_DOMAIN}\\{username}"
    server = Server(AD_SERVER, get_info=ALL)

    try:
        conn = Connection(server, user=user_dn, password=password, authentication=NTLM, auto_bind=True)
        logging.info(f"User {username} authenticated successfully.")
        return True  # Login successful
    except Exception as e:
        logging.error(f"AD Authentication failed for {username}: {e}")
        return False  # Login failed

# Function to configure NAT 1:1
def configure_nat(private_ip, public_ip):
    os_type = platform.system()

    if os_type == "Linux":
        try:
            subprocess.run(["sudo", "iptables", "-t", "nat", "-A", "PREROUTING", "-d", public_ip, "-j", "DNAT", "--to-destination", private_ip], check=True)
            subprocess.run(["sudo", "iptables", "-t", "nat", "-A", "POSTROUTING", "-s", private_ip, "-j", "SNAT", "--to-source", public_ip], check=True)
            subprocess.run(["sudo", "iptables-save"], check=True)  # Save rules
            messagebox.showinfo("Success", "NAT 1:1 Mapping Added Successfully!")
            logging.info(f"NAT configured successfully: {private_ip} <-> {public_ip}")
        except subprocess.CalledProcessError as e:
            messagebox.showerror("Error", f"Failed to configure NAT: {e}")
            logging.error(f"Failed to configure NAT: {e}")

    elif os_type == "Windows":
        try:
            subprocess.run(["netsh", "interface", "portproxy", "add", "v4tov4", "listenaddress=" + public_ip, "connectaddress=" + private_ip], check=True)
            messagebox.showinfo("Success", "NAT 1:1 Mapping Added Successfully!")
            logging.info(f"NAT configured successfully: {private_ip} <-> {public_ip}")
        except subprocess.CalledProcessError as e:
            messagebox.showerror("Error", f"Failed to configure NAT: {e}")
            logging.error(f"Failed to configure NAT: {e}")
    else:
        messagebox.showerror("Error", "Unsupported OS")
        logging.error("Unsupported OS detected")

# Function to handle login and NAT setup
def handle_login():
    username = username_entry.get()
    password = password_entry.get()
    private_ip = private_ip_entry.get()
    public_ip = public_ip_entry.get()

    if not username or not password or not private_ip or not public_ip:
        messagebox.showwarning("Input Error", "All fields are required!")
        return

    if not is_valid_ip(private_ip) or not is_valid_ip(public_ip):
        messagebox.showerror("Input Error", "Invalid IP address format!")
        return

    if authenticate(username, password):
        configure_nat(private_ip, public_ip)
    else:
        messagebox.showerror("Login Failed", "Invalid Active Directory Credentials!")

# GUI Setup using Tkinter
root = tk.Tk()
root.title("1-to-1 NAT Configuration")
root.geometry("350x250")

tk.Label(root, text="Username:").pack()
username_entry = tk.Entry(root)
username_entry.pack()

tk.Label(root, text="Password:").pack()
password_entry = tk.Entry(root, show="*")
password_entry.pack()

tk.Label(root, text="Internal IP (Private):").pack()
private_ip_entry = tk.Entry(root)
private_ip_entry.pack()

tk.Label(root, text="External IP (Public):").pack()
public_ip_entry = tk.Entry(root)
public_ip_entry.pack()

login_button = tk.Button(root, text="Configure NAT", command=handle_login)
login_button.pack()

root.mainloop()
