""" --- Part Two ---
Your calculation isn't quite right. It looks like some of the digits are actually spelled out with letters: one, two, three, four, five, six, seven, eight, and nine also count as valid "digits".

Equipped with this new information, you now need to find the real first and last digit on each line. For example:

two1nine
eightwothree
abcone2threexyz
xtwone3four
4nineeightseven2
zoneight234
7pqrstsixteen
In this example, the calibration values are 29, 83, 13, 24, 42, 14, and 76. Adding these together produces 281.

What is the sum of all of the calibration values?"""


NUMS_DICT = {
    "one": 1,
    "two": 2,
    "three": 3, 
    "four": 4,
    "five": 5,
    "six": 6,
    "seven": 7, 
    "eight": 8,
    "nine": 9
}

def detect_number(text_list: str) -> str:
    sub_word = ""
    for char in text_list:
        if char.isdigit():
            return ""
        sub_word += char
        if sub_word in NUMS_DICT.keys():
            return str(NUMS_DICT[sub_word])
    return ""

            
            

def find_first(text_list: str) -> str:
    first = ""
    if text_list == "":
        return ""
    
    for i in range(len(text_list)):
        if text_list[i].isdigit():
            return str(text_list[i])
        else:
            first = detect_number(text_list[i:])
            if first.isdigit():
                return first
            
    return ""

def find_last(text_list):
    last = ""
    for pos in range(len(text_list)):
        digit = find_first(text_list[pos:])
        if digit != "":
            last = digit
    return last
    

def find_sum(input):
    with open(input) as f:
        lines = f.readlines()
        sum = 0
        for line in lines:
            first = find_first(line)
            last = find_last(line)
            num = first + last
            sum += int(num)
    return sum
            
if __name__ == "__main__":
    print(find_sum("input.txt"))