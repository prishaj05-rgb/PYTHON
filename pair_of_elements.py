#creat class
class pair_of_elements:

    def twoSum(self,nums,target):
        #create and empty dictionary
        lookup = {}

        #iterate through the tuple 
        for i, num in enumerate(nums):
            if target - num in lookup:
                return (lookup[target - num], i)    
            lookup[num] = i

#take value of num from user
value = int(input("Enter sum from which you want to make this search: "))

print("index1=%d, index2=%d" %pair_of_elements().twoSum((10,20,30,40,50,60,70), value))

