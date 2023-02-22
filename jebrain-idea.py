#!/usr/bin/env python3
import os
# Required parameters:
# @raycast.schemaVersion 1
# @raycast.title Jebrain Idea
# @raycast.mode compact

# Optional parameters:
# @raycast.icon 🤖
# @raycast.argument1 { "type": "text", "placeholder": "Project Name" }
# @raycast.needsConfirmation false

import sys
from base import JetBrainsUtils

jetbrains = JetBrainsUtils.JetBrainsUtils("/usr/local/bin/idea")
jobs = jetbrains.readFile()
for job in jobs:
    if job.endswith("/" + sys.argv[1]):
        idea_job = "/usr/local/bin/idea " + job
        os.system(idea_job)
