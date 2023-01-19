
from abc import ABC as _abc
import threading as _th


class abcBot(_abc):

   def __init__(self, th_obj: _th.Thread):
      """"
         class of th_obj would be the name of the hosted_class
      """
      self.th_obj: _th.Thread = th_obj
      self.hosted_class = self.th_obj.__class__.name
      self.hostname: str = ""
      self.lan_ip: str = ""
      self.wan_ip: str = ""

   def init(self):
      pass
