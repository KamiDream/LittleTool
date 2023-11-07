import snap7
from snap7.exceptions import Snap7Exception
# tag:PLC基础功能


class Plc():

    def __init__(self):
        self.po = snap7.client.Client()
        self.cStatus = 2
        pass

    # ---------------------------------------------------------------------------- #

    def connect(self, _ip):  # 尝试连接
        try:
            self.po.connect(str(_ip), 0, 1)
            if self.po.get_connected() is True:  # 连接反馈
                self.cStatus = 1
            else:
                self.cStatus = 0
        except BaseException:
            self.po.disconnect()
            self.cStatus = 0
            # print('Connected')

    def disConnect(self):  # 断开连接
        self.po.disconnect()
        if self.po.get_connected() is False:  # 断开反馈
            self.cStatus = 0
            # print('Disconnected')

    # ---------------------------------------------------------------------------- #

    def _wbool(self, _dbNum, _byteOffset, _boolOffset,
               _value):  # tag:PLC写入bool
        buffer = bytearray(1)
        snap7.util.set_bool(buffer, 0, _boolOffset, _value)
        # print(buffer)
        self.po.db_write(_dbNum, _byteOffset, buffer)

    def _wint(self, _dbNum, _byteOffset, _value):  # tag:PLC写入int
        buffer = bytearray(2)
        snap7.util.set_int(buffer, 0, _value)
        # print(buffer)
        self.po.db_write(_dbNum, _byteOffset, buffer)

    # ---------------------------------------------------------------------------- #

    def _getDrawData(self):  # tag:PLC获取绘图数据
        try:
            data = self.po.db_read(1, 0, 546)
            power = snap7.util.get_uint(data, 538)
            hold = snap7.util.get_uint(data, 4)
            snap7.util.get
            return power, hold
        finally:
            pass
