
import enum


class appErrorCodes(enum.Enum):

   OK = 0
   METER_NOT_FOUND = 431
   MISSING_INPUT = 432
   INVALID_INPUT = 433
   BAD_DB_INSERT = 434
