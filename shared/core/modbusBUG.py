
import serial
import serial_asyncio


class modbusBUG(object):

   def __init__(self, ttydev: str, baudrate: int, parity: str):
      self.ttydev: str = ttydev
      self.baudrate: int = baudrate
      self.parity: str = parity
      self.buffout: bytearray = bytearray()

   def hello(self):
      pass

   def get_bus_id(self) -> str:
      pass

   def get_version(self):
      pass

   def get_pins(self):
      pass

