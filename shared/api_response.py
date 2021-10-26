
import json
from sbmslib.shared.app_error_codes import appErrorCodes


class api_response(object):

   def __init__(self, route: str, method: str, error: appErrorCodes, msg: str = None):
      self.api_route = route
      self.api_method = method
      self.app_err: int = error.value
      if msg is None:
         msg = error.name
      self.err_msg = msg

   def __str__(self):
      return json.dumps(self, default=lambda o: o.__dict__)

   def toJson(self):
      return json.dumps(self, default=lambda o: o.__dict__)
