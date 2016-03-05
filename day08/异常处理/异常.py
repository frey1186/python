
int1 = input("input:")
int2 = input("input:")
class Foo(object):
    pass

obj = Foo()
c = range(10)
d = {
    "name":"alex"
}
try:
    int1 = int(int1)
    int2 = int(int2)

    print(new_name)
    d["age"]
    c[100]
    import os1
    b = open("text.file")
    a = obj.name




except AttributeError as e:
    print("attr err:",e)
except IOError as e:
    print("io err: ",e)
except ImportError as e:
    print("import err:",e)
except IndexError as e:
    print("index err:",e)
except KeyError as e:
    print("key err:",e)

except KeyboardInterrupt as e:
    print("ctl c err:",e)

except NameError as e:
    print("name err:",e)

except ValueError as e:
    print("value err:",e)

except Exception as e:
    print("错误.")