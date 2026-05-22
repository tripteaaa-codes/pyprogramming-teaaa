s = input("enter the string: ")
count = 0
# vowels = ['a', 'e', 'i', 'o', 'u','A', 'E', 'I', 'O', 'U']

for ch in s.lower():
    if ch.isalpha() and ch not in 'aeiou':
        count += 1
print("num of vowels:", count)