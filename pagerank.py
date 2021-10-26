import numpy as np
def create_stochastic(adj_list):
  n = len(adj_list)
  matrix = np.zeros((n, n)) 
  for row, line in enumerate(adj_list):
    if len(line) > 0:
      for index in line:
        matrix[index][row] = 1/(len(line))
    else:
      for index in range(n):
        matrix[index][row] = 1/n
  return matrix

def pg(matriks, jml_brs, max_iter):
  iter = 0
  t = 1
  matriks = np.array(stochastic)

  matriks2 = ([0]*jml_brs)
  for i in range(jml_brs): 
      matriks2[i] = [1/jml_brs]*1
  print(matriks2)

  while iter < max_iter:
    print('\nIterasi ', iter)
    hasil = []
    matriks1 = matriks**t
    
    for i in range(len(matriks1)):
      baris = []
      for k in range(len(matriks2[0])):
        val = 0
        for j in range(len(matriks1[i])):
            val += matriks1[i][j] * matriks2[j][k]
        baris.append(val)
      hasil.append(baris)

    print("PR",iter, '=')
    for baris in hasil:
        print(baris)
    iter += 1
    t += 1 
  return baris
