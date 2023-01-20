
import datetime
import enum


class mqttInfo(object):

   def __init__(self, host: str, port: int, pwd: str):
      self.host: str = host
      self.port: int = port
      self.pwd: str = pwd


class mqttMeterInfo(object):

   def __init__(self, tag: str, syspath: str):
      self.tag: str = tag
      self.syspath = syspath


class redisDBIdx(enum.Enum):

   DB_IDX_ONPREM_DIAG = 0
   DB_IDX_EDGE_DIAG = 1
   DB_IDX_READS = 2
   DB_IDX_HEARTBEATS = 4