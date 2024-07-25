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

    while True:
        # Read data from MEB
        date_now = str(datetime.now())
        data_pla = MEB.db_read_string(db_number=230, start_pos=8, qty_bytes=3)
        data_vis = MEB.db_read_string(db_number=230, start_pos=72, qty_bytes=8)
        data_badge = MEB.db_read_string(db_number=230, start_pos=40, qty_bytes=10)
        data_balancele = MEB.mb_read(mb=6401,type=2)# mb-5000
    
        print(date_now, ' PLA >>> ', data_pla, ' VIS >>> ', data_vis,
            'Balancele >>> ', data_balancele, ' Badge >>> ', data_badge)

        # print(date_now, data_vis)
        # print(date_now, data_pla)

if __name__ == '__main__':
    main('init')
