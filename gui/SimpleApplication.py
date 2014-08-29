from gi.repository import Gtk

class Application(object):
    def __init__(self, builder_path):
        """
        Top class for Gtk application.
        self.builder - default builder object loaded form file
        self.window - top level window object
        """
        self.builder = Gtk.Builder()
        self.builder.add_from_file(builder_path)
        self.window = self.builder.get_object("ApplicationWindow")
        self.name = "SimpleApplication"
        self.menu_file_quit =  self.get_object_by_name("MenuFileQuit")
        self.connect_me()

    def connect_me(self):
        #Connects gtk signals for window object
        self.window.connect("destroy", self.destroy_me)
        self.menu_file_quit.connect("activate", self.destroy_me)

    def run_me(self):
        #runs show_all() on window object and Gtk.main()
        self.window.show_all()
        Gtk.main()

    def destroy_me(self, widget):
        Gtk.main_quit()

    def get_builder(self):
        return self.builder

    def set_app_name(self, name):
        self.name = name

    def get_object_by_name(self, name):
        return self.builder.get_object(name)

