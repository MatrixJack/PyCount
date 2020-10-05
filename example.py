import sys
import os

sys.path.append(os.path.abspath('libaries'))

from comb import combination

stringExample = "coolPassword12"

#r"\d+" = numbers

combinationResult = combination(stringExample)

print("Combo Count: " + str(combinationResult.getCount()))
print("Combo Str Count: " + str(combinationResult.getStrCount()))
print("Str into Combo: " + str(combinationResult.getCount() / combinationResult.getStrCount()))