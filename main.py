# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.

def Reverse(lst):
    print("input: " + str(lst))
    new_lst = lst[::-1]
    print("reverse list: " + str(new_lst))
    return new_lst


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    lst = [10, 11, 12, 13, 14, 15]
    print_hi('PyCharm')
    Reverse(lst)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
