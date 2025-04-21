import picture

def circles(x, y, radius):
    '''
    draws a set of color-changing circles nested inside each other. Each run of circles() draws one circle with radius, cnetred at x and y
    '''

    # TODO base case
    if radius < 10:
      # draw filled circle at x, y
      pass
    
    # starter code for changing color and drawing filled circle at current values
    picture.set_fill_color(0, radius % 255, 0)
    print(radius % 255)
    picture.draw_filled_circle(x, y, radius)

    # TODO recursive call
    # draw filled circle at x, y
    circles(x, y, radius - 3)

def main():
  # set up a new canvas
  dim = 360
  picture.new_picture(dim, dim)

  # find center of canvas
  x_center = dim // 2
  y_center = dim // 2

  # outline color (same for all circles)
  picture.set_outline_color('green')

  # TODO: one test circle before we try recursion!
  picture.set_fill_color(0, 255, 0)
  picture.draw_filled_circle(x_center, y_center, dim // 3)

  # circles(x_center, y_center, dim // 3)

  # save picture (show in different tab of codespace)
  picture.save_picture("verygreen.png")

if __name__ == "__main__":
  main()