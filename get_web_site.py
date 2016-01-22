# -*- coding: utf-8 -*-
__author__ = 'meng'

import sys
from downloadhtml import getWebSite
from changeref import trans

def execute_command(args=sys.argv[1:]):
    if not args:
        #usage()
        sys.exit(1)

    command = args[0]
    if command.startswith('-'):
        if command in ('-h', '--help'):
            #usage(bddown_help.show_help())
            pass
        elif command in ('-V', '-v', '--version'):
            print('V0.1')
        else:
            #usage()
            sys.exit(1)
        sys.exit(0)

    commands = {
        'get':         getWebSite,
        'trans':       trans,
    }

    if command not in commands.keys():
        #usage()
        sys.exit(1)
    elif '-h' in args or '--help' in args:
        #bd_help([command])
        sys.exit(0)
    else:
        commands[command](args[1:])


if __name__ == '__main__':
    execute_command()
