def main():
    path_to_file = "books/frankenstein.txt"
    text = get_book_text(path_to_file)
    num_words = get_num_words(text)

    print(f"{num_words} words found in text\n")

    character_dict = (count_character(text))    
    sorted_characters = sorted(character_dict.items(), key=sort_on, reverse=True)
   
    # print(character_dict)
    for char in sorted_characters:
        print(f"The '{char[0]}' character was found {char[1]} times")

def get_book_text(path_to_file):
    with open(path_to_file) as f:
        text = f.read()
        return text        
        
def get_num_words(text):
    words = text.split()
    count = len(words)
    return count

def count_character(text):
       
    character_dict = {
    "a": 0,
    "b": 0,
    "c": 0,
    "d": 0,
    "e": 0,
    "f": 0,
    "g": 0,
    "h": 0,
    "i": 0,
    "j": 0,
    "k": 0,
    "l": 0,
    "m": 0,
    "n": 0,
    "o": 0,
    "p": 0,
    "q": 0,
    "r": 0,
    "s": 0,
    "t": 0,
    "u": 0,
    "v": 0,
    "w": 0,
    "x": 0,
    "y": 0,
    "z": 0
    }

    # takes text from book 
    # loop over every character
    # if match, concatenate in dictionary under that key
    for t in text.lower():   
        if t in character_dict:
            character_dict[t] += 1

    return character_dict


def sort_on(character_dict):
    return character_dict[1]   
     # sort the characters by numbers of occurance
    # from high to low    
    # return number of times each character exists


if __name__ == '__main__':
    main()