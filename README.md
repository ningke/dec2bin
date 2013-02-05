Convert a decimal number (whole and fraction) to its binary representation.
===========================================================================

# Algorithm:

A decimal number is a number represented as multiples of 10s. So for example 53.72 is
exponent of 10:        1    0   -1   -2
multiples:            10    1   .1  .01
                       5    3.   7    2

Binary number is the same thing except it uses base 2: So a number 3.375:
3.375 = (2 + 1 + 1/8 + 1/4)
exponent of 2:         1    0   -1   -2   -3
multiples:             2    1  1/2  1/4  1/8
                       1    1.   0    1    1

So to convert a decimal number, we do it in two steps:
1) Convert left of decimal point (whole part):
   We keep dividing it by 2 and record the remainder, this is equivalent to right
   shifting on place and record the parity of bit 0.
   So:
     exponent              number        result    remainder   output
            0               3 / 2    =        1           1         1 
            1               1 / 2    =        0           1        11

2) Convert right of decimal point (fraction part):
   We keep multiply by 2 and record the overflow (the digit to the left of the decimal
   point).
   Remember that any rational number can be converted into a floating point
   representation. But in some case the representation has repeats. So 1 / 3 is
   0.33333333...... Similarly a binary number can be the same thing:
   3 / 10 (0.3) is 0.1001 1001 1001 ......
   Our algorithm needs to detect that we are converting the same number and note
   that the digits are repeating and stop.

