import argparse
import sys
import os

# user_response = input("Enter the value")

# if len(sys.argv) > 1:
# 	print("2 args", sys.argv[1])
# 	sys.exit()

#Creating a custom action by subclassing the argparse
# class VerboseStore(argparse.Action):
#     def __init__(self, option_strings, dest, nargs=None, **kwargs):
#         if nargs is not None:
#             raise ValueError('nargs not allowed')
#         super(VerboseStore, self).__init__(option_strings, dest, **kwargs)

#     def __call__(self, parser, namespace, values, option_string=None):
#         print('Here I am, setting the ' \
#               'values %r for the %r option...' % (values, option_string))
#         setattr(namespace, self.dest, values)


# Create the parser
my_parser = argparse.ArgumentParser()


#for custom classes
# my_parser.add_argument('-i', '--input', action=VerboseStore, type = int)
# my_parser = argparse.ArgumentParser(description='List the content of a folder', epilog = "keyword to display at the end")

# Setting the Number of Values That Should Be Consumed by the Option by using the nargs keyword
# my_parser.add_argument('--input', action = 'store', type=int, nargs = 3)

# nargs keyword also accepts below as string
# '?' -->a single value, which can be optional
# my_parser.add_argument('--input', action = 'store', type=int, nargs = '?')

# '*' -->a flexible number of values, which will be gathered into a list
# my_parser.add_argument('--input', action = 'store', type=int, nargs = '*')

# '+' -->like *, but requiring at least one value
# my_parser.add_argument('--input', action = 'store', type=int, nargs = '+')

#argparse.REMAINDER --> all the values that are remaining in the command line
# my_parser.add_argument('first', action = 'store', nargs = argparse.REMAINDER)

# Setting a Default Value Produced if the Argument Is Missing
#despite of data type
# my_parser.add_argument('-a', action = 'store', default = 42)

# Setting the Type of the Argument
# my_parser.add_argument('-a', action = 'store', type = int)

# Setting a Domain of Allowed Values for a Specific Argument
# my_parser.add_argument('-a', action = 'store', choices=['head', 'tail'])

#setting allowed vales of numeric values
# my_parser.add_argument('-a', action = 'store', choices=range(1, 15))

# Setting Whether the Argument Is Required
#bad practice seeting up the required for optional argument
# my_parser.add_argument('-a', action = 'store', choices=['head', 'tail'], required = True)

#help option use -h flag to see choices
my_parser.add_argument('-a', action = 'store', choices=['head', 'tail'], help = "see the choices")


# # Add the arguments
# my_parser.add_argument('Path',
#                        metavar='path',
#                        type=str,
#                        help='the path to list')

# my_parser.add_argument('-l',
#                        '--long',
#                        action='store_true',
#                        help='enable the long listing format')

#Setting the Action to Be Taken for an Argument
# my_parser.add_argument('-a', action='store')
# my_parser.add_argument('-b', action='store_const', const=42)
# my_parser.add_argument('-c', action='store_true')
# my_parser.add_argument('-d', action='store_false')
# my_parser.add_argument('-e', action='append')
# my_parser.add_argument('-f', action='append_const', const=42)
# my_parser.add_argument('-g', action='count')
# my_parser.add_argument('-i', action='help')
# my_parser.add_argument('-j', action='version')


# my_parser.add_argument('--input', action = 'store', type = int)

# Execute the parse_args() method
args = my_parser.parse_args()

# print(args.input)
print(vars(args))
# print('first = %r' % args.first)


# input_path = args.Path

# if not os.path.isdir(input_path):
#     print('The path specified does not exist')
#     sys.exit()

# for line in os.listdir(input_path):
#     if args.long:  # Simplified long listing
#         size = os.stat(os.path.join(input_path, line)).st_size
#         line = '%10d  %s' % (size, line)
#     print(line)

# print('\n'.join(os.listdir(input_path)))
