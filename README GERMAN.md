# **NAT-Übersetzer Einrichtungsanleitung**
https://github.com/Hondanx/for_rinaszeg.git

Diese Anleitung enthält Schritt-für-Schritt-Anweisungen zur Einrichtung und Ausführung des NAT-Übersetzerskripts auf Windows und Linux. Das Paket enthält drei Skripte:

1. **NAT_TRANSLATOR.py** – Das Hauptskript zur NAT-Konfiguration.
2. **installing_depends_for_Linux.sh** – Ein Skript zur Installation der Voraussetzungen unter Linux.
3. **installing_depends_for_win.bat** – Ein Skript zur Installation der Voraussetzungen unter Windows.

Bevor Sie die Skripte ausführen, stellen Sie sicher, dass Sie die folgenden Variablen in `NAT_TRANSLATOR.py` mit den Details Ihres Active Directory-Servers aktualisieren:

```python
AD_SERVER = "ldap://Ihr AD-SERVERNAME"
AD_DOMAIN = "IHR DOMAINNAME"
```

---
## **Abschnitt 1: Windows-Anleitung**

### **Schritt 1: Verbindung prüfen**
Bevor Sie fortfahren, stellen Sie sicher, dass Ihr System mit dem Active Directory (AD)-Server kommunizieren kann.

1. **DNS-Auflösung überprüfen:**
   ```powershell
   nslookup Ihr_AD_Servername
   ```

2. **Verbindung zum AD-Server testen:**
   ```powershell
   Test-Connection Ihr_AD_Servername -Count 4
   ```

3. **Sicherstellen, dass die LDAP-Ports offen sind (389 für Standard, 636 für sicheres LDAP):**
   ```powershell
   Test-NetConnection -ComputerName Ihr_AD_Servername -Port 389
   Test-NetConnection -ComputerName Ihr_AD_Servername -Port 636
   ```

Falls einer dieser Tests fehlschlägt, überprüfen Sie Ihre Netzwerkeinstellungen und Firewallregeln.

### **Schritt 2: Abhängigkeiten installieren**
Führen Sie das bereitgestellte Batch-Skript aus, um die erforderlichen Abhängigkeiten zu installieren:
   ```powershell
   installing_depends_for_win.bat
   ```

### **Schritt 3: NAT-Übersetzer-Skript ausführen**
Sobald die Abhängigkeiten installiert sind, starten Sie das Hauptskript:
   ```powershell
   python NAT_TRANSLATOR.py
   ```

---
## **Abschnitt 2: Linux-Anleitung**

### **Schritt 1: Verbindung prüfen**
Bevor Sie das Skript ausführen, stellen Sie sicher, dass Ihr Linux-System den AD-Server erreichen kann.

1. **DNS-Auflösung überprüfen:**
   ```bash
   nslookup Ihr_AD_Servername
   ```

2. **Den AD-Server anpingen:**
   ```bash
   ping -c 4 Ihr_AD_Servername
   ```

3. **Sicherstellen, dass die LDAP-Ports offen sind:**
   ```bash
   nc -zv Ihr_AD_Servername 389
   nc -zv Ihr_AD_Servername 636
   ```

Falls diese Tests fehlschlagen, überprüfen Sie Ihre Netzwerkeinstellungen.

### **Schritt 2: Abhängigkeiten installieren**
Führen Sie das Linux-Installationsskript aus:
   ```bash
   chmod +x installing_depends_for_Linux.sh
   ./installing_depends_for_Linux.sh
   ```

### **Schritt 3: NAT-Übersetzer-Skript ausführen**
Sobald die Abhängigkeiten installiert sind, starten Sie das Skript:
   ```bash
   python3 NAT_TRANSLATOR.py
   ```

---
## **Fehlersuche**
- Falls die Authentifizierung fehlschlägt, überprüfen Sie die Werte für `AD_SERVER` und `AD_DOMAIN` in `NAT_TRANSLATOR.py`.
- Stellen Sie sicher, dass Python und die erforderlichen Module (`tkinter`, `ldap3`) korrekt installiert sind.
- Überprüfen Sie die Firewall-Einstellungen, um sicherzustellen, dass die erforderlichen LDAP-Ports zugelassen sind.
- Verwenden Sie `cat /etc/resolv.conf` unter Linux, um die DNS-Einstellungen zu überprüfen.

Falls weitere Hilfe benötigt wird, kontaktieren Sie mich mit den Fehlermeldungen und Logs zur Fehlerbehebung.

