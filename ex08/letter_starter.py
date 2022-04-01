import sys


def main(*args):
    if len(args) != 2:
        return
    name, surname = args[1].split('@')[0].split('.')
    print(f"Dear {name.capitalize()}, welcome to our team. We are sure that it will be a pleasure to work with you. That’s a precondition for the professionals that our company hires.")


if __name__ == '__main__':
    main(*sys.argv)
