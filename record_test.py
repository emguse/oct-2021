import pyaudio
import wave

FORMAT = pyaudio.paInt16
CHANNELS = 1 # 1:mono 2:stereo
INPUT_DEVICE_INDEX = 1
CHUNK = 1024 *4
RATE = 44100 # sample rate
RECORD_SECONDS = 5

pa = pyaudio.PyAudio()

stream = pa.open(format=FORMAT,
                     channels=1,
                     rate=RATE,     
                     input=True, 
                     input_device_index=INPUT_DEVICE_INDEX, 
                     frames_per_buffer=CHUNK)

print("* recording")


f = []
try:
    for i in range(0, int(RATE / CHUNK * RECORD_SECONDS)):
        data = (stream.read(CHUNK))
        f.append(data)
finally:
    stream.stop_stream
    stream.close
    pa.terminate()
print("* done recording")

with wave.open('test2.wav', 'wb') as w:
    w.setnchannels(CHANNELS)
    w.setsampwidth(2)
    w.setframerate(RATE)
    w.writeframes(b''.join(f))

print("Output: test2.wav")