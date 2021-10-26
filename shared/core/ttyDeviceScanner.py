
import os
import time
import typing as t
import minimalmodbus as mm
import xml.etree.ElementTree as et
import serial
import serial.tools.list_ports as sysPorts
from sbmslib.shared.utils import sysutils


class ttyUSBDeviceScanner(object):

   AUTO = "AUTO"

   def __init__(self, ttyDev: str = AUTO):
      self.ttyDev = ttyDev
      self.meters: t.List[et.Element] = []
      self.usbSerPorts: [] = None
      self.__load_usb_ser_ports__()

   def locateMetersUSBSerialPort(self, lst: t.List[et.Element]) -> [serial.Serial, None]:
      try:
         for usbPort in self.usbSerPorts:
            print(f"\n-- testing: {usbPort.device} --")
            # -- return first found --
            if self.__test_usb_device__(usbPort, lst):
               print(f"\tfound: {usbPort}")
               return usbPort
         # -- not found --
         return None
      except Exception as e:
         print(f"locateMetersUSBSerialPort: {e}")

   def getMeterInfo(self, meter: et.Element):
      brand = meter.attrib["brand"]
      model = meter.attrib["modelXML"]
      busAddress = meter.attrib["busAddress"]
      modelXml = sysutils.sysutils.getMeterModelXml(brand, model)
      serialXml = modelXml.find("serial")
      xpath = "registers/register[@name=\"ModbusAddress\"]"
      registerXml = modelXml.find(xpath)
      # -- return serial info, meter bus address & --
      return serialXml, registerXml, busAddress

   def __do_ping__(self, inst: mm.Instrument, reg) -> bool:
      boolVal = False
      try:
         time.sleep(1.0)
         hexStr = reg.attrib["address"]
         regID = int(hexStr, 16)
         print(f"ping: {inst.address} on {inst.serial.name}", end="")
         val = inst.read_register(regID)
         print(f" :: ResponseOK!")
         boolVal = int(inst.address) == int(val)
      except Exception as e:
         print(f" :: NoResponse!")
      finally:
         return boolVal

   def __test_usb_device__(self, usbPort, meters: t.List[et.Element]) -> bool:
      pongCount = 0
      meterCount = len(meters)
      for meter in meters:
         ser, reg, busID = self.getMeterInfo(meter)
         inst = self.__get_inst__(usbPort, ser, int(busID))
         if self.__do_ping__(inst, reg):
            pongCount += 1
         inst = None
      # -- check number of pongs vs. number of pings/meters --
      if pongCount == 0:
         return False
      return (pongCount / meterCount) > 0.33

   def __get_inst__(self, usbPort, ser: et.Element, busAddress) -> mm.Instrument:
      inst = mm.Instrument(usbPort.device, busAddress)
      inst.serial.baudrate = int(ser.attrib["baudrate"])
      inst.serial.parity = ser.attrib["parity"]
      inst.serial.stopbits = int(ser.attrib["stopbits"])
      inst.serial.timeout = float(ser.attrib["timeoutSecs"])
      inst.debug = False
      return inst

   def __load_usb_ser_ports__(self):
      ports = sysPorts.comports()
      self.usbSerPorts = [p for p in ports if ("USB" in p.name.upper())]
