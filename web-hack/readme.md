# WEB hack

## Task Overview

1. Deploy the DVWA web platform on a virtual machine or local server.
2. Find at least 3 vulnerabilities.
3. Develop a c99, r57 type shell. The PHP shell should allow you to add a file, delete a file, and execute a command.

## Audit questions

https://github.com/01-edu/public/tree/master/subjects/cybersecurity/web-hack/audit

### Deploying the web platform on a virtual machine with Linux Debian OS installed. After setting up the VM, install the following packages:

`apt-get -y install apache2 mariadb-server php php-mysqli php-gd libapache2-mod-php`

- Download the DVWA repository or extract the zip file.
- Move the contents of the DVWA folder to the root directory of the web server. For Apache, the default is **_/var/www/html_**.
- Go to the **_/var/www/html/config_** directory, copy **_config.inc.php.dist_** to **_config.inc.php_**:
- Set up the database. When using MariaDB, you need to create a new user; for this, connect to the database as the root user and use the following commands:
  `mysql> create database dvwa;
Query OK, 1 row affected (0.00 sec)
mysql> create user dvwa@localhost identified by 'p@ssw0rd';
Query OK, 0 rows affected (0.01 sec)
mysql> grant all on dvwa.\* to dvwa@localhost;
Query OK, 0 rows affected (0.01 sec)
mysql> flush privileges;
Query OK, 0 rows affected (0.00 sec)`

- Make sure that all necessary PHP extensions are installed. For DVWA, **_php-gd, php-mysqli_**, and other extensions are usually required, which are typically installed along with the php package.
- Change the permissions on the DVWA directory so that the web server can write data to it.
- Restart Apache to apply all changes.
- Open a web browser and go to http://localhost/setup.php to finish setting up DVWA. Click on the **_Create / Reset Database_** button.

On the login page of Damn Vulnerable Web Application (DVWA), you must enter the user credentials that are set by default in the application. For DVWA, the standard credentials are usually:

`Username: admin
   Password: password`

### Exploring Vulnerabilities

### SQL Injection

The practice of inserting or "injecting" SQL code into an application, which can lead to unauthorized data access. SQL injection is a type of attack on an application, where the attacker inserts or "injects" SQL code into the application's input data to execute developer-unanticipated commands or database queries. This can allow the attacker to access, modify, delete data, or perform operations that could compromise data integrity or system security.

- Select SQL Injection in DVWA: In the main menu of DVWA, select the SQL Injection section.

  ![sql injection](/img/SQL%20injaction.png)

- Study the injection entry points: Usually, these are text fields where a user can enter data, such as a username or ID.
- Try simple injections: At the "Low" security level, the system will not filter your input, so you can start with simple injections. For example, if you see a field for entering a username, try entering ' OR '1'='1. This may result in a query execution that is always true, and possibly return data from the database.
- If the injection is successful, the application may display data from the database, such as a list of users or their passwords.

  ![result sql injection](/img/SQl%20injection%20result.png)

Protection against SQL injections includes several key practices and techniques that help ensure the security of your web applications and databases. Here are the main ones:

1. Use Prepared Statements with parameterized queries.
2. Use ORM (Object-Relational Mapping) frameworks.
3. Limit database access rights.
4. Use built-in database functions to sanitize input.
5. Validate and sanitize input data.
6. Use web firewalls.
7. Regularly update and patch.
8. Use security testing tools.
9. Education and awareness.

Remember, there is no single way to protect against all types of SQL injections, so combining different methods will provide the best protection.

### Command Injection

Entering arbitrary OS commands that the server then executes. In the context of Damn Vulnerable Web Application (DVWA), Command Injection allows you to explore how such attacks can be carried out and how to protect against them.

- Set the security level. Set the security level in DVWA to "Low" to facilitate the execution of a Command Injection attack.
- Go to the Command Injection section. In the main menu of DVWA, select the "Command Injection" section. You will see an interface offering to enter data, such as an IP address to execute the ping command.

  ![command injection](/img/Command%20Injection.png)

- DVWA allows you to enter an IP address, which is then used in the ping command executed on the server. The task is to modify this request so that the server executes additional commands.
- Add command separators to the IP address, such as `;, &&, or |`, and then enter an additional command you want to execute. For example: `127.0.0.1; ls`. This input will try to execute the ls command on the server after executing the ping command for the address **_127.0.0.1_**, which may result in displaying a list of files in the current server directory.
- After submitting the request, observe the output on the screen. If your command injection is successful, you will see the result of the executed command.

  ![result command injection](/img/Command%20Injection%20result.png)

### Protection against Command Injection:

Input sanitization: All input data must be thoroughly checked and cleaned of potentially dangerous characters and constructions.
Use of high-level abstractions: Use programming language functions and libraries that do not allow direct execution of system commands.
Restriction of rights: Run applications and scripts on the server from a user with the minimum necessary permissions.

### Stored Cross-Site Scripting (XSS)

A type of XSS attack where a malicious script is saved on the target server (for example, in a database, on a forum, in blog comments, etc.) and then executed in the user's browser when the infected content is loaded. In the context of Damn Vulnerable Web Application (DVWA), you can practice and study Stored XSS by following these steps:

- Select the vulnerability. In the main menu of DVWA, choose "XSS Stored". This section contains functionality that simulates a feature where users can leave messages or comments, such as a guest book.

  ![XSS](/img/XSS.png)

- Familiarize yourself with the interface that allows leaving messages. Typically, there is a text field for entering a message and a button to send it.
- In the text field, enter malicious JavaScript code. For example, you can use a simple script to display a popup window: `<script>alert('XSS');</script>` Send the message. The malicious code will be saved on the server.
- When any user (including you) loads the page that displays the saved messages, the malicious script will be executed in their browser. This confirms the success of the Stored XSS attack.

  ![XSS result](/img/XS%20result.png)

Protection against Stored XSS attacks (or Persistent XSS) includes several key strategies that provide multi-layered protection. Here are the main methods of protection:

- Data encoding: This is the most important step. All data entered by the user and then displayed on the page must be encoded so that the browser interprets them as data, not as executable code.
- Using a list of allowed tags.
- Prepared statements and ORM.
- Content Security Policy (CSP).
- HTTP-only and Secure flags for cookies.
- Data validation and sanitization.
- Updating and patching.
- Using auto-escaping in templates

### PHP Shell

Creating a web shell similar to c99 or r57 involves writing a PHP script that allows performing certain actions on the server, such as adding and deleting files, as well as executing commands.

Adding the Script
Go to the File Upload tab and upload the script `web-shell.php`.

![shell upload](/img/php-shell%20upload.png)

Navigate to the page where the script was saved.
In my case, it is `localhost/hackable/uploads/web-shell.php`.

![shell](/img/php-shell.png)

Attempt to upload a file.

![file upload](/img/file%20upload.png)

![file](/img/uploaded.png)

Attempt to execute the uploaded file.

![execute file](/img/shell-command.png)

![cat command](/img/cat%20command.png)

![cat result](/img/result%20cat.png)

At the end of our experiments, delete the file.

![deleting](/img/delete%20shell.png)

![result deleting](/img/result%20shell%20deleting.png)

In this way, any malicious file can be uploaded to the site and any harmful commands executed.
Protecting a web application from malicious PHP shells like c99 and r57 requires a comprehensive approach, including the following measures: restricting file uploads, verifying and validating input data, using safe PHP functions, a robust application architecture, proper server configuration, using a web application firewall (WAF), and others.

## Author

Catharin
