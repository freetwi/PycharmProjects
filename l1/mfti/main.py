import library as lib

print('main module', __name__)
lib.foo(3)
lib.foo(4)
x =lib.bar(1, 5)
print(x)

lib.create_object("круг1")
lib.create_object("круг2")
lib.create_object("круг3")
lib.print_objects()

for obj in lib.objects:
    if