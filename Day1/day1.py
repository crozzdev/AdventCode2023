"""The newly-improved calibration document consists of lines of text; each line originally contained a specific calibration value that the Elves now need to recover. On each line, the calibration value can be found by combining the first digit and the last digit (in that order) to form a single two-digit number.

For example:

1abc2
pqr3stu8vwx
a1b2c3d4e5f
treb7uchet
In this example, the calibration values of these four lines are 12, 38, 15, and 77. Adding these together produces 142.

Consider your entire calibration document. What is the sum of all of the calibration values?"""

def find_first(text_list):
    first = ""
    if text_list == "":
        return ""
    for char in text_list:
        if char.isdigit():
            first = str(char)
            break
    return first

def find_last(text_list):
    last= ""
    if text_list == "":
        return ""
    reversed = text_list[::-1]
    for char in reversed:
        if char.isdigit():
            last = str(char)
            break
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
           