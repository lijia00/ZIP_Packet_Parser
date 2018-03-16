# if Command Class is COMMAND_CLASS_ZIP, parse it this way
import ZW_classcmd as classcmd

command_classes = {classcmd.COMMAND_CLASS_ZIP: 'COMMAND_CLASS_ZIP' }
print(command_classes[0x23])


"""
input: take in the raw bytes
"""



# some_list_of_vars = ['some', 'list', 'of', 'vars']
# dict((eval(name), name) for name in some_list_of_vars)


def parse_cc_zip(data):
    length = len(data)
