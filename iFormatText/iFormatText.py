# Author : Felcot - Felipe Costa Tebar
# Version 0.0.1

from formats import formats;

# This class help with style format of strings
class iFormatText():

    def __init__(self, string):
        self.unStyleString =  string + formats.get('reset');
        self.string = string + formats.get('reset');
    # reset function delete all styles of the text formated
    def reset(self):
        self.string = self.unStyleString;
        return self;

    # apply function insert a style in native python for example \x1b[1;...m
    def apply(self, style):
        self.string = style + self.string;
        return self
    # bond function apply bond style
    def bond(self):
        return self.stylize('bond')

    # italic function apply italic style
    def italic(self):
        return self.stylize('italic')

    # stylize function helps to apply style of list (reset,bond,italic,underline);
    def stylize(self,style):
        if formats.contains(style):
            return self.apply(formats.get(style));
        raise Exception("Stylize error");
    # colorize function helps to apply a text color style of list (black,red,green,yellow,blue,purple,cyan,white)
    def colorize(self,color):
        if formats.containsColor(color):
            return self.color(int(str(formats.get('colorize')) + str(formats.get('colors').get(color))));
        raise Exception("This color style don't exist");

    # background function helps to apply a background color style of list (black,red,green,yellow,blue,purple,cyan,white)
    def background (self,color):
        if formats.containsColor(color):
            return self.color(int(str(formats.get('background')) + str(formats.get('colors').get(color))));
        raise Exception("This color style don't exist");

    # color function helps to apply a background and text color style, but you need to use a native python numbers.
    def color(self, color):
        if isinstance(color,int):
            return self.apply("\x1b[1;" + str(color) + "m");
        return self.colorize(color);

    # rainBlow return a new object with the rainblow style.
    def rainBlow(self):
        maxString = len(self.string) - 6 ;
        max = int(maxString/6);
        cont = 0;
        color = 31;
        newString = "";
        contString = 0;

        for character in self.string:

            if(cont == 0):
                newString = formats.get('reset') + newString + "\x1b[1;" + str(color) + "m";
                color = color + 1;

            newString = newString + character;
            if(cont == max):
                cont = - 1;
            cont= cont + 1;
            contString = contString + 1;
            if(maxString == contString):
                break;

        return iFormatText(newString);

    # This function return value of iFormatText object
    def toString(self):
        return self.string;

    # Print function simplify the printing screen of an object instance of iFormatText
    def print(self):
        print(self.toString());

if (__name__ == '__main__'):  # Ejemplo
    iformatTextPepe = iFormatText("Felcot");
    iformatTextPepe.bond().print();

    iformatTextPepe.reset().colorize('black').background('cyan').print();
    text = iFormatText("This text is an example of rainblow.");
    rainblow = text.rainBlow();
    text.print();
    rainblow.print();



