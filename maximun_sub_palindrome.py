### ¡¡¡¡¡¡¡¡¡Function to validate if the words between spaces in a string are palindromes!!!!!!!! ###

def sub_pal_per_space(string):
    # Convert the string to lowercase to ensure case-insensitive comparison
    lowerString = string.lower()
    # Add a space at the end to ensure the last word is processed
    lowerString += " "   
    arraySetWords = set()
    # Initialize an empty array to store tuples of start and end indices of palindromes
    newArray = []
    
    # Helper function to check if a given word is a palindrome
    def validate_palindrome(word):
        # Compare the word with its reverse
        return word == word[::-1] 
    
    # Variable to build the current word
    newWord = ""
    # Variable to track the start index of the current word
    start = 0
    
    # Iterate through each character in the string
    for end in range(len(lowerString)):
        # If the current character is not a space, add it to the current word
        if(lowerString[end] != " "):
            newWord += lowerString[end]
        else:
            # If a word exists, check if it's a palindrome
            if newWord and len(newWord) >= 3: 
                isP = validate_palindrome(newWord) 
                # If the word is a palindrome, store its start and end indices as a tuple
                if isP and not newWord in arraySetWords:
                    tupla = (start, end - 1)
                    newArray.append(tupla)
                    arraySetWords.add(newWord)
            # Reset the current word for the next iteration
            newWord = ""            
            # Update the start index for the next word
            start = end + 1
    
    # Return the sorted list of tuples
    return newArray


# Example usage:
print(sub_pal_per_space("Madam Arora teaches malam"))
print(sub_pal_per_space("A man a plan a canal Panama"))
print(sub_pal_per_space("Anna Anna Civic Civic"))
#Output: [(0, 4), (6, 10), (20, 24)]


            

            




