class Time:
    min_hour = 0
    max_hour = 23
    max_second_minute = 59

    def __init__(self, hour, minute, second, format="24h"):
        self.hour = hour
        self.minute = minute
        self.second = second
        self.format = format
        self.in_seconds()

    def in_seconds(self):
        self.in_second = self.hour*3600 + self.minute*60 + self.second
        return self.in_second
        #epoch 

    def increment_time(self):
        if self.second < Time.max_second_minute:
            self.second += 1
        else:
            self.second = 0
            if self.minute < Time.max_second_minute:
                self.minute += 1
            else:
                self.minute = 0
                if self.hour < Time.max_hour:
                    self.hour += 1
                else:
                    self.hour = 0

    def display_time(self):
        # self.change_format()
        if self.format == "24h":
            return f"{self.hour:02d} : {self.minute:02d} : {self.second:02d}"
        else:
            if self.hour < 12:
                if self.hour == 0:
                    return f"12 : {self.minute:02d} : {self.second:02d} AM"
                return f"{self.hour:02d} : {self.minute:02d} : {self.second:02d} AM"
            
            else:
                if self.hour == 12:
                    return f"{self.hour:02d} : {self.minute:02d} : {self.second:02d} PM"
                else:
                    return f"{(self.hour - 12):02d} : {self.minute:02d} : {self.second:02d} PM"
      

    # def change_format(self, new_format):

    #     if self.format == "12h" and new_format == "24h":
    #         if self.hour < 12:
    #             return f"{self.hour:02d} : {self.minute:02d} : {self.second:02d}"
    #     elif self.format == "24h" and new_format == "12h":
    #         if self.hour < 12:
    #             if self.hour == 0:
    #                 return f"12 : {self.minute:02d} : {self.second:02d} AM"
    #             return f"{self.hour:02d} : {self.minute:02d} : {self.second:02d} AM"
    #         else:
    #             if self.hour == 12:
    #                 return f"{self.hour:02d} : {self.minute:02d} : {self.second:02d} PM"
    #             else:
    #                 return f"{(self.hour - 12):02d} : {self.minute:02d} : {self.second:02d} PM"


    def __str__ (self):
        return self.display_time()
 
class Alarm(Time):
    max_display = 10 #10 seconds

    def __init__(self, hour, minute, second, format, enabled=False):
        self.hour = hour
        self.minute = minute
        self.second = second
        self.format = format
        self.enabled = enabled
        self.in_seconds()
    
    def __str__ (self):
        if self.enabled:
            alarm_display = f" Alarm : {self.hour:02d} : {self.minute:02d} : {self.second:02d}"
            return f"{alarm_display:>30}"

        # if self.enabled:
        #     return f" ; Alarm : {self.hour:02d} : {self.minute:02d} : {self.second:02d}" + self.display_alarm(self, clock)
        # else:
        #     return ""

