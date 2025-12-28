programming_dictionary = {"Bug": "An error in a program that prevents the program from running as expected.",
                          "Function": "A piece of code that you can easily call over and over again."
}

#adding items into dictionary
programming_dictionary["NA_error"] = "non natural number"

#creating a empty dictionary
empty_dictionary ={}

#wiping an exisiting dictionary
#programming_dictionary={}

#edit an item in a dictionary
programming_dictionary["Bug"]="a moth in a computer"
print(programming_dictionary["Bug"])


# question=input("information key")
# retrieving a value from dictionary
# print(programming_dictionary[question])

#loop through a dictionary
for key in programming_dictionary:
    print(key)
    #print(programming_dictionary[key])