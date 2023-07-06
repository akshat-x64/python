aa = "dogs runs"

a2 = aa.split()
a2.remove("dogs")
# print(a2.("runs"))
if "runs" in aa:
    print("Pppp")

class Multiset:
    aa = []

    def add(self, val):
        self.aa.append(val)
# adds one occurrence of val from the multiset, if any
    def remove(self, val):
        self.aa.remove(val)
        # removes one occurrence of val from the multiset, if any
    def __contains__(self, val):
        
        if val in self.aa:
        # returns True when val is in the multiset, else returns False
            return True
        else: 
            return False
    
    
    def __len__(self):
        # returns the number of elements in the multiset
        return len(self.aa)

aa = Multiset()
aa.add("Akshat")
aa.add("Ankit",)
aa.add("pancholi")
print(len(aa))
print(aa.__contains__("Ankit"))