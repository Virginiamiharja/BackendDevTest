def displayTitle():
    print("Virginia Vowels Alphabet Check")

def countChar(word):
    vowels = 'aeiouAEIOU'
    count = 0
    for vowel in word:
        if vowel in vowels:
            count += 1
    return count
   

def main():
    
    displayTitle()

    word = input("Input word: ")

    totalVowel = countChar(word)

    if totalVowel == 0:
        print ("Vowel not found")
    else:
        print("Number of vowels in your input:", totalVowel)
        
if __name__ == "__main__":
    main()