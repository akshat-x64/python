import os
allfiles = os.listdir("images")
print(allfiles)

aa = 1
for i in allfiles:
    if i.endswith(".jpg"):
        os.rename(f"images/{i}", f"images/a{i}.jpg")
        aa = aa+1
