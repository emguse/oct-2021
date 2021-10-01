import time

'''
A primitive polling timer module.
Provides a low-precision, fixed-cycle timer.
No compensation for cycle delay or advance is provided.
'''

class multi_timer():
    '''
    Multiple timers can be used simultaneously in this class.
    Create an instance with the interval [sec] as an argument.
    '''
    def __init__(self, interval):
        self.last_time = 0.0
        self.up_state = False
        self.interval = interval
        
    def timer(self):
        '''
        The timer method compares the current time with the interval 
        and updates the up_state at each call.
        '''
        if self.last_time + self.interval <= time.time():
            self.last_time = time.time()
            self.up_state = True

def main():
    INTERVAL_1s = float(1.0) # Enter the interval time in seconds
    INTERVAL_10s = float(10.0)  # Enter the interval time in seconds

    # timer instance creation
    timer_1s = multi_timer(INTERVAL_1s)
    timer_10s = multi_timer(INTERVAL_10s)

    while True:
        timer_1s.timer() # Call the method to update the timer
        if timer_1s.up_state == True:
            timer_1s.up_state = False # required to manually rewrite 'up_state' to False
            # Write the process here
            print("1sec: " + str(time.time()))
        timer_10s.timer()
        if timer_10s.up_state ==True:
            timer_10s.up_state = False # required to manually rewrite 'up_state' to False
            # Write the process here
            print("10sec: " + str(time.time()))
    return

if __name__ == "__main__":
  main()