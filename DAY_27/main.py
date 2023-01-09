'''Day 27 of python'''
'''F strings in python'''

letter = "Mahee is awesome {1} but why {0}?"
country = "Bangalider desh"
name="faisal"


print(letter.format(name,country))


print(f"My name is {name} And I come from {country}")


price = 10.123445

shirt=f"The shirt costs {price:.1f}"

print(shirt)
