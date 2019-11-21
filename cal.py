# main program
import sys
import ui

meetings_dic = {'8': '', '9': '', '10': '', '11': '', '12': '', '13': '', '14': '', '15': '', '16': '',
                '17': '', '18': ''}


def schedule_meeting():
    global meetings_dic
    input_title = ui.get_inputs(["Enter meeting title: "], "")
    input_duration = ui.get_inputs(["Enter duration in hours (1 or 2): "], "")

    while input_duration[0] != '1' and input_duration[0] != '2':
        input_duration = ui.get_inputs(
            ["Enter duration in hours (1 or 2): "], "")

    input_time = ui.get_inputs(["Enter start time: "], "")
    while int(input_time[0]) < 8 or int(input_time[0]) > 18:
        ui.print_error_message(
            'Meeting is outside of your working hours (8 to 18)!')
        input_time = ui.get_inputs(
            ["Enter start time: "], "")

    for j in meetings_dic.keys():
        while input_time[0] == j and meetings_dic[j] != '':
            ui.print_error_message(
                'Meeting overlaps with existing meeting!')
            input_time = ui.get_inputs(["Enter start time: "], "")

    for i in meetings_dic.keys():
        if input_time[0] == i and input_duration[0] == '1':
            meetings_dic[i] = input_title[0]

        elif input_time[0] == i and input_duration[0] == '2':
            meetings_dic[i] = input_title[0]
            meetings_dic[str(int(i) + 1)] = input_title[0]


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
    global meetings_dic
    inputs = ui.get_inputs(["Please enter an option: "], "")
    option = inputs[0]
    ui.print_schedule(meetings_dic)
    if option == "s":
        ui.print_message(' Schedule a new meeting.')
        schedule_meeting()
        ui.print_message(' Meeting added.')
        print(meetings_dic)
        ui.print_schedule(meetings_dic)
    elif option == "c":
        ui.print_message(' Cancel an existing meeting.')
        cancel_meeting()
        ui.print_message(' Meeting canceled.')
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
