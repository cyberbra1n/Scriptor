from gi.repository import Gtk

class PluginLayout(object):
    def __init__(self, builder):
        builder.add_from_file("./gui/ArduinoDaemon.glade")
        self.box = builder.get_object("OptionsBox")

