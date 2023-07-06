def insertMeaning():
    word = input("Enter the word:").lower()
    meaning = input("Enter the meaning of the word:").lower()
    aa = open("file_database.txt", 'a')
    final_word_meaning = f"{word}: {meaning} \n"
    aa.write(final_word_meaning)
    aa.close()


def findMeaning():
    word_meaning = input("Enter the word to find out meaning:")
    aa = open("file_database.txt", 'r')
    while aa:
        find_word = aa.readline().split(":")

        if (find_word[0] == word_meaning):
            print(':'.join(find_word))
            break

    aa.close()


while True:
    aa = int(input(
        "Enter '1' for inserting a meaning\nEnter '2' for finding a meaning\nEnter 'zero' for exit:"))
    if (aa == 1):
        insertMeaning()
    elif (aa == 2):
        findMeaning()
    else:
        break
