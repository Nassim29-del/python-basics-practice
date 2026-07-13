# Counts down from a given number of seconds, then announces it's done.

import time


def countdown(seconds):
    while seconds > 0:
        mins, secs = divmod(seconds, 60)
        print(f"{mins:02d}:{secs:02d}", end="\r")
        time.sleep(1)
        seconds -= 1
    print("00:00")
    print("Time's up!")


if __name__ == "__main__":
    countdown(int(input("Countdown from how many seconds? ")))
