#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Copyright (c) 2017, Lars Andre Landås (landas@gmail.com)
# All rights reserved.
#
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions are met:
#
# 1. Redistributions of source code must retain the above copyright notice, this
#    list of conditions and the following disclaimer.
# 2. Redistributions in binary form must reproduce the above copyright notice,
#    this list of conditions and the following disclaimer in the documentation
#    and/or other materials provided with the distribution.
#
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" AND
# ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED
# WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE
# DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT OWNER OR CONTRIBUTORS BE LIABLE FOR
# ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES
# (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES;
# LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND
# ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT
# (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS
# SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
#
# The views and conclusions contained in the software and documentation are those
# of the authors and should not be interpreted as representing official policies,
# either expressed or implied, of the FreeBSD Project.

import plugin_normal
import plugin_random
import sys

class JLogic:

    def __init__(self):
        self.plugin = None
        self.plugin_id = 0;

    def click(self, button):
        data = ""
        if self.plugin != None:
        
            if button == 'a':
                data = self.plugin.onAclick()
                sys.stdout.write('\b')
            if button == 'b':
                data = self.plugin.onBclick()
            if button == 's':
                self.plugin_id = self.plugin_id + 1
                if self.plugin_id > 1:
                    self.plugin_id = 0

                if self.plugin_id == 0:
                    self.plugin = plugin_normal.JKPlugin_Normal
                if self.plugin_id == 1:
                    self.plugin = plugin_random.JKPlugin_Random

        sys.stdout.write(data)
        sys.stdout.flush()

    def set_plugin(self, plugin):
        self.plugin = plugin
