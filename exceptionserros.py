# try:
#     print("h")
#     while(1):
#         pass
# except:
#     print("exception ocrd")
#     while 1:
#         pass

# def test():
#     try:
#         print(int("h"))
#     except TypeError:
#         print("exception ocrd")

try:
    # test()
    try:
        print(int("h"))
    except TypeError:
        print("exception ocrd")
except:
    print("exception ocrd")