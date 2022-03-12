# This is a sample Python script.
from linked_list import Node, LinkedList
# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    list = LinkedList()
    list.add_last(1)
    list.add_last(2)
    list.add_last(3)
    print(list.remove_last())
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
