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

    window = GraphWin('Grayscaling', widthPic, heightPic+44)
    placedPic.draw(window)
    win.close()

    return window, widthPic, heightPic, placedPic, filename

def main():
    win, widthPic, heightPic, picture, filename = openPicture()
    steps = Text(Point(widthPic/2, heightPic + 22), 'Click to grayscale')
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
    steps = Text(Point(widthPic/2, heightPic + 11), 'Enter "y" to save the image or just click to exit')
    steps.draw(win)
    save = Entry(Point(widthPic/2, heightPic + 33), 3)
    save.draw(win)
    win.getMouse()
    answer = save.getText()

    while answer != 'y' and answer != 'Y' and answer != '':
        steps.undraw()
        steps = Text(Point(widthPic/2, heightPic + 11), 'Invalid entry. Enter "y" to save or click to exit').draw(win)
        save.undraw()
        save.setText('')
        save.draw(win)
        win.getMouse()
        answer = save.getText()
    
    if answer == '':
        win.close()
    else:
        picture.save('(grayscaled) {}'.format(filename))
        steps.undraw()
        save.undraw()
        steps = Text(Point(widthPic/2, heightPic + 22), 'Image saved, click again to exit').draw(win)
        win.getMouse()
        win.close()


main()