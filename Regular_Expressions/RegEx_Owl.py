import re

owlFood = "rat cat mat pat"

print(owlFood)
print()
regex = re.compile("[cr]at")

owlFood = regex.sub("owl", owlFood)
print(owlFood)
print()
