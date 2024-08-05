nums = [7, 11, 1, 93, 2,0, 3, 8, 88, 4, 5, 70, 565, 13, 1111]
def circles(nums):
    output = []
    for i in nums:
        numZeroes = sorter(str(i))
        if len(output) == 0:
            output.append(i)
        elif numZeroes > 0:
            j = len(output)-1
            while sorter(str(output[j])) >= numZeroes:
                if output[j] < i and sorter(str(output[j])) == numZeroes:
                    break
                else:
                    j-=1

            output.insert(j+1, i)
        else:
            j = 0
            while output[j] < i and sorter(str(output[j])) <= numZeroes:
                j+=1
                if j ==len(output):
                    break
            output.insert(j, i)

                
                
    return output
                    


def sorter(num):
    ref = {"0":1, "4":1, "6":1, "8":2, "9":1}

    zeroes = 0
    while len(num) > 0:
        if num[-1] in ref:
            zeroes += ref[num[-1]]
        num = num[0:-1]
    return zeroes


            
    
circles(nums)
import random
def generateArr(size):

    mu = 1000
    stdev = 250

    arr = [0] * size

    for index in range(size):
        arr[index] = int(random.normalvariate(mu, stdev))
    
    return arr

def parse(arr):
    for item in arr:
        print(item)

def main():
    inputSize = 50

    parse(circles(generateArr(inputSize)))

main()