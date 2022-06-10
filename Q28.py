def test(dict, val):
  return list(key for key, value in dict.items() if value == val)

students = {
  'Theodore': 19,
  'Roxanne': 20,
  'Mathew': 21,
  'Betty': 20
}

print("\nOriginal dictionary elements:")
print(students)
print("\nFind all keys in the said dictionary that have the specified value:")
print(test(students, 20))