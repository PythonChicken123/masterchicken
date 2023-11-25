# coding=utf-8
import subprocess
import argparse

parser_csv_description = 'Comma-separated values (CSV) is a text file format that uses commas to separate values. A CSV file stores tabular data (numbers and text) in plain text, where each line of the file typically represents one data record. Each record consists of the same number of fields, and these are separated by commas in the CSV file.'


def main():
    parser = argparse.ArgumentParser(description='masterchicken.exe - Install a package or an file in the internet '
                                                 'and create application using masterchicken in python')

    subparsers = parser.add_subparsers(dest='command')
    subparsers.required = True

    # Subcommand 1
    parser_command1 = subparsers.add_parser('csv_read', help=parser_csv_description)
    parser_command1.add_argument('arg1', help='Path to the CSV file')
    parser_command1.add_argument('arg2', help='')

    # Subcommand 2
    parser_command2 = subparsers.add_parser('command2', help='Description for command 2')
    parser_command2.add_argument('arg3', help='Description for argument 1 of command 2')

    # Subcommand 2
    parser_command2 = subparsers.add_parser('backrooms', help='Run backrooms.exe')
    parser_command2.add_argument('arg4', help='Description for argument 1 of command 2')

    args = parser.parse_args()

    if args.command == 'read_csv':
        print('Running command 1 with arg1={}, arg2={}'.format(args.arg1, args.arg2))
        # Do something for command 1
    elif args.command == 'command2':
        print('Running command 2 with arg3={}'.format(args.arg3))
        # Do something for command 2
    elif args.command == 'backrooms':
        if args.arg4 == '.run':
            print("backrooms.exe running with command: arg4={}, install backrooms.brs, rooms.pck".format(args.arg4))
            Warning('Make sure you have: [Microsoft .NET Framework], [Python 2.6 or Later] installed!')
            print("Preparing backrooms.msi to be installed: 1MB or less.")
            try:
                import backrooms
            except:
                subprocess.check_call(
                    ['python.exe', '-m', 'pip', 'install', '--upgrade', '--force', '--user', 'backrooms'])
        else:
            print("Command unrecognised, please insert the command for args.arg4.value")
        pass
    pass


if __name__ == '__main__':
    main()
