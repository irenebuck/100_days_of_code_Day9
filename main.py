# Author : Irene Buck
# Date: July 28, 2023
# 100 Days of Code - Dictionaries


programming_dictionary = {"Bug": "An error in a program that prevents the program from running as expected.",
                          "Function": "A piece of code that you can easily call over and over again."}

programming_dictionary["Loop"] = "The action of doing something over and over again."
print(programming_dictionary)

print(programming_dictionary["Bug"])

empty_dict = {}
print(empty_dict)

programming_dictionary["Bug"] = "Spider"
print(programming_dictionary)

#Looping through a dictionary
for key in programming_dictionary:
    print(key)
    print(programming_dictionary[key])  # prints related value



# Exercist 1 - Create a dictionary and update the score to a ranking
student_scores = {
  "Harry": 81,
  "Ron": 78,
  "Hermione": 99,
  "Draco": 74,
  "Neville": 62,
}
student_grades = {}

for key in student_scores:
    if student_scores[key] > 90:
        student_grades[key] = "Outstanding"
    elif 91 > student_scores[key] > 80:
        student_grades[key] = "Exceeds Expectations"
    elif 81 > student_scores[key] > 70:
        student_grades[key] = "Acceptable"
    else:
        student_grades[key] = "Fail"

print(student_grades)


# Nesting basics
cities_I_visited = {
    "California": ["San Diego", "LA", "San Francisco", "Santa Barbara"],
    "Florida": ["Orlando", "Tampa", "Clearwater", "Port Canaveral"],
    "NY": ["NYC", "Brewster", "North Salem"]
}
travel_log = {
    "France": {"cities_visited": ["Paris", "Lille", "Dijon"], "capital": "Paris"},
    "Germany": {"cities_visited": ["Berlin", "Hamburg", "Munich"], "capital": "Berlin"}
}

travel_log_dicts = [
    {
        "country": "France",
        "cities_visited": ["Paris", "Lille", "Dijon"],
        "capital": "Paris"
    },
    {
        "country": "Germany",
        "cities_visited": ["Berlin", "Hamburg", "Munich"],
        "capital": "Berlin"
    }
]

order = {
    "starter": {1: "Salad", 2: "Soup"},
    "main": {1: ["Burger", "Fries"], 2: ["Steak"]},
    "dessert": {1: ["Ice Cream"], 2: []},
}
print(order["main"][2][0])   # prints Steak



# Exercise 2 - Travel log
travel_log = [
{
  "country": "France",
  "visits": 12,
  "cities": ["Paris", "Lille", "Dijon"]
},
{
  "country": "Germany",
  "visits": 5,
  "cities": ["Berlin", "Hamburg", "Stuttgart"]
},
]


def add_new_country(country, num_visits, list_of_cities):
    travel_log.append({"country": country, "visits": num_visits, "cities": list_of_cities})


add_new_country("Russia", 2, ["Moscow", "Saint Petersburg"])
print(travel_log)