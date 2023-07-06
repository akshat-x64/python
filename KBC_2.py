aa = input("Enter your name:")
print(f"Welcome {input}")
questions_stack = [["What is the capital of india?", "A.delhi", "B.bhopal",
                    "C.Charles Babbage", "D.Central Processing Unit", "a"],
                   ["What is the capital of india?", "A.delhi", "B.bhopal",
                    "C.Charles Babbage", "D.Central Processing Unit", "a"],
                   ["What is the capital of india?", "A.delhi", "B.bhopal",
                    "C.Charles Babbage", "D.Central Processing Unit", "a"],
                   ["What is the capital of india?", "A.delhi", "B.bhopal",
                    "C.Charles Babbage", "D.Central Processing Unit", "a"],
                   ["What is the capital of india?", "A.delhi", "B.bhopal",
                    "C.Charles Babbage", "D.Central Processing Unit", "a"],
                   ["What is the capital of india?", "A.delhi", "B.bhopal",
                    "C.Charles Babbage", "D.Central Processing Unit", "a"],
                   ["What is the capital of india?", "A.delhi", "B.bhopal",
                    "C.Charles Babbage", "D.Central Processing Unit", "a"],
                   ["What is the capital of india?", "A.delhi", "B.bhopal",
                    "C.Charles Babbage", "D.Central Processing Unit", "a"], ["What is the capital of india?", "A.delhi", "B.bhopal",
                                                                             "C.Charles Babbage", "D.Central Processing Unit", "a"], ["What is the capital of india?", "A.delhi", "B.bhopal",
                                                                                                                                      "C.Charles Babbage", "D.Central Processing Unit", "a"]]
levels = [1000, 2000, 3000, 5000, 10000, 20000, 40000, 80000, 160000, 320000]
for i in range(len(questions_stack)):
    questions = questions_stack[i]

    print(questions[0], f"for Rs{levels[i]}")
    print(questions[1], questions[2])
    print(questions[3], questions[4], "press 0 for quit")
    a = input("Enter correct option:")
    if (a == questions[-1]):
        print(f"correct ")
    elif (a == "0"):
        print(f"you won {levels[i]}")
        break
    else:
        if (i <= 4):
            print(f"Wrong answer you won 0")
        elif (i > 4):
            print(f"Wrong answer you won{levels[5]}")
        break
