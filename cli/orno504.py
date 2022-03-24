
import binascii
import time, crc16
import minimalmodbus as mm


class orno504(object):

   def __init__(self):
      self.dev = "/dev/ttyUSB0"
      self.inst = mm.Instrument(port=self.dev, slaveaddress=32)
      self.inst.serial.baudrate = 9600
      self.inst.serial.parity = "N"
      self.inst.serial.stopbits = 1
      self.inst.serial.bytesize = 8

   def write_bytes(self, barr: bytearray):
      self.serial_write(barr)

   def send_passwd(self, pwd: str):
      buff: bytearray = bytearray()
      buff.extend([self.inst.address])
      buff.extend([40, 254, 1, 0, 2, 4])
      buff.extend(bytes.fromhex(pwd[0:2]))
      buff.extend(bytes.fromhex(pwd[2:4]))
      buff.extend(bytes.fromhex(pwd[4:6]))
      buff.extend(bytes.fromhex(pwd[6:8]))
      buff.extend(self.crc16(buff))
      self.serial_write(buff)

   def serial_write(self, barr: bytearray):
      if not self.inst.serial.isOpen():
         self.inst.serial.open()
      tmp = binascii.hexlify(barr)
      print(tmp)
      self.inst.serial.write(barr)
      time.sleep(0.05)
      self.serial_read()

   def serial_read(self):
      while not self.inst.serial.in_waiting:
         time.sleep(0.004)
      buff: bytearray = bytearray()
      while self.inst.serial.in_waiting:
         buff.extend(self.inst.serial.read())
      # -- dump response for now --
      print(buff)

   def crc16(self, data: bytearray):
      crc = 0xffff
      for cur_byte in data:
         crc = crc ^ cur_byte
         for _ in range(8):
            a = crc
            carry_flag = a & 0x0001
            crc = crc >> 1
            if carry_flag == 1:
               crc = crc ^ 0xa001
      # -- return bytes --
      return bytes([crc % 256, crc >> 8 % 256])


# -- run tests --
if __name__ == "__main__":
   o504 = orno504()
   o504.send_passwd("00000000")
   barr: bytearray = bytearray("hello, world!", "ascii")
   o504.write_bytes(barr)
