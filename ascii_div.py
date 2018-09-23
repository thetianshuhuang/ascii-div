
"""ASCII Div drawing command"""

import os
import sublime_plugin

from .ascii_defs import DIVIDERS


# -----------------------------------------------------------------------------
#
#                               Insert ASCII Art
#
# -----------------------------------------------------------------------------
class insertasciiartCommand(sublime_plugin.WindowCommand):

    def run(self, type):

        try:
            self.func = DIVIDERS[type]
            self.window.show_input_panel(
                "Div Text:", "", self.on_done, None, None)
        except KeyError:
            raise Exception("Undefined Div Type.")

    def on_done(self, text):

        file_type = os.path.splitext(self.window.active_view().file_name())[1]

        div = self.func(text, file_type)

        for region in self.window.active_view().sel():

            self.window.run_command(
                "inserttext",
                {"text": div, "point": region.begin()})


# -----------------------------------------------------------------------------
#
#                          Insert Text Helper Command
#
# -----------------------------------------------------------------------------
class inserttextCommand(sublime_plugin.TextCommand):

    def run(self, edit, text, point):

        self.view.insert(edit, point, text)
