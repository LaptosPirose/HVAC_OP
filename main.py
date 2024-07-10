from siemens_lib.s7_connection import S7Connection

def main(args):
    print(f'Hello world! {args}')
    MEB = S7Connection(ip='192.168.0.55', rack=0, cpu_slot=4)

    # Read MB test
    print(f'Read MB5 test')
    # print(f'Leitura de MB bit 0 {MEB.mb_read(mb = 5, bit = 0, type = 0)}')
    # print(f'Leitura de MB bit 1 {MEB.mb_read(mb = 5, bit = 1, type = 0)}')
    # print(f'Leitura de MB bit 2 {MEB.mb_read(mb = 5, bit = 2, type = 0)}')
    # print(f'Leitura de MB bit 3 {MEB.mb_read(mb = 5, bit = 3, type = 0)}')
    # print(f'Leitura de MB bit 4 {MEB.mb_read(mb = 5, bit = 4, type = 0)}')
    # print(f'Leitura de MB bit 5 {MEB.mb_read(mb = 5, bit = 5, type = 0)}')
    # print(f'Leitura de MB bit 6 {MEB.mb_read(mb = 5, bit = 6, type = 0)}')
    # print(f'Leitura de MB bit 7 {MEB.mb_read(mb = 5, bit = 7, type = 0)}')

    print(f'Leitura do byte em binário {MEB.mb_read(mb = 5, type = 1)}')

    # print(f'Leitura do byte em inteiro {MEB.mb_read(mb = 5, type = 2)}')
    # print(f'Leitura do byte em char {MEB.mb_read(mb = 5, type = 3)}')

    print(f'Read MB6 test')
    # print(f'Leitura de MB bit 0 {MEB.mb_read(mb = 6, bit = 0, type = 0)}')
    # print(f'Leitura de MB bit 1 {MEB.mb_read(mb = 6, bit = 1, type = 0)}')
    # print(f'Leitura de MB bit 2 {MEB.mb_read(mb = 6, bit = 2, type = 0)}')
    # print(f'Leitura de MB bit 3 {MEB.mb_read(mb = 6, bit = 3, type = 0)}')
    # print(f'Leitura de MB bit 4 {MEB.mb_read(mb = 6, bit = 4, type = 0)}')
    # print(f'Leitura de MB bit 5 {MEB.mb_read(mb = 6, bit = 5, type = 0)}')
    # print(f'Leitura de MB bit 6 {MEB.mb_read(mb = 6, bit = 6, type = 0)}')
    # print(f'Leitura de MB bit 7 {MEB.mb_read(mb = 6, bit = 7, type = 0)}')

    print(f'Leitura do byte em binário {MEB.mb_read(mb = 6, type = 1)}')
    print(f'Leitura do byte em inteiro {MEB.mb_read(mb = 6, type = 2)}')
    print(f'Leitura do byte em char {MEB.mb_read(mb = 6, type = 3)}')

    # Read MW test
    print(f'Read MW5 test')
    # print(f'Leitura de MW bit 0 {MEB.mw_read(mw=5, bit=0, type=0)}')
    # print(f'Leitura de MW bit 1 {MEB.mw_read(mw=5, bit=1, type=0)}')
    # print(f'Leitura de MW bit 2 {MEB.mw_read(mw=5, bit=2, type=0)}')
    # print(f'Leitura de MW bit 3 {MEB.mw_read(mw=5, bit=3, type=0)}')
    # print(f'Leitura de MW bit 4 {MEB.mw_read(mw=5, bit=4, type=0)}')
    # print(f'Leitura de MW bit 5 {MEB.mw_read(mw=5, bit=5, type=0)}')
    # print(f'Leitura de MW bit 6 {MEB.mw_read(mw=5, bit=6, type=0)}')
    # print(f'Leitura de MW bit 7 {MEB.mw_read(mw=5, bit=7, type=0)}')
    # print(f'Leitura de MW bit 8 {MEB.mw_read(mw=5, bit=8, type=0)}')
    # print(f'Leitura de MW bit 9 {MEB.mw_read(mw=5, bit=9, type=0)}')
    # print(f'Leitura de MW bit 10 {MEB.mw_read(mw=5, bit=10, type=0)}')
    # print(f'Leitura de MW bit 11 {MEB.mw_read(mw=5, bit=11, type=0)}')
    # print(f'Leitura de MW bit 12 {MEB.mw_read(mw=5, bit=12, type=0)}')
    # print(f'Leitura de MW bit 13 {MEB.mw_read(mw=5, bit=13, type=0)}')
    # print(f'Leitura de MW bit 14 {MEB.mw_read(mw=5, bit=14, type=0)}')
    # print(f'Leitura de MW bit 15 {MEB.mw_read(mw=5, bit=15, type=0)}')

    print(f'Leitura da word em binário {MEB.mw_read(mw = 5, type = 1)}')
    print(f'Leitura da word em inteiro {MEB.mw_read(mw = 5, type = 2)}')
    print(f'Leitura do byte em char {MEB.mw_read(mw = 5, type = 3)}')

    # Read MD test
    print(f'Read MD5 test')
    print(f'Leitura da word em binário {MEB.md_read(md = 5, type = 1)}')
    print(f'Leitura da word em inteiro {MEB.md_read(md = 5, type = 2)}')
    print(f'Leitura do byte em char {MEB.md_read(md = 5, type = 3)}')

    

if __name__ == '__main__':
    main('init')
