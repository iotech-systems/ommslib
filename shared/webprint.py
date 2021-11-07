
import os.path
import json, requests


class webprint(object):

   def __init__(self):
      self.confJsonObj = None
      self.confJsonBuff = ""

   def init(self):
      try:
         with open("webprint.config.json", "r") as f:
            self.confJsonBuff = f.read().strip()
         if self.confJsonBuff not in (None, ""):
            self.confJsonObj = json.loads(self.confJsonBuff)
      except IOError as e:
         print(e)
      except Exception as e:
         print(e)

   def print(self, buff):
      try:
         if not self.confJsonObj["enable"]:
            return
         url = self.confJsonObj["printUrl"]
         requests.post(url, data=buff)
      except requests.exceptions.ConnectionError:
         self.fileprint(buff)
      except Exception as e:
         print(e)

   def fileprint(self, buff):
      try:
         on404: str = self.confJsonObj["on404"]
         if on404.startswith("file://"):
            on404 = on404.replace("file://", "")
         # -- run --
         print(on404)
         with open(on404, "a+") as f:
            f.write(buff)
            f.write("\n\n")
      except IOError as e:
         print(e)


# -- test --
if __name__ == "__main__":
    wp: webprint = webprint()
    wp.init()
    wp.print("test...")
