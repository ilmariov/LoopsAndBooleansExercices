from graphics import *

def cartesian_plane(width, height):
    win = GraphWin('Regression Line', width, height)
    win.setCoords(-width/2, -height/2, width/2, height/2)
    x_axis = Line(Point(-width/2, 0), Point(width/2, 0))
    x_axis.setOutline('blue')
    x_axis.setWidth(2)
    x_axis.draw(win)
    y_axis = Line(Point(0, -height/2), Point(0, height*(18/40)))
    y_axis.setOutline('blue')
    y_axis.setWidth(2)
    y_axis.draw(win)
    Text(Point(0, height*(19/40)), 'Specify the data points by clicking on them').draw(win)
    return win

def button(win, width, height):
    p1 = Point(-width*(9/20), -height*(9/20))
    p2 = Point(-width*(6/20), -height*(8/20))
    rect = Rectangle(p1, p2)
    rect.setOutline('red')
    rect.setWidth(2)
    rect.draw(win)
    button = Text(Point(-width*(15/40), -height*(17/40)), 'DONE')
    button.setTextColor('red')
    button.setStyle('bold')
    button.setSize(14)
    button.draw(win)
    return rect, button

def getLimits(width, height):
    x1 = -width*(9/20)
    y1 = -height*(9/20)
    x2 = -width*(6/20)
    y2 = -height*(8/20)
    return (x1, y1, x2, y2)

def draw_line(win, width, height, x_avg, y_avg, m):
    xLeftLimit = int((-width*19)//40)
    xRightLimit = int((width*19)//40)
    for i in range (xLeftLimit, xRightLimit, 3):
            j = y_avg + (m * (i - x_avg))
            if j > -height*(8/20):
                line_dots = Circle(Point(i, j), 1)
                line_dots.setOutline('green')
                line_dots.draw(win)
                
def main():
    width = 800 #float(input('Enter window width: '))
    height = 500 #float(input('Enter window height: '))
    win = cartesian_plane(width, height)
    button(win, width, height)    
    x_left, y_botton, x_right, y_top = getLimits(width, height) #limits for the exit button
    click = win.getMouse()
    x = click.getX()
    y = click.getY()
    total_x = total_y = sum_num = sum_den = n = 0    

    while ((x_left < x < x_right) and (y_botton < y < y_top)) == False:
        dot = Circle(Point(x, y), 1)
        dot.draw(win)

        n = n + 1
        total_x = total_x + x
        total_y = total_y + y
        x_avg = total_x / n
        y_avg = total_y / n

        pro_num = (x * y)
        pro_den = (x * x)
        sum_num = sum_num + pro_num
        sum_den = sum_den + pro_den

        click = win.getMouse()
        x = click.getX()
        y = click.getY()

    num = sum_num - (n * x_avg * y_avg)
    den =  sum_den - (n * x_avg * x_avg)
    if den != 0:
        m = num / den
        draw_line(win, width, height, x_avg, y_avg, m)
    else:
        draw_line(win, width, height, x_avg, y_avg, 0)
    
    win.getMouse()
    win.close()

main()