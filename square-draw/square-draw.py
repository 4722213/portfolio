#coding:utf-8

def square(x, y, mark):
  line =  []
  for i in range(x):
    n = []
    for j in range(y):
      if i == 0 or i == x -1:
        n.append(mark)
      else:
        if j == 0 or j == y -1:
          n.append(mark)
        else:
          n.append(" ")
    line.append(n)
  
  return line

x = int( input("縦: ") )
y = int( input("横: ") )
mark = str( input("mark: ") )

draw = square(x, y, mark)

for i in range( len(draw) ):
  for j in range( len(draw[i]) ):
    print(draw[i][j], end = "")
  print("")
  
