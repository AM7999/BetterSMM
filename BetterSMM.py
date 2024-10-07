from asciimatics.widgets import Frame, TextBox, Layout, Label, Divider, Text, \
    CheckBox, RadioButtons, Button, PopUpDialog, TimePicker, DatePicker, DropdownList, PopupMenu
from asciimatics.effects import Background
from asciimatics.event import MouseEvent
from asciimatics.scene import Scene
from asciimatics.screen import Screen
from asciimatics.exceptions import ResizeScreenError, NextScene, StopApplication, \
    InvalidFields
from asciimatics.parsers import AsciimaticsParser

import sys
import re
import requests
import json
import os

# class config:
#     pathToSatisfactory = ""
#     # This is an un-inclusive variable to be used for the modsInstalled array
#     modsInstalled = 0
#     modsInstalledArray = []


def findFile(filename):
    for root, dirs, files in os.walk("%USERPROFILE%\\AppData\\Local\\SMM-py"):
        if filename in files:
            return True
        else:
            return False

url = "https://api.ficsit.app/v1"

class mainFrame(Frame):
    def __init__(self, screen):
        super(mainFrame, self).__init__(screen,
                                        int(screen.height * 2 // 3),
                                        int(screen.width * 2 // 3),
                                        #data=startForm,
                                        has_shadow=True,
                                        title="Satisfactory Mod Manager: Main")
        layout = Layout([1, 18, 1])
        self.add_layout(layout)

        layout.add_widget(Divider(height=2), 1)
        layout.add_widget(Button("Quit", self._quit), 1)
        #layout.add_widget(Button("Settings", self.SwitchFrame), 1)
        self.fix()
    
    def _quit(self):
        self.__scene.add_effect(
            PopUpDialog(self.screen,
            ["Yes", "No"],
            has_shadow=True,
            on_close=self._quit_on_yes)
        )
    
    @staticmethod
    def _quit_on_yes(selected):
        if selected == 0:
            raise StopApplication("User requested exit")

settingsData = {
    
}

# class settingsFrame(Frame):
#     def __init__(self, screen):
#         super(settingsFrame, self).__init__(screen,
#                                             int(screen.height * 2 // 3),
#                                             int(screen.width * 2 // 3),
#                                             )


def main(screen, scene):
    screen.play([Scene([
        Background(screen),
        mainFrame(screen)
        ], -1)], stop_on_resize=True, start_scene=scene, allow_int=True)

last_scene = None
while True:
    try:
        Screen.wrapper(main, catch_interrupt=False, arguments=[last_scene])
        sys.exit(0)
    except ResizeScreenError as e:
        last_scene = e.scene