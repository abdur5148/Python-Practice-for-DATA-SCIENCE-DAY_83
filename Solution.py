class Person(object):
    def getGender(self):
        return "Human"


class Male(Person):

    def getGender(self):
        return "Male"


class Female(Person):
    def getGender(self):
        return "Female"


var1Male = Male()
var2Female = Female()
print(var1Male.getGender())
print(var2Female.getGender())
