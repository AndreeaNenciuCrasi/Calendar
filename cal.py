# main program
import sys
import ui

meetings_dic = {'8': '', '9': '', '10': '', '11': '', '12': '', '13': '', '14': '', '15': '', '16': '',
                '17': '', '18': '', '19': ''}


def schedule_meeting():
    global meetings_dic
    inputs = ui.get_inputs(
        ["Enter meeting title: ", "Enter duration in hours (1 or 2): ", "Enter start time: "], "")
    while inputs[1] != '1' and inputs[1] != '2':
        inputs = ui.get_inputs(
            ["Enter meeting title: ", "Enter duration in hours (1 or 2): ", "Enter start time: "], "")
    for i in meetings_dic.keys():
        if inputs[2] == i and inputs[1] == '1':
            meetings_dic[i] = inputs[0]
        elif inputs[2] == i and inputs[1] == '2':
            meetings_dic[i] = inputs[0]
            meetings_dic[str(int(i) + 1)] = inputs[0]


def cancel_meeting():
    global meetings_dic
    inputs = ui.get_inputs(
        ["Enter start time: "], "")
    for i in meetings_dic.keys():
        if inputs[0] == i and meetings_dic[i] != '':
            meetings_dic[i] = ''
        else:
            while inputs[0] == i and meetings_dic[i] == '':
                ui.print_error_message(
                    'There is no meeting starting at that time!')
                inputs = ui.get_inputs(["Enter start time: "], "")


def choose():
    inputs = ui.get_inputs(["Please enter an option: "], "")
    option = inputs[0]
    if option == "s":
        schedule_meeting()
        print(meetings_dic)
    elif option == "c":
        cancel_meeting()
        print(meetings_dic)
    elif option == "q":
        sys.exit(0)
    else:
        raise KeyError("There is no such option.")


def handle_menu():
    options = ["schedule a new meeting",
               "cancel an existing meeting",
               "quit"]

    ui.print_menu("Main menu", options, "quit")


def main():
    while True:
        handle_menu()
        try:
            choose()
        except KeyError as err:
            ui.print_error_message(str(err))


if __name__ == '__main__':
    main()
