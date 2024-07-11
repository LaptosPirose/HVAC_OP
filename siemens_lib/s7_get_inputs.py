# Import libraries to Siemens S7 connection
from snap7 import client

"""
    Class to get all needed inputs from PLC
    @Angelo Moura
    julho 2024
"""


class S7GetInput:
    def __init__(self, PLC):
        self.__PLC = PLC
        """
            Constructor function for S7 connection class
            @PLC - PLC S7 Instance
        """

    def getinput(self):
        """
            Get all inputs from PLC
            ** For now just return what you put 
        """
        try:
            # Read MB test
            # Check bit 1 always True to get PLC connection status
            self.__PLC.mb_read(mb=0, bit=1, type=0)
            print(f'Read MB5 test')
            print(f'Leitura de MB bit 0 {self.__PLC.mb_read(mb = 5, bit = 0, type = 0)}')
            print(f'Leitura de MB bit 1 {self.__PLC.mb_read(mb = 5, bit = 1, type = 0)}')
            print(f'Leitura de MB bit 2 {self.__PLC.mb_read(mb = 5, bit = 2, type = 0)}')
            print(f'Leitura de MB bit 3 {self.__PLC.mb_read(mb = 5, bit = 3, type = 0)}')
            print(f'Leitura de MB bit 4 {self.__PLC.mb_read(mb = 5, bit = 4, type = 0)}')
            print(f'Leitura de MB bit 5 {self.__PLC.mb_read(mb = 5, bit = 5, type = 0)}')
            print(f'Leitura de MB bit 6 {self.__PLC.mb_read(mb = 5, bit = 6, type = 0)}')
            print(f'Leitura de MB bit 7 {self.__PLC.mb_read(mb = 5, bit = 7, type = 0)}')

            print(
                f'Leitura do byte em binário {self.__PLC.mb_read(mb = 5, type = 1)}')
            print(
                f'Leitura do byte em inteiro {self.__PLC.mb_read(mb = 5, type = 2)}')
            print(
                f'Leitura do byte em char {self.__PLC.mb_read(mb = 5, type = 3)}')

            print(f'Read MB6 test')
            print(f'Leitura de MB bit 0 {self.__PLC.mb_read(mb = 6, bit = 0, type = 0)}')
            print(f'Leitura de MB bit 1 {self.__PLC.mb_read(mb = 6, bit = 1, type = 0)}')
            print(f'Leitura de MB bit 2 {self.__PLC.mb_read(mb = 6, bit = 2, type = 0)}')
            print(f'Leitura de MB bit 3 {self.__PLC.mb_read(mb = 6, bit = 3, type = 0)}')
            print(f'Leitura de MB bit 4 {self.__PLC.mb_read(mb = 6, bit = 4, type = 0)}')
            print(f'Leitura de MB bit 5 {self.__PLC.mb_read(mb = 6, bit = 5, type = 0)}')
            print(f'Leitura de MB bit 6 {self.__PLC.mb_read(mb = 6, bit = 6, type = 0)}')
            print(f'Leitura de MB bit 7 {self.__PLC.mb_read(mb = 6, bit = 7, type = 0)}')

            print(
                f'Leitura do byte em binário {self.__PLC.mb_read(mb = 6, type = 1)}')
            print(
                f'Leitura do byte em inteiro {self.__PLC.mb_read(mb = 6, type = 2)}')
            print(
                f'Leitura do byte em char {self.__PLC.mb_read(mb = 6, type = 3)}')

            # Read MW test
            print(f'Read MW5 test')
            print(f'Leitura de MW bit 0 {self.__PLC.mw_read(mw=5, bit=0, type=0)}')
            print(f'Leitura de MW bit 1 {self.__PLC.mw_read(mw=5, bit=1, type=0)}')
            print(f'Leitura de MW bit 2 {self.__PLC.mw_read(mw=5, bit=2, type=0)}')
            print(f'Leitura de MW bit 3 {self.__PLC.mw_read(mw=5, bit=3, type=0)}')
            print(f'Leitura de MW bit 4 {self.__PLC.mw_read(mw=5, bit=4, type=0)}')
            print(f'Leitura de MW bit 5 {self.__PLC.mw_read(mw=5, bit=5, type=0)}')
            print(f'Leitura de MW bit 6 {self.__PLC.mw_read(mw=5, bit=6, type=0)}')
            print(f'Leitura de MW bit 7 {self.__PLC.mw_read(mw=5, bit=7, type=0)}')
            print(f'Leitura de MW bit 8 {self.__PLC.mw_read(mw=5, bit=8, type=0)}')
            print(f'Leitura de MW bit 9 {self.__PLC.mw_read(mw=5, bit=9, type=0)}')
            print(f'Leitura de MW bit 10 {self.__PLC.mw_read(mw=5, bit=10, type=0)}')
            print(f'Leitura de MW bit 11 {self.__PLC.mw_read(mw=5, bit=11, type=0)}')
            print(f'Leitura de MW bit 12 {self.__PLC.mw_read(mw=5, bit=12, type=0)}')
            print(f'Leitura de MW bit 13 {self.__PLC.mw_read(mw=5, bit=13, type=0)}')
            print(f'Leitura de MW bit 14 {self.__PLC.mw_read(mw=5, bit=14, type=0)}')
            print(f'Leitura de MW bit 15 {self.__PLC.mw_read(mw=5, bit=15, type=0)}')

            print(
                f'Leitura da word em binário {self.__PLC.mw_read(mw = 5, type = 1)}')
            print(
                f'Leitura da word em inteiro {self.__PLC.mw_read(mw = 5, type = 2)}')
            print(
                f'Leitura do byte em char {self.__PLC.mw_read(mw = 5, type = 3)}')

            # Read MD test
            print(f'Read MD5 test')
            print(f'Leitura de MD bit 0 {self.__PLC.md_read(md=5, bit=0, type=0)}')
            print(f'Leitura de MD bit 1 {self.__PLC.md_read(md=5, bit=1, type=0)}')
            print(f'Leitura de MD bit 2 {self.__PLC.md_read(md=5, bit=2, type=0)}')
            print(f'Leitura de MD bit 3 {self.__PLC.md_read(md=5, bit=3, type=0)}')
            print(f'Leitura de MD bit 4 {self.__PLC.md_read(md=5, bit=4, type=0)}')
            print(f'Leitura de MD bit 5 {self.__PLC.md_read(md=5, bit=5, type=0)}')
            print(f'Leitura de MD bit 6 {self.__PLC.md_read(md=5, bit=6, type=0)}')
            print(f'Leitura de MD bit 7 {self.__PLC.md_read(md=5, bit=7, type=0)}')
            print(f'Leitura de MD bit 8 {self.__PLC.md_read(md=5, bit=8, type=0)}')
            print(f'Leitura de MD bit 9 {self.__PLC.md_read(md=5, bit=9, type=0)}')
            print(f'Leitura de MD bit 10 {self.__PLC.md_read(md=5, bit=10, type=0)}')
            print(f'Leitura de MD bit 11 {self.__PLC.md_read(md=5, bit=11, type=0)}')
            print(f'Leitura de MD bit 12 {self.__PLC.md_read(md=5, bit=12, type=0)}')
            print(f'Leitura de MD bit 13 {self.__PLC.md_read(md=5, bit=13, type=0)}')
            print(f'Leitura de MD bit 14 {self.__PLC.md_read(md=5, bit=14, type=0)}')
            print(f'Leitura de MD bit 15 {self.__PLC.md_read(md=5, bit=15, type=0)}')
            print(f'Leitura de MD bit 16 {self.__PLC.md_read(md=5, bit=16, type=0)}')
            print(f'Leitura de MD bit 17 {self.__PLC.md_read(md=5, bit=17, type=0)}')
            print(f'Leitura de MD bit 18 {self.__PLC.md_read(md=5, bit=18, type=0)}')
            print(f'Leitura de MD bit 19 {self.__PLC.md_read(md=5, bit=19, type=0)}')
            print(f'Leitura de MD bit 20 {self.__PLC.md_read(md=5, bit=20, type=0)}')
            print(f'Leitura de MD bit 21 {self.__PLC.md_read(md=5, bit=21, type=0)}')
            print(f'Leitura de MD bit 22 {self.__PLC.md_read(md=5, bit=22, type=0)}')
            print(f'Leitura de MD bit 23 {self.__PLC.md_read(md=5, bit=23, type=0)}')
            print(f'Leitura de MD bit 24 {self.__PLC.md_read(md=5, bit=24, type=0)}')
            print(f'Leitura de MD bit 25 {self.__PLC.md_read(md=5, bit=25, type=0)}')
            print(f'Leitura de MD bit 26 {self.__PLC.md_read(md=5, bit=26, type=0)}')
            print(f'Leitura de MD bit 27 {self.__PLC.md_read(md=5, bit=27, type=0)}')
            print(f'Leitura de MD bit 28 {self.__PLC.md_read(md=5, bit=28, type=0)}')
            print(f'Leitura de MD bit 29 {self.__PLC.md_read(md=5, bit=29, type=0)}')
            print(f'Leitura de MD bit 30 {self.__PLC.md_read(md=5, bit=30, type=0)}')
            print(f'Leitura de MD bit 31 {self.__PLC.md_read(md=5, bit=31, type=0)}')

            print(f'Leitura da word em binário {self.__PLC.md_read(md = 5, type = 1)}')
            print(f'Leitura da word em inteiro {self.__PLC.md_read(md = 5, type = 2)}')
            print(f'Leitura do byte em char {self.__PLC.md_read(md = 5, type = 3)}')
        except Exception as e:
            print(f'Conexão impossível - {e}.')
