def main():
        sentence = input("Enter desired word to reverse")

        while True:
            print("\n--- MENU ---")
            print("""    0. Enter new Sentence
                        1. Display Sentence
                        2. Count number of characters
                        3. Count number of words
                        4. Convert to UPPERCASE
                        5. Convert to lowercase
                        6. Reverse Sentence
                        7. Count vowels
                        8. Count consonants
                        9. Exit
                            """)
                        
            choice = input(" Enter your choice 0-9:") 

            if choice == "0":
                sentence = input("Enter new sentence:")
            elif choice =="1":
                print("Sentence:", sentence)
            elif choice == "2":
                print("number of characters:", len(sentence))
            elif choice == "3":
                print("Number of words:", len(sentence.split()))
            elif choice == "4":
                print(sentence.upper())
            elif choice == "5":
                print(sentence.lower())
            elif choice == "6":
                print("Reversed Sentence:", sentence[::-1])
            elif choice == "7":
                vowels = "aeiouAEIOU"
                count = sum(1 for ch in sentence if ch in vowels)
                print("Number of vowels:", count)
            elif choice == "8":
                consonants = "bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ"
                count = sum(1 for ch in sentence if ch in consonants)
                print("Number of consonants:", count)

            elif choice == "9":
                print("Exiting program... Goodbye!")
                break

            else:
                print("Invalid choice, try again.")
            
            
                
