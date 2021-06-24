objects = []

def foo(x):
    print('foo', x)

def bar(a, b):
    return  a + b

def create_object(name):
    objects.append("object[" + name + "]")

def print_objects():
    print("все добавленно")
    for obj in objects:
        print(obj)

if __name__ == "__main__":
    print('Library executed seperately. ')
