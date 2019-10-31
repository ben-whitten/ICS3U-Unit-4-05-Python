#!/usr/bin/env python3

# Created by: Ben Whitten
# Created on: October 2019
# This is a program which tells you the total value of multiple numbers.


# This allows me to do things with the text.
class color:
    PURPLE = '\033[95m'
    CYAN = '\033[96m'
    DARKCYAN = '\033[36m'
    BLUE = '\033[94m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    END = '\033[0m'


def main():
    # This is what runs the program.
    print("")
    print("This program will tell you the"
          " value of multiple numbers...")
    print('')

    while True:
        # Input
        amount_as_string = input(color.BOLD + color.YELLOW + 'Input how many'
                                 ' numbers you want to add: ' + color.END)
        number_total = 0
        next_number = 0

        # Process
        try:
            amount = int(amount_as_string)

            while next_number < amount:
                chosen_number_string = input(color.BOLD + color.YELLOW +
                                             'Input a number:' + color.END)

                try:
                    chosen_number = int(chosen_number_string)

                    if chosen_number < 0:
                        next_number = next_number + 1
                        continue
                    else:
                        number_total = number_total + chosen_number
                        next_number = next_number + 1

                # This stops them from putting in something like bob.
                except Exception:
                    print('')
                    print(color.PURPLE + color.UNDERLINE +
                          'That is not a valid number...' + color.END)
                    print("")
                    print("")

            print(color.BOLD + color.GREEN +
                  'the total is: {0}'.format(number_total) + color.END)
            break

        # This stops them from putting in something like bob and gets them to
        except Exception:
            print('')
            print(color.PURPLE + color.UNDERLINE +
                  'That is not a valid number...' + color.END)
            print("")
            print("")


if __name__ == "__main__":
    main()
