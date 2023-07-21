import matplotlib.pyplot as plt
import random
import numpy as np

#Setting graph
def game():
  xmin, xmax, ymin, ymax = -10, 10, -10, 10

  fig, ax = plt.subplots()
  plt.axis([xmin, xmax, ymin, ymax])
  plt.plot([xmin, xmax], [0,0], 'black')
  plt.plot([0,0], [ymin, ymax], 'black')
  ax.set_xticks(np.arange(xmin, xmax, 1))
  ax.set_yticks(np.arange(ymin, ymax, 1))
  ax.grid(True)

  points = 10 * (xmax - xmin)
  x = np.linspace(xmin, xmax, points)
  #Setting random coordinate points
  x1, y1, x2, y2 = [random.randint(xmin, xmax) for _ in range(0, 4)]

  m = (y2 - y1) / (x2 - x1) #slope
  b = y1 - m*x1 # y-intercept

  y = m * x + b
  plt.plot(x, y, 'r')
  plt.plot([x1, x2], [y1, y2], 'bo')

  print('Look at the graph below with the function y = mx + b and find the values of m and b')
  plt.show()
  print('y = mx + b')
  try:
    m_guess = input('m = ')
    if '/' in m_guess:
      a = m_guess.split('/')
      m_guess = float(a[0]) / float(a[1])
    else:
      m_guess = float(m_guess)
    b_guess = input('b = ')
    if '/' in b_guess:
      a = b_guess.split('/')
      b_guess = float(a[0]) / float(a[1])
    else:
      b_guess = float(b_guess)
    if m == m_guess and b == b_guess:
      print('You got it correct. Congratulations!!!')
    else:
      print('Your answer is incorrect! The right answer is')
  except:
    print('You entered an inappropriate value!')
  print(f'y = {m}x + {b}')
  print('Would you like to continue playing?')
  answer = input('(y/n)')
  return answer

print('Welcome to the game "Guess the linear function"')
answer = game()
while answer == 'y':
  answer = game()
