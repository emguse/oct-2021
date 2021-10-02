import pyaudio

def main():
    audio = pyaudio.PyAudio()

    # List index numbers for each voice device
    for x in range(0, audio.get_device_count()): 
        print(audio.get_device_info_by_index(x))

if __name__ == '__main__':
    main()