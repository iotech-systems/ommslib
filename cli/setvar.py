#!/usr/bin/env python3

import os, sys
from appbin.utils import *


INFO = """
   --- omms setvar info ---
      writes file to /opt/iotech/ramdsk folder
"""

if len(sys.argv) == 1:
   print(INFO)
   exit(0)

