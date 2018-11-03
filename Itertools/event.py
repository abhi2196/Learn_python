import itertools

names = 'Tim Bob Julian Carmen Sofia Mike Kim Andre'.split()
locations = 'DE ES AUS NL BR US'.split()
confirmed = [False, True, True, False, True]

dash = itertools.cycle('-')

def append_dashes(data, max_length):
    data_len = len(data)
    for i in range(data_len, max_length+1):
        data.append(next(dash))

def get_attendees():
    append_dashes(locations, 8)
    append_dashes(confirmed, 8)
    
    for participant in zip(names, locations, confirmed):
        print(participant)
    

if __name__ == '__main__':
    get_attendees()
