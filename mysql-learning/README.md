# MySQL Installation on Windows11
Time Update: 2024/07/24

## Step 0: Installing the Microsoft Visual C++

Download and install the Microsoft Visual C++ Redistributable latest supported from the following link： https://learn.microsoft.com/en-us/cpp/windows/latest-supported-vc-redist?view=msvc-170

Check if you installed from "control panel>Program>Program and Features". Check this Link: https://www.youtube.com/watch?v=8PGkqi0FgvY

## Step 1: Downloading the correct MySQL Installer for Windows

1. You can download the MySQL Installer for Windows via this link:
https://dev.mysql.com/downloads/installer
2. On that page, ensure that the latest MySQL version is selected (current version is 8.0.39). Make sure that you download and start the MySQL full-size offline installer — it's the one with a larger installer file size (and not smaller-sized web installer). 
3. After you click the ‘Download’ button shown above, you will be taken to another page where you need to click ‘No thanks, just start my download.’. The download should then start. After the download finishes, run the downloaded .msi installer file.

## Step 2: Installing MySQL on Windows
You should follow the steps of MySQL installer, but below are some important settings: 
- For the "Setup Type", make sure to choose "Full".
On the "Installation" screen that follows, click the "Execute" button.
- On the "Type and Networking", the "Port" should already be set to 3306 — make sure that you keep it at that number, and leave all the other pre-defined settings and click the "Next" button
- In the "Authentication Method" screen that follows, make sure that the "Use Strong Password Encryption for Authentication (RECOMMENDED)" option is selected
specify your MySQL root password. Make sure it’s a strong password, and absolutely make sure to remember the root password. You will need to use the root password later in the installer, and, importantly, you will need to know the root password to use MySQL after installing it.
- In the "Windows Service" step that follows, everything should already be pre-configured. Select "Configure MySQL Server as a Windos Service". Windows Service Name: MySQL80. Select "Start the MySQL Server at System StartUp".
- For the "Server File Permissions", Select "Yes, grant full access to the user running the Windows Service ..."

## Step 3: Starting MySQL Workbench
When MySQL Workbench opens, click the "local instance".

## Step 4: Testing installation
method 1: can open Workbench
method 2: open "command line client"

## Reference
1. Note from Udemy course: https://coursetutorials.notion.site/MySQL-Installation-on-Windows-acec3db643734b5ea8395daeba24ee92