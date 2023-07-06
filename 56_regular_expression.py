# Regular Expressions in Python
# Regular expressions, or "regex" for short, are a powerful tool for working with strings and text data in Python. They allow you to match and manipulate strings based on patterns, making it easy to perform complex string operations with just a few lines of code.

# Metacharacters in regular expressions
# []  Represent a character class
# ^   Matches the beginning
# $   Matches the end
# .   Matches any character except newline
# ?   Matches zero or one occurrence.
# |   Means OR (Matches with any of the characters
#     separated by it.
# *   Any number of occurrences (including 0 occurrences)
# +   One or more occurrences
# {}  Indicate number of occurrences of a preceding RE 
#     to match.
# ()  Enclose a group of REs












import re
patten = r"[A-Z]+lympic"
text = f"American amateur golfer and the first woman to win an Olympic event for the United States: the women's golf tournament at the 1900 Summer Olympics. Born in Calcutta in 1878, Abbott moved with her family to Chicago in 1884. She joined the Chicago Golf Club in Wheaton, Illinois, where she was coached by Charles B. Macdonald and H. J. Whigham. In 1899, she traveled with her mother to Paris to study art. The following year, along with her mother, she signed up for a women's golf tournament without realizing it was part of the second modern Olympics. Abbott won with a score of 47 strokes and was awarded a porcelain bowl; her mother tied for seventh. In December 1902, she married the writer Finley Peter Dunne. They moved to New York and had four children. Abbott died never realizing she won an Olympic event. She was not well known until University of Florida professor Paula Welch researched her life. The New York Times published her belated obituary in 2018."

match = re.search(patten, text)
# print(match)

matches = re.finditer(patten, text)
for i in matches:
    print(i)