from sty import Style, RgbFg
from sty import fg


class color:
    fg.BLACK = Style(RgbFg(0, 0, 0))
    fg.WHITE = Style(RgbFg(227, 220, 220))
    fg.RED = Style(RgbFg(255, 31, 31))
    fg.GREEN = Style(RgbFg(86, 212, 36))
    fg.ORANGE = Style(RgbFg(255, 112, 10))
    fg.BLUE = Style(RgbFg(0, 76, 255))
    fg.PURPLE = Style(RgbFg(31, 81, 255))
    fg.CYAN = Style(RgbFg(0, 187, 255))
    fg.LIGHT_GREY = Style(RgbFg(161, 161, 161))
    fg.DARK_GREY = Style(RgbFg(48, 48, 48))
    fg.LIGHT_RED = Style(RgbFg(255, 61, 61))
    fg.LIGHT_GREEN = Style(RgbFg(98, 255, 74))
    fg.YELLOW = Style(RgbFg(255, 204, 0))
    fg.LIGHT_BLUE = Style(RgbFg(0, 110, 255))
    fg.PINK = Style(RgbFg(255, 71, 2400))
    fg.LIGHT_CYAN = Style(RgbFg(71, 215, 255))
    fg.RESET = '\033[0m'
    BLACK = fg.BLACK
    WHITE = fg.WHITE
    RED = fg.RED
    GREEN = fg.GREEN
    ORANGE = fg.ORANGE
    BLUE = fg.BLUE
    CYAN = fg.CYAN
    LIGHT_GREY = fg.LIGHT_GREY
    DARK_GREY = fg.DARK_GREY
    LIGHT_RED = fg.LIGHT_RED
    LIGHT_GREEN = fg.LIGHT_GREEN
    YELLOW = fg.YELLOW
    LIGHT_BLUE = fg.LIGHT_BLUE
    PINK = fg.PINK
    LIGHT_CYAN = fg.LIGHT_CYAN
    RESET = '\033[0m'


def custom_color(r: int, g: int, b: int):
    fg.CUSTOM = Style(RgbFg(r, g, b))
    CUSTOM = fg.CUSTOM
    return CUSTOM


class prefix:
    INFO = color.DARK_GREY + '[' + color.LIGHT_BLUE + '!' + color.DARK_GREY + '] ' + color.WHITE
    INFO_TWO = color.DARK_GREY + '[' + color.LIGHT_CYAN + '-' + color.DARK_GREY + '] ' + color.WHITE
    FAILED = color.DARK_GREY + '[' + color.RED + '!' + color.DARK_GREY + '] ' + color.WHITE
    ALIVE = color.DARK_GREY + '[' + color.GREEN + '-' + color.DARK_GREY + '] ' + color.WHITE
    DEAD = color.DARK_GREY + '[' + color.RED + '-' + color.DARK_GREY + '] ' + color.WHITE


def banner():
    print(color.BLUE + '____ _    _ ___ ____    ____ ____ ____ ____ ___  ____ ____ ' + color.RESET)
    print(color.PINK + '|___ |    |  |  |___    [__  |    |__/ |__| |__] |___ |__/ ' + color.RESET)
    print(color.BLUE + '|___ |___ |  |  |___    ___] |___ |  \ |  | |    |___ |  \ ' + color.RESET)
    print()
    print()
