# San Francisco Blockchain Scholarship Application Question:
# You are given a 6-sided die. You want to pick a random number from 1 to 10 where
# each number has an equal chance of getting picked.
# How do you do so with the single die? (Python code using a function roll6() is best.)

# roll6() -- random number generator from range 1-10 in base 6
# Tatiana Ensslin March 12, 2018

# complexity: worst run time o(N) since run time depends on N times to hit base case
# (although odds of this are 1/6 runs = 16.667%)

import random

# Global Variables
is_first_roll = True

def roll6():
    global is_first_roll
    global roll1

    # generate random number for first roll
    if is_first_roll:
        roll1 = random.randint(1, 6)
    else:
        roll1 = roll1

    # if odd
    if roll1 % 2 == 1:
        roll2 = random.randint(1, 6)

        # if re-roll required
        if roll2 == 6:
            is_first_roll = False
            value = roll6()
            return value

        else:
            return roll2

    # if even
    else:
        roll2 = random.randint(1, 6)

        # if re-roll required
        if roll2 == 6:
            is_first_roll = False
            value = roll6()
            return value

        else:
            even_switch_map = {
                1: 6,
                2: 7,
                3: 8,
                4: 9,
                5: 10,
            }
            return even_switch_map.get(roll2)

def main():

    value = roll6()

    print("Generated number from 1-10: " + str(value))
    return 0

if __name__ == "__main__":
    main()


# Woohoo -- this is a fun little problem. Okay. I'll walk you through my thought progress.
#  I want to pick a random number 1-10... a standard 6 sided die doesn't naturally map to 10
# -- so this must not be a standard die OR we can have unlimited amounts of rolls.
#  Now we can fill in the gaps as to how we get there. ...
# So, this problem is asking to make a random number generator from 1-10, in python,
# using only a single 6 sided die, or essentially only from 1-6... meaning base 6.
# The first thing I do is grab a pen and paper and I write out the base 6 decimals for the range 1-10..
#  We know that this is a uniform distribution because all of the numbers have an equal
# chance of being picked. Since there are ten numbers, each must have a 1/10 chance of being picked.
# Then I realize there could be a simpler version. So I start to think of an analogy to this problem
#  to make it simpler: make a random number generator using only a coin. Okay, so how can I turn
# a 6 sided die into a coin. Even and odd numbers. I then come up with the following algorithm:
# Roll the die -- 1st roll: If its an odd number {1,3,5} then we say it generates in the range {1-5}.
#  If its an even number {2,4,6} then we say it generates in the range {6-10}.
# Since there are 3/6 chances for each range to be picked at this point numbers still
# have uniform distribution.

# Roll the second die -- 2nd roll: Since we now have a 50/50 chance of picking either range,
# we can map the next roll to each half of the range depending on the 1-5 of the die roll.
#  This means that 6 cannot be mapped to each side, so if we roll 6, we roll until its not 6.
# This means our worst run time will be o(N).
#
# the mapping looks like this:
#
# roll one: {1,3,5}
# roll two:
# 1 = 1
# 2 = 2
# 3 = 3
# 4 = 4
# 5 = 5
#
# or
# roll one: {2,4,6}
# roll two:
# 1 = 6
# 2 = 7
# 3 = 8
# 4 = 9
# 5 = 10
