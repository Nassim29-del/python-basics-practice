
# Function to check whether a given text is a palindrome
def is_palindrome(text):

    # Remove spaces and punctuation, and convert all characters to lowercase
    # Keep only letters and numbers using isalnum()
    cleaned = "".join(ch.lower() for ch in text if ch.isalnum())

    # Compare the cleaned text with its reverse
    # [::-1] reverses the string
    return cleaned == cleaned[::-1]


# Main function: gets user input and displays the result
def main():

    # Ask the user to enter a word, phrase, or sentence
    text = input("Enter text: ")

    # Check whether the entered text is a palindrome
    # Display the appropriate message based on the result
    print("Palindrome!"
          if is_palindrome(text)
          else "Not a palindrome")


# Check if the file is being executed directly
if __name__ == "__main__":

    # Call the main function to start the program
    main()
