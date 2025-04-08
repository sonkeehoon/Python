'''
A Python module for drawing simple graphics in the CLI
'''
def draw_rectangle(width, height):
    '''
    This program draws a square in the terminal window.
    
    `width` : the horizontal length of the rectangle
    
    `height` : the vertical length of the rectangle
    
    '''
    print("\1"+"\6"*width + "\2")
    for _ in range(height): 
        print("\5"+" "*width + "\5")
    print("\3"+"\6"*width + "\4")

if __name__ == '__main__':
    print('draw_rectangle')
    draw_rectangle()
    