
#     ___   _____ ______________   ____  _____    __
#    /   | / ___// ____/  _/  _/  / __ \/  _/ |  / /
#   / /| | \__ \/ /    / / / /   / / / // / | | / /
#  / ___ |___/ / /____/ /_/ /   / /_/ // /  | |/ /
# /_/  |_/____/\____/___/___/  /_____/___/  |___/

"""ASCII Div drawing command"""

import os
import sublime_plugin

from . import ascii_defs
from functools import partial


class insertasciiartCommand(sublime_plugin.WindowCommand):
    """ASCII art handler command

    Examples
    --------
    In Default.sublime-command:
    {
        "caption": "ASCII Art: Add small divider",
        "command": "insertasciiart",
        "args": {"divtype": <divider type>}
    },
    The divider type can be 'small', 'medium', 'large', or 'figlet_<font>'.
    """

    def run(self, divtype):

        if divtype.startswith('figlet_'):
            self.func = partial(ascii_defs.div_figlet, font=divtype[7:])
        else:
            self.func = getattr(ascii_defs, "div_" + divtype)

        self.window.show_input_panel(
            "Div Text:", "", self.on_done, None, None)

    def on_done(self, text):
        """Command to run after dialog box completed

        Parameters
        ----------
        text : str
            String passed by self.window.show_input_panel
        """

        file_type = os.path.splitext(self.window.active_view().file_name())[1]
        active = self.window.active_view()

        for region in active.sel():

            padding = active.rowcol(region.end())[1]
            div = self.func(text, file_type, padding)

            self.window.run_command(
                "inserttext", {
                    "text": div,
                    "point": active.text_point(
                        active.rowcol(region.end())[0], 0)
                })


class inserttextCommand(sublime_plugin.TextCommand):
    """Base insert text command

    Since sublime 'edit' objects can only be created by TextCommands, any
    view edits must pass through an external command.

    Usage
    -----
    self.window.run_command(
        "inserttext", {
            "text": text_to_insert,
            "point": sublime_text_point
        })
    """

    def run(self, edit, text, point):

        self.view.insert(edit, point, text)
