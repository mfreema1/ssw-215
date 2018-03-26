vowels = ['a', 'e', 'i', 'o', 'u']
def place_at_end(str):
    return str[1:] + str[0]

def translate(str):
    arr = str.split()
    for word in arr:
        if word[0] in vowels:
            word += "way"
        else:
            while(word[0] not in vowels):   #move first character to end until vowel
                word = place_at_end(word)
            word += "ay"
    return arr.join(" ")

if __name__ == "__main__":
    while(1):
        text_to_translate = input("Enter a sentence to translate: ")
        print(translate(text_to_translate))