gifts_to_produce = [{ 'toy': 'car', 'quantity': 3 },
  { 'toy': 'doll', 'quantity': 1 },
  { 'toy': 'ball', 'quantity': 2 }]
def manufacture_gifts(gifts_to_produce):
  array_gifts = [gift["toy"] for gift in gifts_to_produce for _ in range(gift["quantity"])]
  return array_gifts

print(manufacture_gifts(gifts_to_produce))