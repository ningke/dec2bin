#
# Convert a decimal number (whole and fraction) to its binary representation.
#

##
# Algorithm:
# A decimal number is a number represented as multiples of 10s. So for example 53.72 is
# exponent of 10:        1    0   -1   -2
# multiples:            10    1   .1  .01
#                        5    3.   7    2
#
# Binary number is the same thing except it uses base 2: So a number 3.375:
# 3.375 = (2 + 1 + 1/8 + 1/4)
# exponent of 2:         1    0   -1   -2   -3
# multiples:             2    1  1/2  1/4  1/8
#                        1    1.   0    1    1
#
# So to convert a decimal number, we do it in two steps:
# 1) Convert left of decimal point (whole part):
#    We keep dividing it by 2 and record the remainder, this is equivalent to right
#    shifting on place and record the parity of bit 0.
#    So:
#      exponent              number        result    remainder   output
#             0               3 / 2    =        1           1         1 
#             1               1 / 2    =        0           1        11
#
# 2) Convert right of decimal point (fraction part):
#    We keep multiply by 2 and record the overflow (the digit to the left of the decimal
#    point).
#    Remember that any rational number can be converted into a floating point
#    representation. But in some case the representation has repeats. So 1 / 3 is
#    0.33333333...... Similarly a binary number can be the same thing:
#    3 / 10 (0.3) is 0.1001 1001 1001 ......
#    Our algorithm needs to detect that we are converting the same number and note
#    that the digits are repeating and stop.
#

def dec2bin(dec):
    ''' Convert a decimal number ''dec'' as a string to its binary form. '''
    if len(dec) == 0:
        return ""
    # find the decimal point
    try:
        pos = dec.index(".")
        left = dec[0:pos]
        right = dec[pos+1:len(dec)]
        return dec2bin_left(left) + "." + dec2bin_right(right)
    except ValueError:
        return dec2bin_left(dec)

def dec2bin_left(dec):
    ''' Left of the point. Just keep shifting right. '''
    if len(dec) == 0:
        return "0"
    res = ""
    dnum = int(dec)
    if dnum == 0:
        return "0"
    while dnum > 0:
        res = str(dnum & 1) + res
        dnum >>= 1
    return res

def dec2bin_right(dec):
    ''' Right of the point. Keep doubling. '''
    _memoized = {}
    length = len(dec)
    if length == 0:
        return "0"
    return _dec2bin_right(dec, "", _memoized)

def _dec2bin_right(dec, res, memoized):
    ''' Memoizes the input so when we see a repeat we can stop. '''
    #print "('%s' '%s' %s)" % (dec, res, memoized)
    order = len(dec)
    if order == 0 or int(dec) == 0:
        return res
    if dec in memoized:
        # Repeat, Append the repeated part with a space and add "..." to the end.
        pos = memoized[dec]
        return res + " " + res[pos:] + "..."
    memoized[dec] = len(res)
    dnum = int(dec)
    double = dnum * 2
    # Must be careful here: We use the string length as order so we have to add some
    # leading zero if 'double' is shorter than 'order'.
    dec = str(double)
    if len(dec) > order:
        # overflow
        digit = '1'
        dec = dec[1:]
    else:
        digit = '0'
        # add leading zeros if necessary
        fmt = "%%0%dd" % order
        dec = fmt % double
    return _dec2bin_right(dec, res + digit, memoized)


def tests():
    whole_numbers = '0 0000 01 1 10 2 3 4 5 16 64 127 200 300 167929 83648237389827329'
    print "Whole numbers:"
    for i in whole_numbers.split():
        print "%s ==> %s" % (i, dec2bin(i))

    print "\nFloating point numbers:"
    floating_points = '0.02 0.1 0.2 0.3 0.125 0.375 1.5 3.875 13.73'
    for f in floating_points.split():
        print "%s ==> %s" % (f, dec2bin(f))

if __name__ == "__main__":
    import sys
    dec = sys.stdin.readline().rstrip()
    print dec2bin(dec)
