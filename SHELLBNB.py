import cmd, sys

class ShellBNB(cmd.Cmd):
    prompt = '(hbnb) '
    file = None

    def do_EOF(self, arg):
        """END OF FILE"""
        print('End of file. Program finished')

    def do_quit(self, arg):
        """Finishes the program"""
        print('Thank you for using HBNB')
        self.close()
        return True

    def precmd(self, line):
        """Needs to change"""
        line = line.lower()
        if self.file and 'playback' not in line:
            print(line, file=self.file)
        return line

    def close(self):
        """Needs to change"""
        if self.file:
            self.file.close()
            self.file = None

def parse(arg):
    """Needs to change"""
    'Convert a series of zero or more numbers to an argument tuple'
    return tuple(map(int, arg.split()))

if __name__ == '__main__':
    ShellBNB().cmdloop()
