f = open("file4.txt", 'w')

list_1 = ["This is a sample text\n", "This is a sample text\n",
          "This is a sample text\n", "This is a sample text\n", "This is a sample text\n"]

f.writelines(list_1)
f.close()
