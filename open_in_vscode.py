#!/usr/bin/env python3

import subprocess

from gi.repository import GObject, Nautilus


class VSCodeMenuProvider(GObject.GObject, Nautilus.MenuProvider):
    def __init__(self):
        pass

    # === Right-click on a folder ===
    def get_file_items(self, files):
        # Only show if exactly one folder is selected
        if len(files) != 1 or not files[0].is_directory():
            return []

        item = Nautilus.MenuItem(
            name="VSCodeExtension::open_in_vscode",
            label="Open in VS Code",
            tip="Open this folder in Visual Studio Code",
        )

        item.connect("activate", self.open_in_vscode, files[0])
        return [item]

    # === Right-click on background (empty space) ===
    def get_background_items(self, current_folder):
        item = Nautilus.MenuItem(
            name="VSCodeExtension::open_current_in_vscode",
            label="Open in VS Code",
            tip="Open current folder in Visual Studio Code",
        )

        item.connect("activate", self.open_current_in_vscode, current_folder)
        return [item]

    # === Launch VS Code for selected folder ===
    def open_in_vscode(self, menu, file):
        filepath = file.get_location().get_path()
        subprocess.Popen(["code", filepath])

    # === Launch VS Code for current folder ===
    def open_current_in_vscode(self, menu, folder):
        filepath = folder.get_location().get_path()
        subprocess.Popen(["code", filepath])
