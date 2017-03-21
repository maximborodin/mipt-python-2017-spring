import argparse
import sys


class MyError(Exception):
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)


class Formatter:
    def __init__(self):
        self.parser = None
        self.punctuation_marks = [",", ".", "?", "!", "-", ":", "'"]
        self.args = None
        self.input_text = None
        self.formatted_text = ''

    def parse_arguments(self):
        self.parser = argparse.ArgumentParser()
        self.parser.add_argument(
            '-i', '--input',
            type=str, default=sys.stdin,
            dest='input', required=True,
            help='Name of input file')
        self.parser.add_argument(
            '-o', '--output',
            type=str, default=sys.stdout,
            dest='output', required=True,
            help='Name of output file')
        self.parser.add_argument(
            '-l', '--line-length',
            type=int, default=80,
            dest='line_length', required=True,
            help='Max line length')
        self.parser.add_argument(
            '-p', '--paragraph-spaces',
            type=int, default=4,
            dest='paragraph_spaces', required=True,
            help='Length of spaces in new paragraph')
        self.args = self.parser.parse_args()

    def read_text(self):
        file = open(self.args.input, 'r')
        self.input_text = file.readlines()
        file.close()

    def format(self):
        length_of_current_line = 0
        current_word = ''
        new_paragraph = ' ' * self.args.paragraph_spaces
        was_space = False
        for line in self.input_text:
            if line == '\n':
                if new_paragraph == ' ' * self.args.paragraph_spaces \
                        and len(current_word) == 0:
                    new_paragraph = ''
                else:
                    new_paragraph, length_of_current_line, current_word = \
                        self.add_word(new_paragraph, length_of_current_line, current_word)
                    new_paragraph += '\n'
                self.formatted_text += new_paragraph
                new_paragraph = ' ' * self.args.paragraph_spaces
                continue
            for symbol in line:
                if symbol in self.punctuation_marks:
                    current_word += symbol
                elif symbol == ' ' or symbol == '\n':
                    was_space = True
                    continue
                else:
                    if was_space:
                        new_paragraph, length_of_current_line, current_word = \
                            self.add_word(new_paragraph, length_of_current_line, current_word)
                        current_word += symbol
                        was_space = False
                    else:
                        current_word += symbol
        new_paragraph, length_of_current_line, current_word = \
            self.add_word(new_paragraph, length_of_current_line, current_word)
        self.formatted_text += new_paragraph

    def add_word(self, paragraph, length_of_current_line, current_word):
        if len(current_word) > self.args.line_length:
            raise MyError("Too much symbols in word " + current_word)
        if len(current_word) + length_of_current_line > self.args.line_length:
            paragraph += '\n' + current_word
            length_of_current_line = len(current_word)
        else:
            paragraph += current_word
            length_of_current_line += len(current_word)
        current_word = ''
        if length_of_current_line < self.args.line_length:
            paragraph += ' '
            length_of_current_line += 1
        return [paragraph, length_of_current_line, current_word]

    def write_text(self):
        file = open(self.args.output, "w")
        file.write(self.formatted_text)
        file.close()

    def exec(self):
        self.parse_arguments()
        self.read_text()
        self.format()
        self.write_text()


def main():
    formatter = Formatter()
    formatter.exec()


if __name__ == "__main__":
    main()
