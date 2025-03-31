# for_rinaszeg 
# NAT Translator Setup Guide

This guide provides instructions for setting up and running the NAT Translator script on both Windows and Linux. The package includes three scripts:

1. **NAT_TRANSLATOR.py** – The main script for configuring NAT.
2. **installing_depends_for_Linux.sh** – A script to install prerequisites on Linux.
3. **installing_depends_for_win.bat** – A script to install prerequisites on Windows.

Before running the scripts, ensure that you update the following variables in `NAT_TRANSLATOR.py` with your Active Directory server details:

```python
AD_SERVER = "ldap://Your AD SERVER NAME"
AD_DOMAIN = "YOUR DOMAIN NAME"
```

---
## **Section 1: Windows Instructions**

### **Step 1: Verify Connectivity**
Before proceeding, ensure that your system can communicate with the Active Directory (AD) server.

1. **Check DNS resolution:**
   ```powershell
   nslookup your_ad_server_name
   ```

2. **Test connectivity to the AD server:**
   ```powershell
   Test-Connection your_ad_server_name -Count 4
   ```

3. **Ensure LDAP ports are open (389 for standard, 636 for secure LDAP):**
   ```powershell
   Test-NetConnection -ComputerName your_ad_server_name -Port 389
   Test-NetConnection -ComputerName your_ad_server_name -Port 636
   ```

If any of these tests fail, verify network settings and firewall rules.

### **Step 2: Install Dependencies**
Run the provided batch script to install required dependencies:
   ```powershell
   installing_depends_for_win.bat
   ```

### **Step 3: Run the NAT Translator Script**
Once dependencies are installed, execute the main script:
   ```powershell
   python NAT_TRANSLATOR.py
   ```

---
## **Section 2: Linux Instructions**

### **Step 1: Verify Connectivity**
Before running the script, confirm that your Linux system can reach the AD server.

1. **Check DNS resolution:**
   ```bash
   nslookup your_ad_server_name
   ```

2. **Ping the AD server:**
   ```bash
   ping -c 4 your_ad_server_name
   ```

3. **Ensure LDAP ports are open:**
   ```bash
   nc -zv your_ad_server_name 389
   nc -zv your_ad_server_name 636
   ```

If these checks fail, troubleshoot your network settings.

### **Step 2: Install Dependencies**
Run the Linux dependency installation script:
   ```bash
   chmod +x installing_depends_for_Linux.sh
   ./installing_depends_for_Linux.sh
   ```

### **Step 3: Run the NAT Translator Script**
Once dependencies are installed, execute the script:
   ```bash
   python3 NAT_TRANSLATOR.py
   ```

---
## **Troubleshooting Tips**
- If authentication fails, double-check the `AD_SERVER` and `AD_DOMAIN` values in `NAT_TRANSLATOR.py`.
- Ensure that Python and required modules (`tkinter`, `ldap3`) are correctly installed.
- Check system firewall settings to allow required LDAP ports.
- Use `cat /etc/resolv.conf` on Linux to verify DNS settings.

For further assistance, contact me with the  error messages and logs for debugging.

