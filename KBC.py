name_1 = input("Enter your name:")
print(f"Welcome {name_1}")
list_qustions = ["What is the capital of india?",
                 "What is the capital of mp?", "Who is the father of Computers?", "What is the full form of CPU?"]
list_options = [["A.delhi", "B.bhopal",
                "C.Charles Babbage", "D.Central Processing Unit"], ["A.delhi", "B.bhopal",
                "C.Charles Babbage", "D.Central Processing Unit"], ["A.delhi", "B.bhopal",
                "C.Charles Babbage", "D.Central Processing Unit"], ["A.delhi", "B.bhopal",
                "C.Charles Babbage", "D.Central Processing Unit"]]
list_answers = ["a", "b", "c", 'd']
list_input_users = []
list_num = 0
while (list_num < len(list_qustions)):
    print(list_qustions[list_num])
    for i in range(4):
        print(i)
        print(list_options[list_num][i])
    aa = input(":")
    list_input_users.append(aa)
    list_num = list_num+1

print(list_input_users)
for i in range(len(list_qustions)):
    if (list_answers[i] == list_input_users[i]):
        print("correct")

    else:
        print("wrong")
    print(i)
