
# Function to count the number of vowels in a given text
def count_vowels(text):

    # Define the vowels in the English alphabet
    vowels = "aeiou"

    # Convert the text to lowercase and check each character
    # Count 1 every time a character matches one of the vowels
    # sum() adds all the occurrences together
    return sum(1 for ch in text.lower() if ch in vowels)


# Main function: gets user input and displays the vowel count
def main():

    # Ask the user to enter a word, sentence, or text
    text = input("Enter text: ")

    # Call the count_vowels() function and display the result
    print(f"Vowels: {count_vowels(text)}")


# Check if the file is being executed directly
if __name__ == "__main__":

    # Call the main function to start the program
    main()
