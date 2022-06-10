def test(d):
  return max(d, key = d.get), min(d, key = d.get)

students = {
  'Theodore': 19,
  'Roxanne': 22,
  'Mathew': 21,
  'Betty': 20
}
print("\nOriginal dictionary elements:")
print(students)
print("\nFinds the key of the maximum and minimum value of the said dictionary:")
print(test(students))
