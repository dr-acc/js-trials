"""Python functions for JavaScript Trials 1."""


def output_all_items(items):
    for item in items:
        print(item)


def get_all_evens(nums):

    even_nums = []
    
    for num in nums:
        if num % 2 == 0:
            even_nums.append(num)
    
    return even_nums
        


def get_odd_indices(items):
    
    result = []    
    
    for idx in range(len(items)):
        if idx % 2 != 0:
            result.append(items[idx])    

    return result


def get_range(start, stop):

    numbers = []

    for item in range(start, stop):
        numbers.append(item)

        # print(f'{i}. {item}')
    return item


def censor_vowels(word):
    
    chars = []

    for letter in word:
        if letter in 'aeiou':          
            chars.append('*')
        else:
            chars.append(letter)

    return chars

def snake_to_camel(string):
    """ Given a string in snake case, return a string in upper camel case. 
        Ex.:
        >>> snake_to_camel('hello_world');
        'HelloWorld'"""

    camel_case = []

    # new_word = string.split('_')

    # new_word = string.split(' ')

    for word in string:
        camel_case.append(f'{word[0].upper()}{word[1:]}')
    
    return ''.join(camel_case)



#     for (const word of string.split('_')) {
#     camelCase.push(`${word[0].toUpperCase()}${word.slice(1)}`);
#   }

#   return camelCase.join('');


def longest_word_length(words):
    pass  # TODO: replace this line with your code
    longest_word = len(word[0])

    for word in words:
        if longest_word < len(word):
            return len(longest_word)

def truncate(string):
    pass  # TODO: replace this line with your code


def has_balanced_parens(string):
    


def compress(string):
    pass  # TODO: replace this line with your code
