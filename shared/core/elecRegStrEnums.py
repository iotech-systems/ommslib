
from enum import Enum


# register names table
# class elecRegStrEnums(Enum):
#
#    ModbusAddress = "ModbusAddress"
#    SerialNumber = "SerialNumber"
#    BaudRate = "BaudRate"
#    HardwareVersion = "HardwareVersion"
#    SoftwareVersion = "SoftwareVersion"
#    CT_Rate = "CT_Rate"
#    S0_OutputRate = "S0_OutputRate"
#    A3 = "A3"
#    CycleTime = "CycleTime"
#    # line(s) frequency ~ Hz
#    GridFreqHz = "GridFreqHz"
#    L1_FreqHz = "L1_FreqHz"
#    L2_FreqHz = "L2_FreqHz"
#    L3_FreqHz = "L3_FreqHz"
#    # voltage ~ V
#    LineVoltage = "LineVoltage"                              # used by 1phase and 3phase edge_meters
#    L1_Voltage = "L1_Voltage"
#    L2_Voltage = "L2_Voltage"
#    L3_Voltage = "L3_Voltage"
#    # amps ~ A
#    TotalAmps = "TotalAmps"                                  # used by 1phase and 3phase edge_meters
#    L1_Amps = "L1_Amps"
#    L2_Amps = "L2_Amps"
#    L3_Amps = "L3_Amps"
#    # active power ~ watts
#    TotalActivePower = "TotalActivePower"                    # used by 1phase and 3phase edge_meters
#    L1_ActivePower = "L1_ActivePower"
#    L2_ActivePower = "L2_ActivePower"
#    L3_ActivePower = "L3_ActivePower"
#    # reactive power ~ Volt-Ampere reactive i.e. VAR
#    TotalReactivePower = "TotalReactivePower"                # used by 1phase and 3phase edge_meters
#    L1_ReactivePower = "L1_ReactivePower"
#    L2_ReactivePower = "L2_ReactivePower"
#    L3_ReactivePower = "L3_ReactivePower"
#    # apparent power ~ units of Volt-amp (VA)
#    TotalApparentPower = "TotalApparentPower"                # used by 1phase and 3phase edge_meters
#    L1_ApparentPower = "L1_ApparentPower"
#    L2_ApparentPower = "L2_ApparentPower"
#    L3_ApparentPower = "L3_ApparentPower"
#    # power factor
#    TotalPowerFactor = "TotalPowerFactor"                    # used by 1phase and 3phase edge_meters
#    L1_PowerFactor = "L1_PowerFactor"
#    L2_PowerFactor = "L2_PowerFactor"
#    L3_PowerFactor = "L3_PowerFactor"
#    # misc
#    CRC = "CRC"
#    CombinedCode = "CombinedCode"
#    # kwh ~ kWh
#    TotalActiveEnergy = "TotalActiveEnergy"                  # used by 1phase and 3phase edge_meters
#    L1_TotalActiveEnergy = "L1_TotalActiveEnergy"
#    L2_TotalActiveEnergy = "L2_TotalActiveEnergy"
#    L3_TotalActiveEnergy = "L3_TotalActiveEnergy"
#    # - - - -
#    TotalReactiveEnergy = "TotalReactiveEnergy"              # used by 1phase and 3phase edge_meters
#    L1_ReactiveEnergy = "L1_ReactiveEnergy"
#    L2_ReactiveEnergy = "L2_ReactiveEnergy"
#    L3_ReactiveEnergy = "L3_ReactiveEnergy"
#    # forward active energy
#    ForwardActiveEnergy = "ForwardActiveEnergy"
#    L1_ForwardActiveEnergy = "L1_ForwardActiveEnergy"
#    L2_ForwardActiveEnergy = "L2_ForwardActiveEnergy"
#    L3_ForwardActiveEnergy = "L3_ForwardActiveEnergy"


class elecRegStrEnumsShort(Enum):
   # -- misc --
   Unknown = "Unknown"
   ModbusAddr = "ModbusAddr"
   SerialNum = "SerialNum"
   BaudRate = "BaudRate"
   HWVer = "HWVer"
   SWVer = "SWVer"
   # -- voltage --
   ln_v = "ln_v"
   l1_v = "l1_v"
   l2_v = "l2_v"
   l3_v = "l3_v"
   # -- freq --
   grid_hz = "grid_hz"
   # l1_hz = "l1_hz"
   # l2_hz = "l2_hz"
   # l3_hz = "l3_hz"
   # -- amps --
   tl_a = "tl_a"
   l1_a = "l1_a"
   l2_a = "l2_a"
   l3_a = "l3_a"
   # -- kwh --
   tl_kwh = "tl_kwh"
   l1_kwh = "l1_kwh"
   l2_kwh = "l2_kwh"
   l3_kwh = "l3_kwh"
   # -- watts --
   tl_w = "tl_w"
   l1_w = "l1_w"
   l2_w = "l2_w"
   l3_w = "l3_w"
   # -- power factor --
   tl_pf = "tl_pf"
   l1_pf = "l1_pf"
   l2_pf = "l2_pf"
   l3_pf = "l3_pf"
   """
      this list needs to be expended as needed
   """
   tl_var = "tl_var"
   tl_va = "tl_va"
   tl_kvarh = "tl_kvarh"
