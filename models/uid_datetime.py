#!/usr/bin/python3
import uuid
import datetime
class MyObject:
    def __init__(self):
        self.__id = str(uuid.uuid4())

    def uid(self):
        return self.__id

o = MyObject()
print(o.uid())
p = MyObject()
print(p.uid())
q = MyObject()
print(q.uid())
r = MyObject()
print(r.uid())
s = MyObject()
print(s.uid())
print(datetime.datetime.now())
