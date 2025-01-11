class Time:
    min_hour = 0
    max_hour = 23
    max_second_minute = 59

    def __init__(self, hour, minute, second, format="24h"):
       self.horloge = (hour, minute, second, format)

    def in_seconds(self):
        in_second = self.horloge[0]*3600 + self.horloge[1]*60 + self.horloge[2]
        return in_second
        #epoch 

    def increment_time(self):
        if self.horloge[2] < Time.max_second_minute: # horloge [2] = second
            
            self.horloge = (self.horloge[0], self.horloge[1], self.horloge[2]+1, self.horloge[3])
        else:
            self.horloge[2] = 0
            if self.horloge[1] < Time.max_second_minute:#horloge[1]=minute
                self.horloge[1] += 1
            else:
                self.horloge[1] = 0 
                if self.horloge[0] < Time.max_hour: #horloge [0] = hour
                    self.horloge[0]+= 1
                else:
                    self.horloge[0] = 0

    def __str__(self):
        if self.horloge [3] == "24h": #horlorge [3]= format
            return f"{self.horloge[0] :02d} : {self.horloge[1]:02d} : {self.horloge[2]:02d}"
        else:
            if self.horloge [0] < 12:
                if self.horloge [0]  == 0:
                    return f"12 : {self.horloge[1]:02d} : {self.horloge[2]:02d} AM"
                return f"{self.horloge[0]:02d} : {self.horloge[1]:02d} : {self.horloge[2]:02d} AM"
            
            else:
                if self.horloge [0]  == 12:
                    return f"{self.horloge[0] :02d} : {self.horloge[1]:02d} : {self.horloge[2]:02d} PM"
                else:
                    return f"{(self.horloge[0] - 12):02d} : {self.horloge[1]:02d} : {self.horloge [2]:02d} PM"
      

class Alarm(Time):
    max_display = 10 #10 seconds

    def __init__(self, hour, minute, second, format, enabled=False):
        super().__init__(hour, minute, second, format)

        print(self.horloge)
        self.enabled = enabled
    
    def __str__ (self):
        if self.enabled:
            alarm_display = f"Alarm : {super().__str__()}"
            return f"{alarm_display:>30}"