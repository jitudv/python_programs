import sys
import os
print(" version = \t %s"%sys.version)
print(sys.version_info)
print("platform   = \t %s"%sys.platform)
sys.path.insert(1,"/home/jays/Desktop/")
print("Enter data by  input Stream ")
data =sys.__stdin__.readline()
print("data = \t %s"%data)
print(sys.builtin_module_names)
print(sys.byteorder)
print(sys.api_version)
print(sys.float_info)
print(sys.exc_clear())
print("tthis is parrent dir  = \t %s"% os.pardir)
os.openpty()
print()
def displayhook(value):
    if value is None:
        return
    # Set '_' to None to avoid recursion
    __builtins__ = None
    text = repr(value)
    try:
        sys.stdout.write(text)
    except UnicodeEncodeError:
        bytes= "hello  jitu "
        bytes = text.encode(sys.stdout.encoding, 'backslashreplace')
        if hasattr(sys.stdout, 'buffer'):
            sys.__stdout__.write(bytes)
        else:
            text = bytes.decode(sys.stdout.encoding, 'strict')
            sys.stdout.write(text)
    sys.stdout.write("\n")
    __builtins__== bytes
displayhook("hii this is jitu ")