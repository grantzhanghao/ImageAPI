from matplotlib import pylab
from pylab import plt,xlabel,ylabel,grid
from PIL import Image
import matplotlib.pyplot as plt 

def draw_mock_graph():
    '''draw the toe energy per meter graph.
    '''
    plt.plot([1, 2, 3, 4, 5], [1, 4, 9, 16, 18], 'ro')
    plt.axis([0, 6, 0, 20 ])    
    canvas = pylab.get_current_fig_manager().canvas
    canvas.draw()
    pil_image = Image.frombytes("RGB", canvas.get_width_height(), canvas.tostring_rgb())
    pylab.close()
    return pil_image
