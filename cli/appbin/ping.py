
import os
from .xcmd import xcmd


class ping(xcmd):

   def __init__(self):
      super(ping, self).__init__()
      self.omms_root = os.getenv("OMMS_ROOT")
      self.omms_ = os.getenv("OMMS_METER")

   def setArgs(self, args: []):
      super(ping, self).setArgs(args)

   def run(self):
      print(self.args)

   def parse(self):
      pass
