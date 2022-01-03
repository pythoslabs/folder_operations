# Created : 3 Jan 2022
# Reads a file and counts the number of lines  

#One line 
print(len([k for k in open("../data/classes.txt","r").read().split("\n") if len(k)>0]))

# Writting the same line as a function 
def count_lines(PATH)
  L_lines = open(PATH,"r").read().split("\n")
  L_lines = [k for k in L_lines if len(k)>0]
  return (len(L_lines))
