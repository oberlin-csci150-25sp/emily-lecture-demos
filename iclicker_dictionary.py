iClicker = {
  'Alex': [0, 0, 1, 1, 1, 1], # attended 2 sessions ago
  'Erin': [1, 1, 1, 0, 0], # attended 0 sessions ago
  'Mika': [0, 1, 1, 1, 1] # attended 1 session ago
 }

def most_recent_while(slist):
  """
  Given a student's list of iClicker data, return the index ('# sessions ago') of their most recent attendance.
  """

  # while loop approach
  value = 0 # attendance value
  index = 0 # day corresponding to attendance value
  while value == 0: # keep going when there are absences (0s)
    value = slist[index]
    index += 1 # check the next day
  return index - 1 # undo the most recent index +=1

def most_recent_for(slist):
  """
  Given a student's list of iClicker data, return the index ('# sessions ago') of their most recent attendance.
  """

  # for loop approach
  for index in range(len(slist)):
    if slist[index] == 1:
      return index 

def most_recent(slist):
  return most_recent_for(slist)

def main():
  # print(most_recent_for(iClicker['Alex']))
  # print(most_recent_for(iClicker['Erin']))
  # print(most_recent_for(iClicker['Mika']))

  for stu in iClicker.keys():
    # sessions_ago = ??
    # CLICKER Q: How do I call our most_recent() function from elsewhere in the program? 
    # A. sessions_ago = iClicker.most_recent(stu)
    # B. sessions_ago = most_recent(stu)
    sessions_ago = most_recent(iClicker[stu])
    # D. sessions_ago = most_recent(iClicker, stu)
    # E. None of the above

    print(stu + " attended " + str(sessions_ago) + " sessions ago!")

main()

# Discarded Drafts
  # looping by element
  # days = 0
  # days_present = []
  # for attendance in slist:
  #   if attendance == 0:
  #     days += 1
  #   if attendance == 1:
  #     days += 1
  #     days_present.append(days)
  #     return days

  # pseudocode for reference
  # loop through indices
    # find 1 value
    # return current index