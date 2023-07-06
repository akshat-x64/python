
string_1 = "This is a sample text"
string_1_list = string_1.split(" ")
string_1_final = []
print(string_1_list)
for word in string_1_list:
    if (len(word) >= 3):
        r1 = "Abc"
        r2 = "xyz"
        word = r1 + word[1:] + word[0] + r2
        print(word)
        string_1_final.append(word)
    else:
        word = word[::-1]
        string_1_final.append(word)
print(" ".join(string_1_final))
aa = " ".join(string_1_final)
print(aa)

string_1_list = aa.split(" ")
print(string_1_list)
akshat_final = []

for word in string_1_list:
    if (len(word) >= 3):
        word = word[3:-3]
        # print(word)

        word = word[-1] + word[0:-1]

        akshat_final.append(word)
    else:
        word = word[::-1]
        akshat_final.append(word)

print(" ".join(akshat_final))
