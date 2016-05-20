class TwoSum(object):
    answer={}

    def add(self,input):
        if(input in self.answer):  #python3.0之后没有has_key了，改为 key in table形式
            count=self.answer.get(input)
        else:
            count=0
        self.answer[input]=count+1

    def find(self,val):
        for entry in self.answer:
            y=val-entry
            if(y==entry):
                if(self.answer[entry]>=2):  #如果是两个相同数字的和，在answer中有两个或以上的值，那么返回true
                    return True
            elif(y in self.answer):
                return True
        return False

my_twosum=TwoSum()
my_twosum.add(1)
my_twosum.add(3)
my_twosum.add(3)
my_twosum.add(5)
print(my_twosum.find(4))

if __name__=="__main__":
    print("i am the main")
else:
    print("i am not")