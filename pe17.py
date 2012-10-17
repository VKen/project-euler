

def num_to_word(num):
    if type(num) is not int:
        print "must be integer"
        return
    if num > 1000 or num <= 0:
        print "number must be between 1 and 1000"
        return
    # check length of numner
    num_len = len(str(num))
    #print num_len

    if num_len is 1:
        return _one_digit(num)

    elif num_len is 2:
        return _two_digit(num)

    elif num_len is 3:
        if num % 100:
            return _one_digit(num / 100) + \
                    "hundredand" + _two_digit(num % 100)
        else:
            return _one_digit(num / 100) + "hundred"
    elif num_len is 4:
        return "onethousand"


def _one_digit(num):
    num = int(num)
    if num is 1:
        return "one"
    elif num is 2:
        return "two"
    elif num is 3:
        return "three"
    elif num is 4:
        return "four"
    elif num is 5:
        return "five"
    elif num is 6:
        return "six"
    elif num is 7:
        return "seven"
    elif num is 8:
        return "eight"
    elif num is 9:
        return "nine"
    else:  # zero
        return ""


def _two_digit(num):

    num = int(num)
    if num is 0:
        return ""
    elif num is 10:
        return "ten"
    elif num is 11:
        return "eleven"
    elif num is 12:
        return "twelve"
    elif num is 13:
        return "thirteen"
    elif num is 14:
        return "fourteen"
    elif num is 15:
        return "fifteen"
    elif num is 16:
        return "sixteen"
    elif num is 17:
        return "seventeen"
    elif num is 18:
        return "eighteen"
    elif num is 19:
        return "nineteen"
    elif num is 20:
        return "twenty"
    elif num is 30:
        return "thirty"
    elif num is 40:
        return "forty"
    elif num is 50:
        return "fifty"
    elif num is 60:
        return "sixty"
    elif num is 70:
        return "seventy"
    elif num is 80:
        return "eighty"
    elif num is 90:
        return "ninety"
    elif num:
        return (_two_digit(num // 10 * 10) + _one_digit(num % 10))

count = 0
for x in range(1, 1001):
    count += len(num_to_word(x))

print count
#num_to_word(21)
#print num_to_word(212)
#print num_to_word(300)
