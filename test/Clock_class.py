from datetime import datetime
import time, display

class Clock:
    def __init__(self, clock, ampm_hour, format, mode):
        self.clock = clock
        self.ampm_hour = ampm_hour
        self.format = format
        self.mode = mode

    def clock_ticking(self, clock_datetime):
        clock_datetime = clock_datetime + datetime.timedelta(seconds=1)
        self.clock = (int(clock_datetime.strftime('%H')), int(clock_datetime.strftime('%M')), int(clock_datetime.strftime('%S')))
        
        # %I = hour in 12h format
        self.ampm_hour = int(clock_datetime.strftime('%I'))
        # %p = AM/PM
        self.format = clock_datetime.strftime('%p')

    def display_clock(self, event):
        while True:
            event.wait()
            if self.mode == False:
                clock_datetime = datetime.datetime(1970, 1, 1, self.clock[0], self.clock[1], self.clock[2])
                # TODO display the tuple instead; change datetime only in change_clock
                display.clock_24h(self)
            else:
                clock_datetime = datetime.datetime(1970, 1, 1, self.ampm_hour, self.clock[1], self.clock[2])
                display.clock_12h(self)
                
            self.clock_ticking(clock_datetime)

            time.sleep(1)

    def change_clock(self):
        while True:
            clock_config = display.input_clock_config()

            if clock_config == "automatique" or clock_config == "auto" or clock_config == "a":
                current_time = datetime.now()
                return (int(current_time("%H")), int(current_time("%M")), int(current_time("%S")))

            elif clock_config == "manuel" or clock_config == "m":
                while True:
                    user_clock = display.input_user_clock()
                        
                    #Verify if it's a number
                    try:
                        test = int(user_clock)
                    except Exception:
                        display.error_NaN()
                        continue

                    #Verify if it's a valid hour with datetime error directly
                    try:
                        test = datetime.datetime(1970, 1, 1, user_clock[:2], user_clock[2:4], user_clock[4:])
                    except Exception:
                        display.error_invalid_time()
                        continue

                    #Verify if the input contain exactly 6 numbers
                    if len(user_clock) != 6:
                        display.error_number_length()
                        continue

                    if self.mode == True:
                        user_format = display.input_user_format(user_clock)
                        
                        if self.format != "AM" and "PM":
                            display.error_format()
                            continue

                        self.format = user_format
                        if user_format == "PM" and user_clock[:2] != "12":
                            user_clock[:2] = int(user_clock[:2])+12
                        elif user_format == "AM" and user_clock[:2] == "12":
                            user_clock[:2] = "00"

                    display.message_clock_valid()
                        
                    self.clock = (int(user_clock[0:2]), int(user_clock[2:4]), int(user_clock[4:]))
                    return    
            
            else:
                continue