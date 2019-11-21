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
    Sample display:
        Please provide your personal information
        Name <user_input_1>
        Surname <user_input_2>
        Age <user_input_3>

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
    """
    Displays an error message (example: ``Error: @message``)

    Args:
        message (str): error message to be displayed

    Returns:
        None: This function doesn't return anything it only prints to console.
    """

    print(f'Error - {message}')
