# mplcyberpunk Styles
import matplotlib.pyplot as plt
import mplcyberpunk

def plot_glow():
  plt.style.use("cyberpunk")
    
  plt.plot([1, 3, 9, 5, 2, 1, 1], marker='o')
  plt.plot([4, 5, 5, 7, 9, 8, 6], marker='o')

  mplcyberpunk.add_glow_effects()
  plt.show()


def plot_lines_glow():
  plt.style.use("cyberpunk")
    
  plt.plot([1, 3, 9, 5, 2, 1, 1], marker='o')
  plt.plot([4, 5, 5, 7, 9, 8, 6], marker='o')

  mplcyberpunk.make_lines_glow()
  plt.show()


def plot_underglow():
  plt.style.use("cyberpunk")
    
  plt.plot([1, 3, 9, 5, 2, 1, 1], marker='o')
  plt.plot([4, 5, 5, 7, 9, 8, 6], marker='o')

  mplcyberpunk.add_underglow()
  plt.show()


plot_glow()
plot_lines_glow()
plot_underglow()
