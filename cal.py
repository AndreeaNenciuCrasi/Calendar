# main program
import sys
import ui
import storage

meetings_dic = {'8': '', '9': '', '10': '', '11': '', '12': '', '13': '', '14': '', '15': '', '16': '',
                '17': '', '18': ''}


def schedule_meeting(meetings_dic):
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
    return meetings_dic


def cancel_meeting(meetings_dic):
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
    return meetings_dic


def change_meeting(meetings_dic):
    input_time = ui.get_inputs(
        ["Enter start time: "], "")
    while int(input_time[0]) < 8 or int(input_time[0]) > 18:
        ui.print_error_message(
            'Meeting is outside of your working hours (8 to 18)!')
        input_time = ui.get_inputs(
            ["Enter start time: "], "")
    return meetings_dic

    inputs = ui.get_inputs(
        ["Enter meeting title: ", "Enter duration in hours (1 or 2): ", "Enter start time: "], "")
    if input_time[0] == inputs[2]:
        for i in meetings_dic.keys():
            if input_time[0] == i and inputs[1] == '1':
                meetings_dic[i] = inputs[0]

            elif input_time[0] == i and inputs[1] == '2':
                meetings_dic[i] = inputs[0]
                meetings_dic[str(int(i) + 1)] = inputs[0]


def compact_meetings(meetings_dic):
    schedule = []
    for key, value in meetings_dic.items():
        if value != '':
            schedule.append(value)
            meetings_dic[key] = ''
    i = 0
    while i < len(schedule):
        meetings_dic[str(i+8)] = schedule[i]
        i += 1
    return meetings_dic


def choose():
    inputs = ui.get_inputs(["Please enter an option: "], "")
    option = inputs[0]

    if option == "s":
        ui.print_schedule(meetings_dic)
        ui.print_message(' Schedule a new meeting.')
        schedule_meeting(meetings_dic)
        ui.print_message(' Meeting added.')
        print(meetings_dic)
    elif option == "c":
        ui.print_schedule(meetings_dic)
        ui.print_message(' Cancel an existing meeting.')
        cancel_meeting(meetings_dic)
        ui.print_message(' Meeting canceled.')
        print(meetings_dic)
    elif option == "L":
        storage.export_schedule(meetings_dic)
        ui.print_message('\n Exported schedule')
    elif option == "M":
        ui.print_schedule(meetings_dic)
        change_meeting(meetings_dic)
        ui.print_message('\n Changed meeting')
    elif option == "z":
        compact_meetings(meetings_dic)
        ui.print_message('\n Compact meetings')
        ui.print_schedule(meetings_dic)
    elif option == "q":
        sys.exit(0)
    else:
        raise KeyError("There is no such option.")


def handle_menu():
    options = ["schedule a new meeting",
               "cancel an existing meeting",
               "Save and load",
               "Change meeting",
               "Compact meetings",
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
