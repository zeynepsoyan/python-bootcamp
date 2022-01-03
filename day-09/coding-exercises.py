# Grading Program

student_scores = {
  "Harry": 81,
  "Ron": 78,
  "Hermione": 99, 
  "Draco": 74,
  "Neville": 62,
}

student_grades = {}
for key in student_scores:
    score = student_scores[key]
    grade = ""

    if score > 90:
        grade = "Outstanding"
    elif score > 80:
        grade = "Exceeds Expectations"
    elif score > 70:
        grade = "Acceptable"
    else:
        grade = "Fail"

    student_grades[key] = grade

print(student_grades)

# Dictionary in List

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

def add_new_country(country, visits, cities):
    new_log = {}
    new_log["country"] = country
    new_log["visits"] = visits
    new_log["cities"] = cities
    travel_log.append(new_log)


add_new_country("Russia", 2, ["Moscow", "Saint Petersburg"])
print(travel_log)