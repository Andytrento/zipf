# myls.py

# import os
# import sys

# if len(sys.argv) > 2:
# print('You have specified too many arguments')
# sys.exit()

# if len(sys.argv) < 2:
# print('You need to specify the path to be listed')
# sys.exit()


# input_path = sys.argv[1]

# if not os.path.isdir(input_path):
# print('The path specified does not exist')
# sys.exit()

# print('\n'.join((os.listdir(input_path))))


# myls.py using argparse

# Import the argparse library
import argparse
import os
import sys

# Create the parser
my_parser = argparse.ArgumentParser(
    prog="myls",
    usage="%(prog)s [option] path",
    description="List the content of a folder",
    epilog="Enjoy the program! :)"
)

# Add the arguments
my_parser.add_argument("Path", metavar="path", type=str, help="the path to list")
my_parser.add_argument(
    "-l", "--long", action="store_true", help="enable the long list format"
)

# Execute the parse_args() method
args = my_parser.parse_args()
# print(type(args))  # parse_args() return a Namespace object that contains the user input

input_path = args.Path

if not os.path.isdir(input_path):
    print("The path specified does not exist")
    sys.exit()

for line in os.listdir(input_path):
    if args.long:
        size = os.stat(os.path.join(input_path, line)).st_size
        line = '%10d%s' % (size, line)
    print(line)

print("\n".join((os.listdir(input_path))))
