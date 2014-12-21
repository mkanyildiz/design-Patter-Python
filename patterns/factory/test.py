# coding=utf-8
from factory.GtkUIFactory import GtkUIFactory
from factory.QtUIFactory import QtUIFactory


class test:
    if __name__ == "__main__":
        gnome = True
        kde = not gnome

        # What environment is available?
        if gnome:
            ui = GtkUIFactory()
        elif kde:
            ui = QtUIFactory()

        # Build the UI
        toolbox = ui.getToolboxWindow()
        layers  = ui.getLayersWindow()
        main    = ui.getMainWindow()

        # Let's see what have we recieved
        print("%s:%s" % (toolbox.getToolkit(), toolbox.getType()))
        print ("%s:%s" % (layers.getToolkit(), layers.getType()))
        print ("%s:%s" % (main.getToolkit(), main.getType()))
 