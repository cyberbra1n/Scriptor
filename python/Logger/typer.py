import sys
import time
import datetime
import os.path
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

class DirEventHandler(FileSystemEventHandler):
    def on_modified(self, event):
        self.updated = True

    def get_state_updated(self):
        return self.updated


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
            self.file_last_modified = os.path.getmtime(self.file_path)
            self.file_to_list()

    def file_to_list(self):
        self.fhandler = open(self.file_path, 'r')
        for each in self.fhandler:
            if each != '' and each !="\n":
                date_time = self.get_datetime_now()
                self.add_string(each, date_time)

    def get_datetime_now(self):
            date_time = datetime.datetime.now()
            return date_time.strftime("%d %b |%H:%M:%S") # time format


    def add_string(self, string, date_time):
        self.string_buffer.append(str(date_time) + "| " + string)
        self.new_to_buffer = self.new_to_buffer + 1

    def get_first(self):
        return self.string_buffer[0]

    def pop_first(self):
        string = self.string_buffer[0]
        self.string_buffer.remove(string)
        self.new_to_buffer = self.new_to_buffer - 1
        return string
    
    def execute_one(self):
        if self.new_to_buffer > 0:
            string = self.get_first()
            for each in string:
                sys.stdout.write(each)
                sys.stdout.flush()
                time.sleep(self.update_interval)

    def get_last_line(self):
        return self.fhandler.readlines()[0]

    def wait_for_file_update(self):
        self.observer.schedule(self.event_handler, path='.', recursive=False)
        self.observer.start()
        try:
            while True:
                time.sleep(1)
        except KeyboardInterrupt:
            self.observer.stop()
        self.observer.join()

            #modified_time = os.path.getmtime(self.file_path)
            #if modified_time == self.file_last_modified:
            #    return
            #    
            #else:
            #    self.new_to_buffer += 1
            #    now = self.get_datetime_now()
            #    self.string_buffer.append(now + "| " + str(self.get_last_line()))
            #    self.file_last_modified = modified_time
            #    #time.sleep(2)
            #    #return self.pop_first()
            #    #print "break"
            #    #return True
                

    def execute(self):
        #while True:
        if self.new_to_buffer > 0:
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
