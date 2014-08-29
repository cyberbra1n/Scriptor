from gui.SimpleApplication import Application
from models.ListModel import ListModel
from gui.PluginLoader import PluginLayout

class Scriptor(Application):
    def __init__(self):
        super(Scriptor, self).__init__("gui/Scriptor.glade")
        self.registrated_scripts = []
        self.name = "Scriptor"
        self.options_container = self.get_object_by_name("OptionsContainer")
        self.options_layout = PluginLayout(self.builder)

        self.tree_view = self.get_object_by_name("ApplicationList")
        self.tree_view.set_model(self.get_object_by_name("ApplicationListModel"))

        #load layout by app : ex
        self.load_layout_by_app(self.options_layout.box)

        #populates OptionBox TODO: make in loop and for all
        #self.add_script_to_list()
        self.connect_signals()

    def load_layout_by_app(self, app_options_layout_toplevel):
        """reparents OptionsContainer(box) widget with provided layout """
        app_options_layout_toplevel.reparent(self.options_container)

    def connect_signals(self):
        self.builder.get_object("AddScriptButton").connect("clicked", self.run_add_dialog)
        self.builder.get_object("RemoveScriptButton").connect("clicked", self.remove_script_from_list)

    def run_add_dialog(self, widget):
        self.add_script_to_list("script_name", "script_dir")
        pass

    def add_script_to_list(self, script_name, script_dir):
        print "Implement: add_script_to_list"
        pass

    def remove_script_from_list(self, widget):
        print "Implement: remove_script_from_list"
        pass


    def get_applications_list(self):
        #probably should import new module for model handling:
        #ideas: database or file objects (maybe json??)
        pass





if __name__ == "__main__":
    app = Scriptor()
    app.set_app_name("Scriptor")
    print "App " + app.name + " Created"
    print "Runing App..."
    app.run_me()
    print "Bye bye"
    
