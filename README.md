
                            
          
    ██╗  ██╗███████╗██╗   ██╗    ██╗      ██████╗  ██████╗  ██████╗ ███████╗██████╗ 
    ██║ ██╔╝██╔════╝╚██╗ ██╔╝    ██║     ██╔═══██╗██╔════╝ ██╔════╝ ██╔════╝██╔══██╗
    █████╔╝ █████╗   ╚████╔╝     ██║     ██║   ██║██║  ███╗██║  ███╗█████╗  ██████╔╝
    ██╔═██╗ ██╔══╝    ╚██╔╝      ██║     ██║   ██║██║   ██║██║   ██║██╔══╝  ██╔══██╗
    ██║  ██╗███████╗   ██║       ███████╗╚██████╔╝╚██████╔╝╚██████╔╝███████╗██║  ██║
    ╚═╝  ╚═╝╚══════╝   ╚═╝       ╚══════╝ ╚═════╝  ╚═════╝  ╚═════╝ ╚══════╝╚═╝  ╚═╝
    --------------------------------------------------------------------------------
                              python cli key logging script


### What is a Key logger?
A keylogger script is a program designed to covertly record and log keystrokes on a computer, capturing sensitive information. It can be used for various purposes, including both legitimate monitoring and malicious activities.


## Requirement (Keylogger.py)
This script depends on the following three libraries: datetime, threading, and keyboard. Two of these, datetime and threading, are already pre-installed with Python. However, the keyboard library needs to be installed to run this script.

pip3

      pip3 install keyboard

pip

      pip install keyboard



## Requirement (Keylogger_script2.py)
This script depends on the following three libraries: datetime, threading, and pynput. Two of these, datetime and threading, are already pre-installed with Python. However, the pynput library needs to be installed to run this script.

pip3

      pip3 install pynput

pip

      pip install pynput


## Usage 
Both scripts do pretty much the same thing, but the keylogger.py one needs you to have admin rights to run because it uses the keyboard module. The other one, keylogger_script2.py, can run without you needing admin rights. Once you run either of them, they start saving all the keystrokes and put them in the current directory. The name of the file has the date and time when you started the script and the date and time when it was saved.


#### To run keylogger.py

       sudo python keylogger.py 

#### To run keylogger_script2.py

       python keylogger_script2.py 

