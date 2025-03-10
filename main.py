import sys
from stats import count_words 
from stats import count_character_occurances
from stats import sorted_character_occurances

def get_book_text(filepath):
    with open(filepath) as file:
        contents = file.read()
    return contents

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    
    book = sys.argv[1]

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book}...")
    words = get_book_text(book)
    count = count_words(words)
    print("----------- Word Count ----------")
    print(f"Found {count} total words")
    occurances = count_character_occurances(words)
    sorted = sorted_character_occurances(occurances)
    print("--------- Character Count -------")
    for value in sorted:
        print(f"{value["letter"]}: {value["count"]}")
    print("============= END ===============")

main()
