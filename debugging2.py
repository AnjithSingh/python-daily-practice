# 1
def find_all_evens(numbers):
    even_list = []
    
    for n in numbers:
        if n % 2 == 0:
            even_list.append(n)
        return even_list  
            
    return even_list

my_nums = [1, 2, 3, 4, 5, 6, 8]
result = find_all_evens(my_nums)

print(result)

# 2

def analyze_data(text):
    text.lower()
    text.replace(".", "")
    text.replace(",", "")
    text.replace("!", "")
    
    words = text.split()
    

    unique_words = list(words) 
    unique_count = len(unique_words)
    

    freq_dict = {}
    
    for w in words:
        if w in freq_dict:
            freq_dict[w] += 1
        else:
            freq_dict[w] = 1
            
        return (len(words), unique_count, freq_dict)

raw_data = "Python is Great. python is easy."
print(analyze_data(raw_data))