
    # Practice Challenge: Correct the errors!
first_name = "Alana"
last_name = "Da Silva"
age = 36
profession = "Software Developer"
years_experience = 5

greeting = "Hello my name is ", first_name, last_name

print(greeting) 
# Desired output: Hello my name is Alana Da Silva

print("I am {age} years old") 
# Desired output: I am 36 years old

print("I work as a profession.".format(profession))
# Desired output: I work as a Software Developer.

exp_string = "I have worked in the field for {} years."
print(exp_string.format(years_experience))
# Desired output: I have worked in the field for 5 years.

start_age = age - years_experience
print("I started in the field when I was {} years old.".format(start_age))
# Desired output: I started in the field when I was 31 years old.