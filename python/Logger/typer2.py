import sys
import time
import datetime
import os.path
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

class DirEventHandler(FileSystemEventHandler):
    def __init__(self):
        super(DirEventHandler, self).__init__()
        self.new_line_buffer = []

    def set_file_path(self, file_path):
        self.file_to_watch = file_path

    def set_type_interval(self, type_interval):
        self.type_interval = type_interval

    def get_datetime_now(self):
            date_time = datetime.datetime.now()
            return date_time.strftime("%d %b |%H:%M:%S") # time format

    def on_modified(self, event):
        self.updated = True
        self.new_line_buffer.append(self.get_last_line())
        self.type_buffer()

    
    def get_last_line(self):
        if self.file_to_watch:
            file_handler = open(self.file_to_watch, 'r')
            last_line = file_handler.readlines()[-1]
            return last_line
        else:
            print "no file is set"

    def type_buffer(self):
        if len(self.new_line_buffer) > 0:
            for each in self.new_line_buffer[-1]:
                sys.stdout.write(each)
                sys.stdout.flush()
                time.sleep(self.type_interval)



class TypeString(object):
    def __init__(self, update_interval, file_path=''):
        super(TypeString, self).__init__()
        self.update_interval = update_interval
        self.string_buffer = []
        self.new_to_buffer = 0

        self.event_handler = DirEventHandler()
        self.observer = Observer()

        if file_path:
            self.file_path = file_path
            self.event_handler.set_file_path(self.file_path) #interface
            self.event_handler.set_type_interval(self.update_interval) #interface
            self.file_last_modified = os.path.getmtime(self.file_path)
            self.file_to_list()

    def file_to_list(self):
        self.fhandler = open(self.file_path, 'r')
        for each in self.fhandler:
            if each != '' and each !="\n":
                #date_time = self.get_datetime_now()
                self.add_string(each)

    def add_string(self, string):
        self.string_buffer.append( "from file:| " + string)
        self.new_to_buffer = self.new_to_buffer + 1

    def pop_first(self):
        string = self.string_buffer[0]
        self.string_buffer.remove(string)
        self.new_to_buffer = self.new_to_buffer - 1
        return string
    
    def wait_for_file_update(self):
        self.observer.schedule(self.event_handler, path='.', recursive=False)
        self.observer.start()
        try:
            while True:
                time.sleep(1)
                pass
        except KeyboardInterrupt:
            self.observer.stop()
            exit("\nBye")
        self.observer.join()

    def execute(self):
        while self.new_to_buffer > 0:
            string = self.pop_first()
            for each in string:
                sys.stdout.write(each)
                sys.stdout.flush()
                time.sleep(self.update_interval)
            self.execute()
        else:
            self.wait_for_file_update()

if __name__ == "__main__":
    typer = TypeString(0.03, 'test_file')
#    typer.add_string("Wake up cYber!")
#    typer.add_string("The day has just started!")
    typer.execute()
