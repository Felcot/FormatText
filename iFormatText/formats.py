class formats():
    def __init__(self):
        self.formats = {
            'reset' : "\x1b[10m",
            'bond' : "\x1b[11m",
            'normal' : "\x1b[12m",
            'italic' : "\x1b[13m",
            'underline' : "\x1b[14m",
            'colors' : {
                'black'   : '0',
                'red'     : '1',
                'green'   : '2',
                'yellow'  : '3',
                'blue'    : '4',
                'purple'  : '5',
                'cyan'    : '6',
                'white'   : '7'
            },
            'colorize'    : '3',
            'background'  : '4',
        }

    def get(self,string):
        return self.formats.get(string)

    def contains (self,style):
        return style in self.formats

    def containsColor(self,color):
        return color in self.formats.get('colors')
formats = formats()