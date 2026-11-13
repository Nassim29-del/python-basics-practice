
# Import the time module to add delays between countdown numbers
import time


# Function that counts down from the given number of seconds
def countdown(seconds):

    # Continue the countdown as long as seconds is greater than zero
    while seconds > 0:

        # Convert total seconds into minutes and remaining seconds
        mins, secs = divmod(seconds, 60)

        # Display the countdown in MM:SS format
        # :02d ensures that each number has at least two digits
        # end="\r" updates the timer on the same line
        print(f"{mins:02d}:{secs:02d}", end="\r")

        # Pause the program for one second
        time.sleep(1)

        # Decrease the remaining time by one second
        seconds -= 1

    # Display 00:00 when the countdown reaches zero
    print("00:00")

    # Notify the user that the countdown has finished
    print("Time's up!")


# Check if this file is being executed directly
if __name__ == "__main__":

    # Ask the user for the countdown duration in seconds
    # Convert the input from a string to an integer
    countdown(int(input("Countdown from how many seconds? ")))
