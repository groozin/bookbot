def count_words(book):
    words = book.split()
    return len(words)

def count_characters(book):
    characters = {}
    for char in book:
        lower_case_char = char.lower()
        if lower_case_char in characters:
            characters[lower_case_char] += 1
        else:
            characters[lower_case_char] = 1
    return characters

def main():
    with open('books/frankenstein.txt', 'r') as f:
        book = f.read()
        word_count = count_words(book)
        character_count = count_characters(book)

        print("--- Begin report of books/frankenstein.txt ---")
        print(f"{word_count} words found in the document")

        sorted_characters = sorted(character_count.items(), key=lambda x: x[1], reverse=True)
        for char, count in sorted_characters:
            print(f"The '{char}' character was found {count}times")


        print("--- End report ---")

if __name__ == '__main__':
    main()