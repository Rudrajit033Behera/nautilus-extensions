# Nautilus Extensions

A collection of Nautilus file manager extensions that add convenient context menu options for opening folders in different applications.

## Features

- **Open in Terminator**: Adds a context menu option to open the selected folder in a Terminator terminal
- **Open in VS Code**: Adds a context menu option to open the selected folder in Visual Studio Code
- **Open in Kiro**: Adds a context menu option to open the selected folder in Kiro

## Requirements

- Python 3
- Nautilus file manager
- Python-Nautilus `python3-nautilus`
- GNOME libraries (`python3-gi` and `gi.repository`)
- Terminator terminal (for the Terminator extension)
- Visual Studio Code (for the VS Code extension)
- Kiro (for the Kiro extension)

## Installation

1. Copy the extension files to your Nautilus extensions directory:

   ```bash
   sudo cp open_in_terminator.py open_in_vscode.py open_in_kiro.py ~/.local/share/nautilus-python/extensions
   ```

2. Restart Nautilus to load the extensions:
   ```bash
   nautilus -q
   ```

## Usage

- Right-click on a folder and select "Open in Terminator" or "Open in VS Code" or "Open in Kiro"
- Right-click on empty space in a folder and select "Open in Terminator" or "Open in VS Code" to open the current folder

## License

This project is open source and available under the MIT License.
