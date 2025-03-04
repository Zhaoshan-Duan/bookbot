from stats import get_word_count, character_occurence
import sys

def main():
    if len(sys.argv) != 2:
        print("python3 main.py <path_to_book>")
        sys.exit()

    book_path = sys.argv[1]
    text = get_book_text(book_path)
    word_count = get_word_count(text)
    character_occurence(text)
    generate_report(text)

def get_book_text(path):
    with open(path) as f:
        return f.read()

def generate_report(text):
    print("============ BOOKBOT ============")
    print("Analyzing book found at books/frankenstein.txt...")
    print("----------- Word Count ----------")
    print(f"Found {get_word_count(text)} total words")

    map = character_occurence(text)

    print("--------- Character Count -------")
    for k in map:
        # print(f"The '{k}' character was found {v} times\n")
        print(f"{k}: {map[k]}")
    
    print("--- End report ---")

main()   


