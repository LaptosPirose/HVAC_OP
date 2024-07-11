from siemens_lib.s7_connection import S7Connection
from siemens_lib.s7_get_inputs import S7GetInput


def main(args):
    print(f'Hello world! {args}')

    ip = '192.168.0.55'
    rack = 0
    cpu_slot = 4

    
    MEB = S7Connection(ip=ip, rack=rack, cpu_slot=cpu_slot)
    MEB_inputs = S7GetInput(PLC = MEB)
    MEB_inputs.getinput()


if __name__ == '__main__':
    main('init')
