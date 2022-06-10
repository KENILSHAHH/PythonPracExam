from collections import defaultdict
from math import floor
def test(lst, fn):
  d = defaultdict(list)
  for el in lst:
    d[fn(el)].append(el)
  return dict(d)
nums = [7,23, 3.2, 3.3, 8.4]
print("Original list & function:")
print(nums," Function name: floor:")
print("Group the elements of the said list based on the given function:")
print(test(nums, floor))
print("\n")
print("Original list & function:")
colors = ['Red', 'Green', 'Black', 'White', 'Pink']
print(colors," Function name: len:")
print("Group the elements of the said list based on the given function:")
print(test(colors, len))
