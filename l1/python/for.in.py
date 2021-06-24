# countries = ["Denmark", "Finland", "Norway", "Sweden"]
# for country in countries:
#    print(country)

# for letter in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
#       if letter in "AEIOU":
#           print(letter, "is a vowel")
#       else:
#           print(letter, "is a consonant")
s = input ("enter an integer: ")
try:
    i = int(s)
    print("valid ineger entered:", i)
except ValueError as err:
    print(err)
