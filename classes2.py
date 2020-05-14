class wordiplier:
    def __init__(self,word,num):
        self.word = word
        self.num = num
#    def __mul__(self,num):
#        return wordiplier(self.word*self.num)
x = wordiplier("Hello",4)

result = x.word*x.num
print(result)
