# saving and loading files (after you implement it)


def export_schedule(meetings_dic):
    schedule = []
    count = 0
    for key, value in meetings_dic.items():
        if value != '':
            schedule.append(' ' + key + ' - ' +
                            str(int(key)+1) + ' : ' + value)
            file = open('meetings.txt', "w")
            file.write("Your schedule for the day:\n")
            for result in schedule:
                file.writelines(result)
                file.write("\n")
        else:
            count += 1

    if count == len(meetings_dic):
        file = open('meetings.txt', "w")
        file.write("Your schedule for the day:\n")
        file.write('empty')
