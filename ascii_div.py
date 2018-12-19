
"""ASCII Div drawing command"""

import os
import sublime_plugin

from . import ascii_defs
from functools import partial


# -----------------------------------------------------------------------------
#
#                               Insert ASCII Art
#
# -----------------------------------------------------------------------------
class insertasciiartCommand(sublime_plugin.WindowCommand):

    def run(self, divtype):

        if divtype.startswith('figlet_'):
            self.func = partial(ascii_defs.div_figlet, font=divtype[7:])
        else:
            self.func = getattr(ascii_defs, "div_" + divtype)

        self.window.show_input_panel(
            "Div Text:", "", self.on_done, None, None)

    def on_done(self, text):

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


# -----------------------------------------------------------------------------
#
#                          Insert Text Helper Command
#
# -----------------------------------------------------------------------------
class inserttextCommand(sublime_plugin.TextCommand):

    def run(self, edit, text, point):

        self.view.insert(edit, point, text)
