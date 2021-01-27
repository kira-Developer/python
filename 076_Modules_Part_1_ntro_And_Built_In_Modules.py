# ---------------------------------
# -- Modules => Built In Modules --
# ---------------------------------
# [1] Module is A File Contain A Set Of Functions
# [2] You Can Import Module in Your App To Help You
# [3] You Can Import Multiple Modules
# [4] You Can Create Your Own Modules
# [5] Modules Saves Your Time
# --------------------------------------------------


# Import Main Module
import random

print(random)

print(f'print random folat number {random.random()}')

print('#' * 50)
# Show All Functions Inside Module

print(dir(random))

print('#' * 50)

# Import One Or Two Functions From Module
from random import randint , random

print(f'print random float {random()}')
print(f'print random ingteger {randint(100 , 900)}')
