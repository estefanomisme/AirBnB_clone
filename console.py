#!/usr/bin/python3
import cmd, sys
from models.engine.file_storage import FileStorage

dictclass = FileStorage.allclasses


class HBNBCommand(cmd.Cmd):
    prompt = '(hbnb) '

    def emptyline(self):
        """Does nothing
        """
        pass

    def do_create(self, line):
        """Creates a new instance of any allowed class

        Args:
            line: Must contain the name/names of some allowed class(es)
        """
        args = line.split()
        if len(args) == 0:
            print("** class name missing **")
        else:
            for a in args:
                if a in dictclass.keys():
                    obj = dictclass[a]()
                    obj.save()
                    print(obj.id)
                else:
                    print("** class doesn't exist **")
                    break

    def do_EOF(self, arg):
        """EOF command to exit the program
        """
        sys.exit(0)

    def do_quit(self, arg):
        """Quit command to exit the program
        """
        sys.exit(0)

if __name__ == '__main__':
    HBNBCommand().cmdloop()
