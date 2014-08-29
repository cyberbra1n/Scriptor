
import subprocess


class BackupRouter(object):
    def __init__(self, ip):
        super(BackupRouter, self).__init__()
        self.PIPE = subprocess.PIPE
        self.ip = ip
        self.save_dir = None
        self.file_paths = []

    def set_file_paths(self):
        print "Enter path for file to be monitored:\n"
        while True:
            new_file_path = raw_input()
            if new_file_path == '':
                print "Folowing files has been added:"
                print self.file_paths
                break

            else:
                print "Next file or Enter for continue"
                self.add_file_path(new_file_path)

        
    def add_file_path(self, file_path):
        self.file_paths.append(file_path)

    def run(self):
        self.set_file_paths()


if __name__ == "__main__":
    backup_cc = BackupRouter('10.0.0.1')
    backup_cc.run()

