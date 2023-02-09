
import xml.etree.ElementTree as _et
from ommslib.shared.core.elecRegStrEnums import elecRegStrEnumsShort
from core.logutils import logUtils


"""
   <reg type="total_kwh" lbl="TotalActiveEnergy" default="null" />
"""
class elecReg(object):

   def __init__(self, xmlelm: _et.Element):
      try:
         self.xmlelm: _et.Element = xmlelm
         __tmp = self.xmlelm.attrib["type"]
         self.regtype: elecRegStrEnumsShort = elecRegStrEnumsShort[__tmp]
         self.default = self.xmlelm.attrib["default"]
         self.lbl = self.xmlelm.attrib["lbl"]
      except Exception as e:
         logUtils.log_exp(["elecReg.c-tor", e])
