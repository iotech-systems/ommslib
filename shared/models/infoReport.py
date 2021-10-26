
from openbmslib.shared.models import coreModel


class infoReport(coreModel.coreModel):

   INFO = "INFO"
   ERROR = "ERROR"
   WARNING = "WARNING"

   def __init__(self, infoMsg: str, infoTag: str):
      super(infoReport, self).__init__()
      self.info_msg: str = infoMsg
      self.info_tag: str = infoTag

   def fromJson(self, jsonBuff: str):
      jObj = infoReport.__json_obj__(jsonBuff)
      if self.className != jObj["className"]:
         raise Exception(f"bad _type_ : {self.className}")
      self.dtsUTC: str = str(jObj["dtsUTC"])
      self.info_tag: str = str(jObj["info_tag"])
      self.info_msg: str = str(jObj["info_msg"])
