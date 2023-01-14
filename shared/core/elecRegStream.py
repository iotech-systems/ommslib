
import datetime
import time
import typing as _t, xml.etree.ElementTree as _et
from ommslib.shared.core.elecReg import elecReg, elecRegStrEnumsShort


"""
   <stream enabled="1" name="kWhrs" runInterval="20" dataTable="stream.kwhrs_raw">
"""
class elecRegStream(object):

   def __init__(self, rs_xml: _et.Element):
      self.rs_xml: _et.Element = rs_xml
      self.name = self.rs_xml.attrib["name"]
      self.run_index: int = int(self.rs_xml.attrib["runIndex"])
      # -- -- -- -- -- -- -- --
      self.run_intv: int = 0
      tmp = self.rs_xml.attrib["runInterval"].lower()
      if "m" in tmp.lower():
         self.run_intv = (int(tmp.replace("m", "")) * 60)
      else:
         self.run_intv = int(tmp)
      # -- -- -- -- -- -- -- --
      self.data_table = self.rs_xml.attrib["dataTable"]
      self.last_run_time: int = 0
      self.reg_arr: _t.List[elecReg] = []
      self.__init_reg_arr()

   def __str__(self):
      return f"name: {self.name} | run_intv: {self.run_intv}"

   def is_time_to_run(self):
      return (int(time.time()) - self.last_run_time) > self.run_intv

   def time_to_run(self) -> int:
      diff = int(time.time()) - self.last_run_time
      return self.run_intv - diff

   def update_last_run(self):
      self.last_run_time = int(time.time())

   def __init_reg_arr(self):
      for r_xml in self.rs_xml.findall("reg"):
         er: elecReg = elecReg(r_xml)
         self.reg_arr.append(er)
