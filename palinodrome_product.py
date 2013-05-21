"""A palindromic number reads the same both ways. The largest palindrome made
from the product of two 2-digit numbers is 9009 = 91 99.Find the largest
palindrome made from the product of two 3-digit numbers."""

highest = 0  # highest palindrome product found so far
xa = xb = 0
for a in xrange(999, 99, -1):  # start with the highest products
    for b in range(a, 99, -1):  
        product = a * b
        if product <= highest:  # none of the other b's can be high enough
            break 
        digits = str(product)
        back = "".join(reversed(digits))  # reverse the digits
        if digits == back:
            highest = product  # we already tested that the product is higher
            xa = a
            xb = b
#            print a, b, digits
            break
print "The largest palindrome made from the product of two 3-digit numbers:"
print xa, xb, highest

