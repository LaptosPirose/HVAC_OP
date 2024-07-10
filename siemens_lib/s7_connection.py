# Import libraries to Siemens S7 connection
from snap7 import client

'''
    Class to connect Siemens S7 connection. Also provides variables getters and setters
    @AngeloMoura
    072024
'''

class S7Connection:
    def __init__(self, ip, rack, cpu_slot, tcp_port=1102):
        """
            Constructor function for S7 connection class
            @ip - PLC IP address
            @rack - PLC rack number
            @cpu_slot - PLC CPU slot number
            @tcp_port - tcp port to connection - Not used to perform all ports permitted.
                Notated just to keep standard connection parameters
        """
        self.__ip = ip
        self.__rack = rack
        self.__cpu_slot = cpu_slot
        self.__tcp_port = tcp_port
        self.__connect(self.__ip, self.__rack,
                       self.__cpu_slot, self.__tcp_port)

    def __connect(self, ip, rack, cpu_slot, tcp_port):
        """
            Perform connection to S7 connection Siemens PLC
            @ip - PLC IP address
            @rack - PLC rack number
            @cpu_slot - PLC CPU slot number
            @tcp_port - tcp port to connection - Not used to perform all ports permitted.
                Notated just to keep standard connection parameters
        """
        try:
            self.__connection = client.Client()
            self.__connection.connect(ip, rack, cpu_slot)
            self.__connection.get_connected()
            print('connected successfully')
            print(type(self.__connection))
            return self.__connection
        except Exception as __exception:
            print(f'Connection failed. {__exception}')

    def __convert_bin(self, raw_value, length):
            '''
                Perform conversion from raw integer value to binary representation.
                @raw_value_byte - integer value to convert
                @length - size of array to convert (8, 16...)
            '''
            self.__raw_value_binary = bin(raw_value)
            if raw_value < 0:
                self.__raw_value_binary = self.__raw_value_binary[3:]
                self.__changed_bits = str('')
                for i in range(len(self.__raw_value_binary)):
                    if self.__raw_value_binary[i] == '0':
                        self.__changed_bits += '1'
                    else:
                        self.__changed_bits += '0'
                add_zeros = length - len(self.__raw_value_binary)
                self.__changed_bits = add_zeros * '1' + self.__changed_bits
                self.__final_inverted_value = int(self.__changed_bits, 2) + 1
                self.__binary = bin(self.__final_inverted_value)
            else:
                self.__raw_value_binary = self.__raw_value_binary[2:]
                self.__raw_binary_len = len(self.__raw_value_binary)
                self.__byte_add_len = length - self.__raw_binary_len
                self.__binary = self.__byte_add_len * '0' + self.__raw_value_binary
                self.__binary = '0b' + self.__binary
            return self.__binary

    def mb_read(self, mb, bit=0, type=1):
        '''
            Perform return getter from MB. The value returned depends of type
                you entered.
                0 = Return bit from mb representation (consider as string)
                1 = Return byte binary representation (consider as string)
                2 = Return byte decimal representation (consider as int)
                3 = Return char representation (consider string)
        '''
        self.__BYTE_LEN = 8
        self.__raw_value_byte = int.from_bytes(self.__connection.mb_read(
            mb, 1), signed=True)
        self.__binary = self.__convert_bin(
            raw_value=self.__raw_value_byte, length=self.__BYTE_LEN)

        if type == 0:
            self.__binary = self.__binary[2:]
            self.__binary = self.__binary[self.__BYTE_LEN - 1 - bit]
            self.__byte = self.__binary

        if type == 1:
            self.__byte = self.__binary

        if type == 2:
            self.__byte = self.__raw_value_byte

        if type == 3:
            self.__byte = chr(abs(self.__raw_value_byte))

        return self.__byte

    def mw_read(self, mw, bit=0, type=1):
        '''
            Perform return getter from MW. The value returned depends of type
                you entered.
                0 = Return bit from mb representation (consider as string)
                1 = Return word binary representation (consider as string)
                2 = Return word decimal representation (consider as int)
                3 = Return char representation (consider string)
        '''
        self.__WORD_LEN = 16
        self.__raw_value_word = int.from_bytes(self.__connection.mb_read(
            mw, 2), signed=True)
        self.__binary = self.__convert_bin(
            raw_value=self.__raw_value_word, length=self.__WORD_LEN)

        if type == 0:
            self.__binary = self.__binary[2:]
            self.__binary = self.__binary[self.__WORD_LEN - 1 - bit]
            self.__word = self.__binary

        if type == 1:
            self.__word = self.__binary

        if type == 2:
            self.__word = self.__raw_value_word

        if type == 3:
            self.__char_last = self.__binary[:10]
            self.__char_last = chr(int(self.__char_last, 2))

            self.__char_first = self.__binary[10:]
            self.__char_first = chr(int(self.__char_first, 2))

            self.__word = self.__char_last + self.__char_first

        return self.__word

    def md_read(self, md, bit=0, type=1):
            '''
                Perform return getter from MD. The value returned depends of type
                    you entered.
                    0 = Return bit from mb representation (consider as string)
                    1 = Return word binary representation (consider as string)
                    2 = Return word decimal representation (consider as int)
                    3 = Return char representation (consider string)
            '''
            self.__DWORD_LEN = 32
            self.__raw_value_word = int.from_bytes(self.__connection.mb_read(
                md, 4), signed=True)
            self.__binary = self.__convert_bin(
                raw_value=self.__raw_value_word, length=self.__DWORD_LEN)

            if type == 0:
                self.__binary = self.__binary[2:]
                self.__binary = self.__binary[self.__DWORD_LEN - 1 - bit]
                self.__dword = self.__binary

            if type == 1:
                self.__dword = self.__binary

            if type == 2:
                self.__dword = self.__raw_value_word

            if type == 3:
                self.__char_last = self.__binary[26:]
                self.__char_last = chr(int(self.__char_last, 2))

                self.__char_third = self.__binary[18:26]
                self.__char_third = chr(int(self.__char_third, 2))

                self.__char_second = self.__binary[10:18]
                self.__char_second = chr(int(self.__char_second, 2))

                self.__char_first = self.__binary[:10]
                self.__char_first = chr(int(self.__char_first, 2))

                self.__dword = self.__char_first + self.__char_second + self.__char_third + self.__char_last

            return self.__dword
