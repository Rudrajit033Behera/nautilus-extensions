#!/usr/bin/env python3

import subprocess

from gi.repository import GObject, Nautilus


class KiroMenuProvider(GObject.GObject, Nautilus.MenuProvider):
    def __init__(self):
        pass

    # === Right-click on a folder ===
    def get_file_items(self, files):
        # Only show if exactly one folder is selected
        if len(files) != 1 or not files[0].is_directory():
            return []

        item = Nautilus.MenuItem(
            name="KiroExtension::open_in_kiro",
            label="Open in Kiro",
            tip="Open this folder in Kiro",
        )

        item.connect("activate", self.open_in_kiro, files[0])
        return [item]

    # === Right-click on background (empty space) ===
    def get_background_items(self, current_folder):
        item = Nautilus.MenuItem(
            name="KiroExtension::open_current_in_kiro",
            label="Open in Kiro",
            tip="Open current folder in Kiro",
        )

        item.connect("activate", self.open_current_in_kiro, current_folder)
        return [item]

    # === Launch Kiro for selected folder ===
    def open_in_kiro(self, menu, file):
        filepath = file.get_location().get_path()
        subprocess.Popen(["kiro", filepath])

    # === Launch Kiro for current folder ===
    def open_current_in_kiro(self, menu, folder):
        filepath = folder.get_location().get_path()
        subprocess.Popen(["kiro", filepath])
