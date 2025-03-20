iClicker = {
  'Alex': [0, 0, 1, 1, 1, 1], # attended 2 sessions ago
  'Erin': [1, 1, 1, 0, 0], # attended 0 sessions ago
  'Mika': [0, 1, 1, 1, 1] # attended 1 session ago
 }

def most_recent(slist):
  """
  Given a student's list of iClicker data, return the index ('# sessions ago') of their most recent attendance.
  """

  # while loop approach
  # WORK IN PROGRESS
  value = 0
  index = 0
  while value == 0:
    value = slist[index]
    index += 1
  return 

  # for loop approach
  # WORK IN PROGRESS
  for name in slist:
    if ??? == 0:
      days += 1
    if ?? == 1:
      return days

  # pseudocode for reference
  # loop through indices
    # find 1 value
    # return current index


print(most_recent('Erin'))