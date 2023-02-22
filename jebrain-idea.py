#!/usr/bin/env python3
import os
# Required parameters:
# @raycast.schemaVersion 1
# @raycast.title Idea
# @raycast.mode compact

# Optional parameters:
# @raycast.icon IDEA
# @raycast.argument1 { "type": "text", "placeholder": "Project Name" }
# @raycast.needsConfirmation false

import sys
from base import JetBrainsUtils

jetbrains = JetBrainsUtils.JetBrainsUtils("/usr/local/bin/idea")
jobs = jetbrains.readFile()
noObject = True
objectName = sys.argv[1]
for job in jobs:
    if job.endswith("/" + objectName):
        noObject = False
        idea_job = "/usr/local/bin/idea " + job
        os.system(idea_job)

if noObject:
    print("没有对应的项目 " + objectName)
