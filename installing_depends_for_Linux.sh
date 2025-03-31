#!/bin/bash

echo "====================================================="
echo " Installing Prerequisites for NAT Script (Ubuntu/Debian)"
echo "====================================================="
echo

# Step 1: Update package list
echo "Updating package list..."
sudo apt update -y

# Step 2: Install system-wide Python packages using APT
echo "Installing required system packages..."
sudo apt install -y python3 python3-tk python3-ldap3 iptables

# Step 3: Enable IP Forwarding for NAT
echo "Enabling IP forwarding..."
sudo sysctl -w net.ipv4.ip_forward=1
echo "net.ipv4.ip_forward = 1" | sudo tee -a /etc/sysctl.conf > /dev/null

# Step 4: Verify Installations
echo "Verifying installations..."
python3 -c "import ldap3, tkinter, platform; print('All modules installed successfully!')"

echo
echo "====================================================="
echo " Prerequisites installation completed successfully!"
echo " You can now run the main script."
echo "====================================================="
echo

