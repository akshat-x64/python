from final import welcome, akshat


def strEnc(word):
    if (len(word) < 3):
        temp = word[1]
        word = temp + word[0]
        return word
    else:
        temp = word[1:]
        word = temp + word[0]
        final = ""
        for i in word:
            final = i + final
        final = final + "asd"
        final = "asd" + final
        print(final)
        # return final


def strDnc(word):
    if (len(word) < 3):
        temp = word[1]
        word = temp + word[0]
        return word
    else:
        temp = word[3:]
        temp = temp[0:-3]
        i_1 = ""
        for i in temp:
            i_1 = i + i_1
        aa = i_1[-1]
        i_1 = i_1[0:-1]
        i_1 = aa+i_1
        print(i_1)
        # return i_1


while (True):
    print("Enter 'A' to encrypt word")
    print("Enter 'B' to decrypt word")
    print("Enter '0' to exit from program")
    inp = input(":")
    if (inp.upper() == "A"):
        inp_2 = input("Enter a word:")
        strEnc(inp_2)
    elif (inp.upper() == "B"):
        inp_2 = input("Enter a word:")
        strDnc(inp_2)
    elif (inp == "0"):
        break


# print(strEnc("Akshat"))
# print(strDnc("asdAtahskasd"))
welcome()
print(akshat)
