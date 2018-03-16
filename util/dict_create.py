

def generate_content(path):
    with open(path) as f:
        content = f.readlines()

    # generates a list containing each line in the file
    content = [x.strip() for x in content]
    return content


# given a line, find the location of this marker
def find_marker(mystring, symbol):
    return mystring.find(symbol)


def create_dict_from_variable_list(path):
    classcmd_dict = {}
    content = generate_content(path)
    for line in content:
        marker_location = find_marker(line, '=') + 4  # FIXME assuming there is a space after the equal sign
        cmd_value = line[marker_location:len(line)]
        cmd_name = line[:marker_location - 5]  # FIXME assuming there is a space before the equal sign
        classcmd_dict.update({cmd_value: cmd_name})

    return classcmd_dict
