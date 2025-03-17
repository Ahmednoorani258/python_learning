
def palindromecheck(word):
    return word == word[::-1]

print(palindromecheck("racecar"))
print(palindromecheck("121"))
    
def double_sum_checker(arr,target):
    for i in range(len(arr)):
        for j in range(i+1,len(arr)):
            if arr[i]+arr[j] == target:
                return f"{arr[i]} + {arr[j]} = {target}"
    return False

print(double_sum_checker([1,2,3,4,5],9))
print(double_sum_checker([1,2,5,4,5],9))
    