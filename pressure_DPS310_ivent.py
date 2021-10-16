import RPi.GPIO as gpio
import time
import pressure_DPS310_csv as DPS310
import multi_timer
import csv
import datetime
from collections import deque

BUTTON_PIN = 5 # slot D5
SAVE_DIR = 'press_log/'
SAVE_LENGTH = 5 # [sec]
BUTTON_MASK = 1.0 # [sec]

def export(d):
    today = datetime.date.today()
    filename = str(SAVE_DIR + today.strftime('%Y%m%d') + '-' + time.strftime('%H%M%S') + '.csv')
    with open(filename, 'w', newline='') as f:
        writer = csv.writer(f)
        print("Start exporting")
        for i in d:
            writer.writerow(i)
        print("Export Complete")

def main():
    gpio.setmode(gpio.BCM)
    gpio.setup(BUTTON_PIN,gpio.IN)

    dps310 = DPS310.pressure_sensor_DPS310() # Instance creation
    dps310_timer = multi_timer.multi_timer(dps310.read_interval) 
    button_mask = multi_timer.multi_timer(BUTTON_MASK)

    Factors = dps310.read_calibration_coefficients() # Read Calibration Coefficients

    ivent_length = SAVE_LENGTH * (1/dps310.read_interval)
    d = deque(maxlen=int(ivent_length))

    while True:
        try:
            dps310.start_measurement()
            while True:
                dps310_timer.timer()
                button_mask.timer()
                if dps310_timer.up_state == True:
                    dps310_timer.up_state = False
                    # process
                    scaled_temp ,temperature = dps310.read_temperature(Factors) # read and compensation temperature
                    press = dps310.read_pressure(scaled_temp, Factors) # read and compensation pressure
                    #print(str(time.time()) + "," + str(press))
                    data = [str(time.time()),str(press)]
                    d.append(data)
                if gpio.input(BUTTON_PIN) and button_mask.up_state == True:
                    button_mask.up_state = False
                    export(d)
        finally:
            dps310.stop_measurement()
            gpio.cleanup()

if __name__ == "__main__":
  main()