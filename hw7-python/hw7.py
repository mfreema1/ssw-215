def appendToFile():
    with open('file.txt', 'a') as fileObject:
        while(1):
            strToAppend = input('Please enter something to append, enter nothing to quit: ')
            if(strToAppend == ''):
                break
            fileObject.write(strToAppend + '\n')

def clearFile():
    with open('file.txt', 'w') as fileObject:
        fileObject.write('')

def readFileLines():
    with open('file.txt', 'r') as fileObject:
        for line in fileObject:
            print(line, end='\n')

def printMenu():
    print('I am a text file manager.  Please enter what you would like to do.', end='\n')
    print('Enter 1 to clear the text file', end='\n')
    print('Enter 2 to read the file', end='\n')
    print('Enter 3 to append to the file', end='\n')
    print('Anything else to quit: ')

if __name__ == '__main__':
    while(1):
        printMenu()
        choice = int(input())
        if(choice == 1):
            clearFile()
        elif(choice == 2):
            readFileLines()
        elif(choice == 3):
            appendToFile()
        else:
            break
