import time

last_spoken_time = time.time()
speech_delay = 2  # in seconds

def should_speak(current_time):
    global last_spoken_time
    if current_time - last_spoken_time > speech_delay:
        last_spoken_time = current_time
        return True
    return False
