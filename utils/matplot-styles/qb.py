# QB Styles
import matplotlib.pyplot as plt
from qbstyles import mpl_style

def plot(dark):
  mpl_style(dark)
    
  plt.plot([1, 3, 9, 5, 2, 1, 1], marker='o')
  plt.plot([4, 5, 5, 7, 9, 8, 6], marker='o')

  plt.show()

plot(dark=True)