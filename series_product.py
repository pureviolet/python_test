"""Complete this program to find the greatest produdct of five consecutive
digits in the list"""

import operator

in_file = open('array.txt')
lines = in_file.readlines()
in_file.close()

# assumes that consective digits can span lines
digits = "".join([ line.strip() for line in lines ])  # remove new lines
numbers = [ int(x) for x in digits ]  # place all digits in one list

greatest_product = 0  # the maximum product found so far
index_of_greatest = 0
i = 0
end = len(numbers)-5  # starting position of the last string
while i <= end:
    five_numbers = numbers[i:i+5]
    if five_numbers[-1] == 0:  # skip most of the zero products
        i += 5
        continue
    current_product = reduce(operator.mul, five_numbers)  # product
    if current_product > greatest_product:
        greatest_product = current_product
        index_of_greatest = i
    i += 1

print "greatest product:", greatest_product
print "calculated from digits at index:", index_of_greatest
print "these are the digits:", "".join([ str(x) for x in numbers[index_of_greatest:index_of_greatest+5]])
