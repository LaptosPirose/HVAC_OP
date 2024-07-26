from siemens_lib.s7_connection import S7Connection
from siemens_lib.s7_get_inputs import S7GetInput
from datetime import datetime


def main(args):
    print(f'Hello world! {args}')

    ip = '192.168.0.55'
    rack = 0
    cpu_slot = 4

    MEB = S7Connection(ip=ip, rack=rack, cpu_slot=cpu_slot)
    MEB_inputs = S7GetInput(PLC=MEB)
    # MEB_inputs.getinput()

    date_now = str(datetime.now())
    data_pla = MEB.db_read(db_number=230, start_pos=8,
                           qty_bytes=3, qty_bits=24, bit=0, type=3)
    data_vis = MEB.db_read(db_number=230, start_pos=72,
                           qty_bytes=8, qty_bits=64, bit=0, type=3)
    data_badge = MEB.db_read(db_number=230, start_pos=41,
                             qty_bytes=8, qty_bits=64, bit=0, type=3)
    data_balancele = MEB.db_read(
        db_number=6401, start_pos=10, qty_bytes=2, qty_bits=32, bit=0, type=2)-5000

    print(date_now, ' PLA >>> ', data_pla, ' VIS >>> ', data_vis,
          'Balancele >>> ', data_balancele, ' Badge >>> ', data_badge)


if __name__ == '__main__':
    main('init')
