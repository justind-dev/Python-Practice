# extending builtin python methods

class Text(str):
    def duplicate(self):
        return self + self

mytext = Text("Python")

print(mytext)

# mytext object also has all methods that a normal string would have. 
# Such as split, trim, etc...but now it has been extended to also
# include a 'duplicate' method to add the string to itself.
print(mytext.duplicate())


class TrackableList(list):
    # overwriting the built-in append method
    def append(self, object):
        print("Append called")
        #calling the built-in append method from the parent class
        super().append(object)

list = TrackableList()
list.append("1")
print(list)