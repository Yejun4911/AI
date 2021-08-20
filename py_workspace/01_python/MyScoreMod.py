
def getSum(data):
    total=0
    for i in data:
        total+=i
    return total

def getMean(data):
    return getSum(data)/len(data)

def getMax(data):
    maxV=data[0]
    for i in data[1:]:
        if i>max:
            maxV=i
            
    return maxV
def getMin(data):   
    minV=data[0]
    for i in data[1:]:
        if i<max:
            minV=i
    return minV
def getTwoSum(num1,num2):
    sum=0
    if num1<num2:
        num1,num2 = num2,num1;
    for i in range(num1,num2):
        sum+=i
    return 0
