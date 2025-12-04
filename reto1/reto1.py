def filter_gifts(gifts):
  gifts_filtered = [gift for gift in gifts if '#' not in gift]
  return gifts_filtered