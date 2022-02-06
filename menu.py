from argparse import ArgumentError
from typing import List, Callable

# A MenuItem has a name and a func, which bears the MenuItem's functionality.
class MenuItem:
    name: str
    # Should be used to bear menu item functionality.  A selection of this MenuItem will result in the invocation of this function.
    # The function will return false if the containing menu should be exited following completion and true if it should not.
    # E.g. An "exit" menu item may be a lambda that simply returns false.  A menu item that should never exit the menu will always return true.
    func: Callable[[], bool]
    def __init__(self, name: str, func: Callable[[], bool]):
        if not func:
            raise ArgumentError
        self.name = name
        self.func = func

# A menu has a name, and a menu has a list of items. A Menu can be prompted to standard out by passing it to prompt_menu.
class Menu:
    name: str
    items: List[MenuItem]
    def __init__(self, name: str, items: List[MenuItem]):
        if not items:
            raise ArgumentError
        self.name = name
        self.items = items

# Prints one line per item of the menu argument of the following format:
# "{index}: {name}"
# where index is the index of the menu item (starting from 0) and name is the name of the menu item.
# After printing, it waits for user input.  If the input is in range, the corresponding menu item's func is called.
# If the func returns false, the function will return to the caller.  Otherwise, the prompt will loop.
def prompt_menu(menu: Menu) -> bool:
    if not menu:
        raise ArgumentError
    while True:
        print(f'\n{menu.name}')

        # Print menu items
        for index, menu_item in enumerate(menu.items):
            print(f'{index}: {menu_item.name}')

        # Validate selection
        menu_selection = input('Give us an input: ')
        if not menu_selection.isnumeric() or int(menu_selection) >= len(menu.items):
            print('Bad input')

        # Call menu function
        if not menu.items[int(menu_selection)].func():
            break