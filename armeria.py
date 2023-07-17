#!/usr/bin/env python3
import os
import subprocess
# Required parameters:
# @raycast.schemaVersion 1
# @raycast.title Armeria Debug
# @raycast.mode compact

# Optional parameters:
# @raycast.icon Armeria
# @raycast.argument1 { "type": "text", "placeholder": "Project Name" }
# @raycast.needsConfirmation false

import sys

objectName = sys.argv[1]
os.system("/Volumes/workspace/admin/go/go-script/bin/utils armeria -p " + objectName)
