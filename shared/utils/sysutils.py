
import os
from typing import List
from ommslib.shared.models.kWhReading import kWhReading
import xml.etree.ElementTree as et


class sysutils(object):

   @classmethod
   def hostName(cls) -> str:
      with open("/etc/hostname", "r") as file:
         buff: str = file.read()
      return buff.strip()

   @classmethod
   def findRegister(cls, regList: List[kWhReading], regName: str) -> [kWhReading, None]:
      regVal = next((r for r in regList if r.regName == regName), None)
      return regVal

   @classmethod
   def getMeterModelXml(cls, brand: str, model: str) -> et.Element:
      meterXmlFile = f"brands/{brand}/{model}"
      if not os.path.exists(meterXmlFile):
         raise Exception(f"FileNotFound: {meterXmlFile}")
      # -- return --
      return et.ElementTree().parse(meterXmlFile)

   @staticmethod
   def ttyusb(ap: argsParser):
      ttydev = ap.get_item("port")
      path = ap.get_item("path")
      if ttydev == "":
         finder: ttyUSBFinder = ttyUSBFinder()
         ttydev = finder.find_by_path(path)
      if ttydev in [None, False]:
         raise SystemError(f"CanNotLocateUSBDevice:[ {ttydev} : {path} ]")
      print(f"\tusing ttydev:[ {ttydev} : {path} ]")
      return ttydev
