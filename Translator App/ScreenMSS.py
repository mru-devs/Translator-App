import mss

region = {
    "top": 200,
    "left": 300,
    "width": 400,
    "height": 200
}

with mss.mss() as sct:
    screenshot = sct.grab(region)

    mss.tools.to_png(screenshot.rgb, screenshot.size, output="region.png")


# Just testing so far