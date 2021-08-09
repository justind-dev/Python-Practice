class TagCloud:
    def __init__(self):
        #double underscore to create private attributes
        #this does not mean its not accessible, its more of a 
        # "hey im private so dont touch me warning to those viewing the source"
        self.__tags = {}

    def add(self, tag):
        self.__tags[tag.lower()] = self.__tags.get(tag.lower(), 0) + 1
    
    def __getitem__(self, tag):
        return self.__tags.get(tag.lower(), 0)

    def __len__(self):
        return len(self.__tags)
    
    def __setitem__(self, tag, count):
        self.__tags[tag.lower()]=count

    def __iter__(self):
        return iter(self.__tags)

cloud = TagCloud()

#add some items to the tag cloud 'cloud' object
cloud.add("python")
cloud.add("python")
cloud.add("Python")
cloud.add("C#")
cloud.add("Java")
cloud.add("Java")

#this will throw an error, because the objects __tags attribute has been made private
#print(cloud.__tags)

#our dictionary can still be viewed here
print(cloud.__dict__)

#and thus we can still access the tags by doing this, object._ClassName__privateattribute
print(cloud._TagCloud__tags)