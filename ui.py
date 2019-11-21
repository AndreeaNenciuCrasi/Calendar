# printing data, asking user for input


def print_menu(title, list_options, exit_message):
    print(f'    {title}')
    letter_list = ['s', 'c', 'q']
    i = 1
    while i < len(list_options):
        print(f'        ({letter_list[i-1]}) {list_options[i-1]}')
        i += 1
    print(f'        (q) {exit_message}')


def get_inputs(list_labels, title):
    """
    Gets list of inputs from the user.
    Sample call:
        get_inputs(["Name","Surname","Age"],
                    "Please provide your personal information")

    Args:
        list_labels (list): labels of inputs
        title (string): title of the "input section"

    Returns:
        list: List of data given by the user. Sample return:
            [<user_input_1>, <user_input_2>, <user_input_3>]
    """

    i = 0
    inputs = []
    while i < len(list_labels):
        inputs.append(input(f'{title} {list_labels[i]}'))
        i += 1
    return inputs


def print_error_message(message):
    print(f'Error - {message}')


def print_message(message):
    print(f"{message}  \n")


def print_schedule(meetings_dictionary):
    print('\n Your schedule for the day: ')
    count = 0
    for key, value in meetings_dictionary.items():
        if value != '':
            print(' ' + key + ' - ' + str(int(key)+1) + ' : ' + value)
        else:
            count += 1

    if count == len(meetings_dictionary):
        print(' (emty)')
    print('\n')
