import re

class combination():
    def __init__(self, string, regex="(.*?)"):
        self.compiled = ""
        self.count = 0
        self.strCount = 0
        
        for charIndex in range(len(string)):
            character = string[charIndex]

            if len(re.findall(regex, character)) > 0:
                strippedString = string[:charIndex] + string[charIndex + 1:]

                #print("mainStr: " + string)
                #print("mainCharacter: " + character)
                #print("strippedString: " + strippedString)

                self.strCount += 1

                for charIndex in range(len(strippedString)):
                    newCharacter = string[charIndex]

                    #print("newCharacter: " + newCharacter)

                    self.compiled = self.compiled + "\n" + character + newCharacter + strippedString[:charIndex] + strippedString[charIndex + 1:]
                    self.count += 1

            #print("----------")

    def getStrCount(self):
        return self.strCount

    def getCount(self):
        return self.count

    def getString(self):
        return self.compiled