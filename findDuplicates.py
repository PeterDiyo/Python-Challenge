numbers = [3,6,2,4,3,]
for i in range (len(numbers)):
    for j in range (i+1, len(numbers)):
        if numbers[i] == numbers[j]:
            print(numbers[i], " is the duplicate value") 
            break