def main():
    book_path = "book/frankenstein.txt"
    text = get_book_text(book_path)
    word_count = get_word_count(text)
    character_occurence(text)
    generate_report(text)

def get_book_text(path):
    with open(path) as f:
        return f.read()

def get_word_count(text):
    return len(text.split())
          
def character_occurence(text):
    map = {}
    for s in text.split():
        for c in s.lower():
            if c.isalnum():
                map[c] = map.get(c, 0) + 1
    return map


def generate_report(text):
    print("--- Begin report of books/frankenstein.txt ---")
    print(f"{get_word_count(text)} words found in the document")

    map = character_occurence(text)

    for k,v in map.items():
        print(f"The '{k}' character was found {v} times\n")
    
    print("--- End report ---")

main()   


