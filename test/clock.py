import time, datetime, message

#datetime.time.now()

def clock_ticking(clock_datetime, clock_time):
    clock_datetime = clock_datetime + datetime.timedelta(seconds=1)
    clock_time.clock = (int(clock_datetime.strftime('%H')), int(clock_datetime.strftime('%M')), int(clock_datetime.strftime('%S')))
    
    # %I = hour in 12h format
    clock_time.ampm_hour = int(clock_datetime.strftime('%I'))
    # %1
    clock_time.format = clock_datetime.strftime('%p')


def display_clock(event, clock_time, dic_cursor):
    while True:
        event.wait()
        if clock_time.mode == False:
            clock_datetime = datetime.datetime(1970, 1, 1, clock_time.clock[0], clock_time.clock[1], clock_time.clock[2])
            print(f"{dic_cursor["delete_line_1-clock"]}{clock_datetime.strftime('%H:%M:%S')}{dic_cursor["cursor_position_load"]}", end="", flush=True)
        else:
            clock_datetime = datetime.datetime(1970, 1, 1, clock_time.ampm_hour, clock_time.clock[1], clock_time.clock[2])
            print(f"{dic_cursor["delete_line_1-clock"]}{clock_datetime.strftime('%I:%M:%S')} {clock_time.format}{dic_cursor["cursor_position_load"]}", end="", flush=True)
            
        clock_ticking(clock_datetime, clock_time)

        time.sleep(1)

def change_clock(dic_cursor, clock_time):
    while True:
        # error check
        # debug display concatenated
        user_clock = input(f"{dic_cursor["delete_line_1-clock"]}__:__:__{dic_cursor["cursor_position_start"]}")
       # try: 
  
        
        user_clock += input(f"{dic_cursor["cursor_position_start"]}{user_clock[0:2]}:")
        user_clock += input(f"{dic_cursor["cursor_position_start"]}{user_clock[0:2]}:{user_clock[2:4]}:")
        if clock_time.mode == True:
            clock_time.format = input(f"{dic_cursor["cursor_position_start"]}{user_clock[0:2]}:{user_clock[2:4]}:{user_clock[4:]} ")











        message.clock_valid(dic_cursor)
        print(dic_cursor["cursor_position_load"])
        return (int(user_clock[0:2]), int(user_clock[2:4]), int(user_clock[4:]))