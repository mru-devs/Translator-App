import mss

filePathName = "region.png"
def ScreenShotter(x1,y1,x2,y2):
    width = x2 - x1
    height = y2 - y1

    region = {
        "left": x1,
        "top": y1,
        "width": width,
        "height": height
    }

    with mss.mss() as sct:
        screenshot = sct.grab(region)
        mss.tools.to_png(screenshot.rgb, screenshot.size, output=filePathName)


# Just testing so far