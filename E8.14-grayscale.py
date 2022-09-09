from graphics import *

def openPicture():
    win = GraphWin('Grayscaling', 400, 100)
    Text(Point(200,35), 'Enter image filename, then click:').draw(win)
    picName = Entry(Point(200,75), 10)
    picName.setText('.PPM')
    picName.draw(win)
    win.getMouse()
    filename = picName.getText()
    picture = Image(Point(200, 50), filename)
    heightPic = picture.getHeight()
    widthPic = picture.getWidth()
    placedPic = Image(Point(widthPic/2, heightPic/2), filename)

    window = GraphWin('Grayscaling', widthPic, heightPic+30)
    placedPic.draw(window)
    win.close()

    return window, widthPic, heightPic, placedPic, filename

def main():
    win, widthPic, heightPic, picture, filename = openPicture()
    steps = Text(Point(widthPic/2, heightPic + 15), 'Click to grayscale')
    steps.draw(win)
    win.getMouse()

    for i in range(0, heightPic):
        for j in range(0, widthPic):
            #print(j, i)
            r, g, b = picture.getPixel(j, i)
            brightness = int(round(0.299*r + 0.587*g + 0.114*b))
            picture.setPixel(j, i, color_rgb(brightness, brightness, brightness))
        picture.undraw()
        picture.draw(win)
    
    steps.undraw()
    steps = Text(Point(widthPic/2, heightPic + 15), 'Click to save to a file image')
    steps.draw(win)
    win.getMouse()

    picture.save('(grayscaled) {}'.format(filename))
    steps.undraw()
    steps = Text(Point(widthPic/2, heightPic + 15), 'Click to exit').draw(win)
    win.getMouse()
    win.close()

main()