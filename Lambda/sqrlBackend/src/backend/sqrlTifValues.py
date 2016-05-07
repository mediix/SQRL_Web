# TIF response
# Transaction information flags
class sqrlTifValues:
    ID_MATCH = 0x01
    PID_MATCH = 0x02
    IPS_MATCHED = 0x04
    SQRL_DISABLED = 0x08
    FUNC_NOT_SUPPORTED = 0x10
    TRANSIENT_ERROR = 0x20
    COMMAND_FAILED = 0x40
    CLIENT_FAILURE = 0x80
    BAD_ID_ASSOCIATION = 0x100
    
