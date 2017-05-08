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

import evdev
import re
import jinput
import plugin_normal
import threading
import time
import sys
import jlogic

print("Starting jkeyboard.py");

selected_dev = None;

devices = [evdev.InputDevice(fn) for fn in evdev.list_devices()]
for device in devices:
    if re.match(".*gamepad.*",device.name,re.IGNORECASE):
        selected_dev = device

    print(device.fn, device.name, device.phys)

if selected_dev is None:
    print("Gamepad not found");
    exit(0);

cur_device = evdev.InputDevice(selected_dev.fn)
print(cur_device)
sys.stdout.write(chr(27) + "[2J")
sys.stdout.write("\n\n\n\n\n\n\n\n\n\n\n\n\n\n");
sys.stdout.write("\033[F\033[F\033[F""");
sys.stdout.write("\033[F\033[F\033[F""");
sys.stdout.write("\033[F\033[F\033[F""");
sys.stdout.write("   ")


sys.stdout.flush()
try:
    plugin = plugin_normal.JKPlugin_Normal
    mylogic = jlogic.JLogic()
    mylogic.set_plugin(plugin)
    keyboardh = jinput.JKInput(cur_device);
    keyboardh.add_gamepad_event_handler(mylogic.click)
    t1 = threading.Thread(target=keyboardh.start)
    t1.start()

    while True:
        time.sleep(1)
except KeyboardInterrupt:
    print "Ctrl-c pressed ..."
    sys.exit(1)
