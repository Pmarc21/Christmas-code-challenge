def draw_gift(size, symbol):
  gift_array = []
  if size < 2:
    return ''
  else:
    for i in range(size):
        if i == 0 or i == size-1:
            gift_array.append(size*symbol)
        else:
           gift_array.append(symbol + ' '*size-2 + symbol)
    return "\n".join(str(x) for x in gift_array)

print(draw_gift(3, "#"))