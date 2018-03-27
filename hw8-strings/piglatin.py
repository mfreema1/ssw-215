#Mark Freeman
vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
def getIndexOfVowel(str):
    index = 0
    for letter in str:
        if letter in vowels:
            return index
        else:
            index += 1

def translate(str):
    arr = str.split()
    latin_arr = []
    for word in arr:
        if word[0] in vowels:
            latin_arr.append(word + "way")
        else:
            index = getIndexOfVowel(word)
            latin_arr.append(word[index:] + word[:index] + "ay")
    return " ".join(latin_arr)

if __name__ == "__main__":
    while(1):
        text_to_translate = input("Enter a sentence to translate: ")
        print(translate(text_to_translate))