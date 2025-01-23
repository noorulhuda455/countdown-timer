import time  # Import the time module for creating delays
import os  # Import the os module for clearing the terminal screen

def countdown_timer(seconds):
    """
    A function to run a countdown timer that clears the screen
    and displays the remaining time with a progress bar.

    Parameters:
    seconds (int): The countdown time in seconds.
    """
    while seconds > 0:
        # Clear the screen for each second to refresh the display
        os.system('cls' if os.name == 'nt' else 'clear')  # 'cls' for Windows, 'clear' for other systems

        # Display the remaining time in seconds
        print(f"Time Remaining: {seconds} seconds")
        
        # Progress Bar visualization
        total_bar_length = 30  # Length of the progress bar
        progress = int((1 - (seconds / total_time)) * total_bar_length)  # Calculate the filled portion of the bar
        bar = '#' * progress + '-' * (total_bar_length - progress)  # Create the progress bar string
        print(f"[{bar}]")  # Display the progress bar
        
        time.sleep(1)  # Pause execution for 1 second
        seconds -= 1  # Decrement the seconds remaining by 1

    # Clear the screen one last time when the countdown ends
    os.system('cls' if os.name == 'nt' else 'clear')  # 'cls' for Windows, 'clear' for other systems

    # Notify the user that the time is up
    print("Time’s up!")
    
    # Optional: Try to play a beep sound (works on some systems)
    try:
        print('\a')  # '\a' is the ASCII bell character; it triggers a beep sound
    except:
        pass  # Ignore if the platform does not support the sound

# Main program entry point
if __name__ == "__main__":
    try:
        # Prompt the user to enter the countdown time in seconds
        total_time = int(input("Enter countdown time in seconds: "))
        
        # Validate that the input is a positive integer
        if total_time > 0:
            countdown_timer(total_time)  # Call the countdown_timer function with user input
        else:
            print("Please enter a positive number!")  # Error message for non-positive input
    except ValueError:
        # Handle cases where the user enters non-integer input
        print("Invalid input! Please enter an integer.")

