#!/usr/bin/env python3

import os
import subprocess

from gi.repository import GObject, Nautilus

TERMINATOR_PATH = "/usr/bin/terminator"


class TerminatorMenuProvider(GObject.GObject, Nautilus.MenuProvider):
    def __init__(self):
        pass

    def get_file_items(self, files):
        if len(files) != 1 or not files[0].is_directory():
            return []
        item = Nautilus.MenuItem(
            name="TerminatorExtension::open_in_terminator",
            label="Open in Terminator",
            tip="Open this folder in a Terminator terminal",
        )
        item.connect("activate", self.open_in_terminator, files[0])
        return [item]

    def get_background_items(self, current_folder):
        item = Nautilus.MenuItem(
            name="TerminatorExtension::open_current_in_terminator",
            label="Open in Terminator",
            tip="Open current folder in a Terminator terminal",
        )
        item.connect("activate", self.open_current_in_terminator, current_folder)
        return [item]

    def open_in_terminator(self, menu, file):
        filepath = file.get_location().get_path()
        subprocess.Popen([TERMINATOR_PATH, "--working-directory", filepath], env=os.environ.copy())

    def open_current_in_terminator(self, menu, folder):
        filepath = folder.get_location().get_path()
        subprocess.Popen([TERMINATOR_PATH, "--working-directory", filepath], env=os.environ.copy())
