
import os
import xml.etree.ElementTree as et


def get_omms_meter_info() -> [None, tuple]:
   root = os.getenv("OMMS_ROOT")
   meter = os.getenv("OMMS_METER")
   path = f"{root}/brands/{meter}.xml"
   if not os.path.exists(path):
      print(f"meter path not found: {path}")
      return None
   print(f"\npath: {path}\n")
   # -- load meter xml --
   xml = et.parse(path)
   xml_root = xml.getroot()
   # -- read meter comm info --
   xml_ser = xml_root.find("serial")
   dbr = xml_ser.attrib["baudrate"]
   par = xml_ser.attrib["parity"]
   sbt = xml_ser.attrib["stopbits"]
   tout = float(xml_ser.attrib["timeoutSecs"])
   # -- read meter address info --
   xpath = "registers/register[@name=\"ModbusAddress\"]"
   xml_reg = xml_root.find(xpath)
   adr_str = xml_reg.attrib["address"]
   if adr_str.startswith("0x"):
      adr_int = int(adr_str, 16)
   else:
      adr_int = int(adr_str)
   # -- return tuple --
   return int(dbr), par, sbt, tout, adr_int
