# Raschio File Transfer Tools

## Because sometimes Dropbox is overkill.

Raschio File Transfer Tools is a set of command line tools for sending files between computers on a LAN.

## Usage

### Sending

In PowerShell navigate to the directory containing the file you want to send, and then type `send <filename>`. This puts your file on the network.  
**Note: files sent using this command will be only be receivable by one (1) connection. If you want to get it to multiple computers, you will have to use the `send` tool for each instance.**

Alternatively, you can right-click a file in Windows Explorer, and then click on the `File Transfer Tools` option in the `Send To` submenu.

### Receiving

`$ receive <ip address> <directory>`  
and then type in the required information when prompted. Please note that these requirements are optional; if you do not enter an argument you will be prompted to enter the necessary information.

## Installation

For a standard installation, download the installer (`Install Raschio File Transfer Tools.exe`) to your computer, and then run it.
