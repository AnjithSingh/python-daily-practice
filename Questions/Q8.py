A = {'1', '2', '3', '4', '5'}
B = {'4', '5', '6', '7', '8'}

print(A & B)  
union = (list(A | B))
union.sort()
print(union)



# Count vowels for given input  by user:

word = input("Word dalo: ").lower()
vowels = "aeiou"
count = 0

for char in word:
    if char in vowels:
        count += 1
    print(count)
        

# sqaure of resp

n = 5
squares = {}

for i in range(1, n+1):
    squares[i] = i**2

print(squares)


#frequency checker 

text = "data science is cool and python is cool for data"
words = text.split() # ['data', 'science', 'is', 'cool'...]

freq = {}

for w in words:
    if w in freq:
        freq[w] += 1
    else:
        freq[w] = 1

print(freq)
