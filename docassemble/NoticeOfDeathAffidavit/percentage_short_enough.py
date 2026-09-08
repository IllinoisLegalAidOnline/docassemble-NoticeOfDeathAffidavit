def percentage_short_enough(share_number):
  percent_string = str(share_number)
  if len(percent_string) < 6:
    return True
  else:
    return False