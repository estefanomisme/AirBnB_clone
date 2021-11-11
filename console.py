#!/usr/bin/python3
import cmd, sys
from models.engine.file_storage import FileStorage

dictclass = FileStorage.allclasses


def no_quotes(string):
    if (string[0] == '\"' or string[0] == '\''):
        return string[1:-1]
    else:
        return string

class HBNBCommand(cmd.Cmd):
    prompt = '(hbnb) '

    def emptyline(self):
        """Does nothing
        """
        pass

    def do_create(self, line):
        """Creates a new instance of any allowed class
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

    def do_show(self, line):
        """Prints the string representation of an instance of a class
        """
        args = line.split()
        allobjs = FileStorage()
        if len(args) == 0:
            print("** class name missing **")
        elif args[0] not in dictclass.keys():
            print("** class doesn't exist **")
        elif len(args) == 1:
            print("** instance id missing **")
        elif "{}.{}".format(args[0], args[1]) not in allobjs.all().keys():
            print("** no instance found **")
        else:
            obj = allobjs.all()["{}.{}".format(args[0], args[1])]
            print(obj)

    def do_all(self, line):
        """Prints all string representation of all instances based or
        not on the class name
        """
        args = line.split()
        allobjs = FileStorage()
        listobjs = []
        if len(args) == 0:
            for v in allobjs.all().values():
                listobjs.append(str(v))
            print(listobjs)
        elif args[0] not in dictclass.keys():
            print("** class doesn't exist **")
        else:
            for k, v in allobjs.all().items():
                clid = k.split('.')
                if clid[0] == args[0]:
                    listobjs.append(str(v))
            print(listobjs)

    def do_destroy(self, line):
        """Deletes an instance based on the class name and id
        """
        args = line.split()
        allobjs = FileStorage()
        if len(args) == 0:
            print("** class name missing **")
        elif args[0] not in dictclass.keys():
            print("** class doesn't exist **")
        elif len(args) == 1:
            print("** instance id missing **")
        elif "{}.{}".format(args[0], args[1]) not in allobjs.all().keys():
            print("** no instance found **")
        else:
            obj = allobjs.all()["{}.{}".format(args[0], args[1])]
            del(obj)
            """deletes the instance"""
            del allobjs.all()["{}.{}".format(args[0], args[1])]
            """deletes the item in the main dictionary"""
            allobjs.save()

    def do_update(self, line):
        """Updates an instance based on the class name and id by adding
        or updating attribute
        """
        args = line.split()
        allobjs = FileStorage()
        if len(args) == 0:
            print("** class name missing **")
        elif args[0] not in dictclass.keys():
            print("** class doesn't exist **")
        elif len(args) == 1:
            print("** instance id missing **")
        elif "{}.{}".format(args[0], args[1]) not in allobjs.all().keys():
            print("** no instance found **")
        elif len(args) == 2:
            print("** attribute name missing **")
        elif len(args) == 3:
            print("** value missing **")
        else:
            objU = allobjs.all()["{}.{}".format(args[0], args[1])]
            args[3] = no_quotes(args[3])
            q1 = (args[2] != 'id')
            q2 = (args[2] != 'created_at')
            q3 = (args[2] != 'updated_at')
            if (q1 and q2 and q3):
                if hasattr(objU, args[2]):
                    t = type(getattr(objU, args[2]))
                    setattr(objU, args[2], t(args[3]))
                else:
                    setattr(objU, args[2], args[3])
                objU.save()
            else:
                print("** this attribute can't be updated **")


    def do_EOF(self, line):
        """EOF command to exit the program
        """
        sys.exit(0)

    def do_quit(self, line):
        """Quit command to exit the program
        """
        sys.exit(0)

if __name__ == '__main__':
    HBNBCommand().cmdloop()