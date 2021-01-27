# ----------------------------------
# -- Built In Functions => Reduce --
# ----------------------------------
# [1] Reduce Take A Function + Iterator
# [2] Reduce Run A Function On FIrst and Second Element And Give Result
# [3] Then Run Function On Result And Third Element
# [4] Then Run Function On Rsult And Fourth Element And So On
# [5] Till One ELement is Left And This is The Result of The Reduce
# [6] The Function Can Be Pre-Defined Function or Lambda Function
# ---------------------------------------------------------------

from functools import reduce

def sumAll(num1 , num2) :
    return num1 + num2

numbers = [1 , 2 , 4 , 6 , 7 , 45]

# result = reduce(sumAll , numbers)
result  = reduce(lambda num1 , num2 : num1 + num2 , numbers)
print(result)