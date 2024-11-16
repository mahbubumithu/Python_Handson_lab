# Question 1: Create a empty dictionary.

my_dict = {}

# Question 2: Create a dictionary with key-value pairs for a person's name and age.

person = {"name":"Mithu", "age": 20}

# Question 3: Access the value associated with the key "age" in the person dictionary.

age = person["age"]

# Question 4: Check if a key exists in the person dictionary.

if "name" in person:
    print("Key 'name' exists.", person["name"])

# Question 5: Add a new key-value pair "city" with the value "New York" to the person dictionary.

person["city"] = "New York"

print(person)

# Question 6: Remove the key-value pair with the key "age" from the person dictionary.

del person["age"]

print(person)

# Question 7: Iterate through the keys in the person dictionary.

for key in person:
    print(key)
    
# Question 8: Iterate through the values in the person dictionary.

for value in person.values():
    print(value)

# Question 9: Iterate through both keys and values in the person dictionary.

for key, value in person.items():
    print(key, value)
    
# Question 10: Create a dictionary with default values using the dict.fromkeys() method.

defaults = dict.fromkeys(["name", "age", "city"], "Unknown")

# Question 11: Get the value associated with a key using the dict.get() method with a default value.

age = person.get("age", 0)

# Question 13: Merge two dictionaries.

dict1 = {"a": 1, "b": 2}
dict2 = {"b": 3, "c": 4}
merged_dict = {**dict1, **dict2}

print(merged_dict)

    