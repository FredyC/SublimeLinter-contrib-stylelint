#
# linter.py
# Linter for SublimeLinter3, a code checking framework for Sublime Text 3
#
# Written by @kungfusheep
# Copyright (c) 2016 @kungfusheep
#
# License: MIT
#
"""This module exports the Stylelint plugin class."""

import os

from SublimeLinter.lint import NodeLinter, util

class Stylelint(NodeLinter):
    """Provides an interface to stylelint."""

    syntax = ('css', 'css3', 'sass', 'scss', 'postcss')
    executable = 'stylelint'
    npm_name = 'stylelint'
    error_stream = util.STREAM_BOTH
    config_file = ('--config', '.stylelintrc', '~')
    tempfile_suffix = 'css'
    regex = (
        r'^(?P<line>[0-9]+)\:(?P<col>[0-9]+)(?P<message>.+)'
    )

    def cmd(self):
        """Return a tuple with the command line to execute."""

        path = self.executable_path

        if not path:
            result = self.context_sensitive_executable_path([self.executable])

            if result[1]:
                path = result[1]

        command = [path]
        return command