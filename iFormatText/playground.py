from iFormatText import iFormatText


if (__name__ == '__main__'):
    iformatTextPepe = iFormatText("Example")
    iformatTextPepe.bond().print()

    iformatTextPepe.reset().colorize('black').background('cyan').print()
    text = iFormatText("This text is an example of rainblow.")
    rainblow = text.rainBlow()
    text.print()
    rainblow.print()