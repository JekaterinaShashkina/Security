# Local

## Audit Questions:

https://github.com/01-edu/public/tree/master/subjects/cybersecurity/local/audit

## Task Overview:

This guide meticulously outlines the steps taken in the "Local" challenge. The task encompasses everything from determining the server's IP address to gaining root access and retrieving the flags.

## Step-by-Step Description:

1.  Virtual Machine Setup: I downloaded the 01-Local1.ova file and then imported it into VirtualBox via File – Import Appliance. Network settings were adjusted to bridge mode, in my case, the suitable adapter was Microsoft Network Adapter Multiplexor Driver.

2.  Using PowerShell with administrative rights and the command `Get-NetIPAddress | Where-Object { $_.AddressFamily -eq 'IPv4' -and $_.PrefixOrigin -eq 'Dhcp' }`, we obtained the host machine's address as **_192.168.2.1_**, thus the network address would be **_192.168.2.0/24_**.

3.  In the same PowerShell, the command nmap -sn **_192.168.2.0/24_** was used to find the addresses of all devices in this network. According to the results, the VM's address was **_192.168.2.16_**.

4.  Through nmap, three open ports were discovered:
    21: FTP with anonymous access.
    22: SSH.
    80: HTTP.
5.  FTP Exploration: Using the FTP Filezilla file manager, access was gained to the FTP server, where two files were found - **_template.html_** and **_life.c_**.

6.  Web Server Recon: Accessing the server's IP address through a browser displayed the HTML page content.

7.  Vulnerability scanning was conducted using Zap, which identified several potential vulnerabilities, but access to the server was not achieved.

8.  Remote File Execution: Anticipating the ability to execute uploaded files, a php-reverse-shell was obtained, customized for the local IP address, and uploaded via FTP.

9.  Gaining Shell Access: Launching a netcat listener and subsequently accessing the uploaded .php file on the web server allowed shell access to the server.

10. In the `/home` directory, two significant items were discovered - the `/shrek` user directory and the **_important.txt_** file, suggesting the execution of the `/.runme.sh` script.

11. Executing the script yielded no result, so the cat command was used to view the script itself, where a hashed password for the user was found: **_shrek:061fe5e7b95d5f98208d7bc89ed2d569_**

12. Using the service https://hashes.com/en/decrypt/hash, the hashed password was decrypted to reveal **_061fe5e7b95d5f98208d7bc89ed2d569:youaresmart_**.

13. With the login: **_shrek_** and the obtained password **_youaresmart_**, access was gained to the system with user rights. The command `sudo -l` provided the hint `“User shrek may run the following commands on ubuntu: (root) NOPASSWD: /usr/bin/python3.5”`.

14. To run Python 3.5, the command `sudo /usr/bin/python3.5` was entered.

15. In Python's interactive mode, the following code was entered to launch an interactive shell with superuser rights: `import os; os.system('/bin/bash')`. This code initiates a Bash shell with the rights of the user under whom Python was launched, in this case, root.

16. Root privileges were obtained. The only thing left was to find the flag. Using the command `ls -a`, the file **_root.txt_** was found. Viewing its contents revealed the text `“Congratulations, You have successfully completed the challenge! Flag: 01Talent@nokOpA3eToFrU8r5sW1dipe2aky”`

## Author

Catharin
