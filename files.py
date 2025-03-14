# friday march 14, 2025
# lecture 18: files, functions, & lists

# game plan
# [x] hello world! file and function
# [x] read_data() function: open, read, and prepare iClicker data variable
# [] eventually use in broader applications :-)

def read_data(filename):
  """Transforms iClicker csv into an iClicker nested list."""
  
  # Open
  file = open(filename, "r")

  # Read
  lines = file.readlines()

  # Close
  file.close() 

  # print(lines) # everything
  # print(type(lines)) # it's a list!
  # print(lines[0]) # header
  # print(lines[1]) # student data (one student per line)

  # Prepare 
  iClicker = [] 

  # Convert the lines in the file into sublists
  for line in lines[1:]: 
    # Strip function 
    # Remove the newline character from the end
    line = line.strip()

    # Split function
    # Utilizes structure of comma separated value file 
    line = line.split(',')
    # print(line)

    slist = [] 
    slist.append(line[0]) # name string as is
    scores = line[1:]
    # Discuss
    for entry in scores:
      # TODO: Convert everything after the name string into integers (# if statement)
      # TODO: Convert empty strings into 0s (# replace, use int())
      if entry == "" or entry == "0":
        slist.append(0)
      elif entry == "1":
        slist.append(1)
      else:
        print("not a 0, 1, or empty string - pls troubleshoot", entry)
      
    iClicker.append(slist) # Build up the iClicker nested list

  return iClicker

iClicker_22fa = read_data("22fa_clicker.csv")
print(iClicker_22fa)