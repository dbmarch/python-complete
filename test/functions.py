# def center_text(*args, sep=' ', end = '\n', file=None, flush=False):
#     text = ""
#     for arg in args:
#         text += str(arg) + sep
#     left = (80 - len(text))//2
#     print(" "*left, text, end=end, file=file, flush=flush)
#
#
# with open("centered", mode="w") as centered_file:
#     center_text("this is some text", file = centered_file)
#     center_text("this is longer string with some text", file=centered_file)
#     center_text("this is text", file=centered_file)
#     center_text("first", "second", 3, 4, "five", sep=":", file=centered_file)


def center_text(*args, sep= ' ' ):
    text = ""
    for arg in args:
        text += str(arg) + sep
    left = (80 - len(text))//2
    return " "*left + text


print(center_text("this is some text"))
print(center_text("this is longer string with some text"))
print(center_text("this is text"))
print(center_text("first", "second", 3, 4, "five", sep=":"))
print("=" + str(12*3))
print (sorted(['b','d','c','a']))