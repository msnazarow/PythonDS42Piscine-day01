import string
import sys


def encode(x, shift: int):
    if x in main.ascii_lowercase:
        return main.ascii_lowercase[(ord(x) - ord('a') + shift) % 26]
    if x in main.ascii_uppercase:
        return main.ascii_lowercase[(ord(x) - ord('A') + shift) % 26]
    return x


def decode(x, shift: int):
    if x in main.ascii_lowercase:
        return main.ascii_lowercase[(ord(x) - ord('a') - shift) % 26]
    if x in main.ascii_uppercase:
        return main.ascii_lowercase[(ord(x) - ord('A') - shift) % 26]
    return x


def main(*args):
    if len(args) != 4:
        raise (AttributeError("Usage: python3 caesar.py encode 'ssh -i private.key user@school21.ru' 12"))
    if not all(ord(c) < 128 for c in args[2]):
        raise (ValueError("The script does not support your language yet."))
    if args[1] == 'encode':
        shift = int(args[3])
        print(''.join(map(lambda x: encode(x, shift), args[2])))
    elif args[1] == 'decode':
        shift = int(args[3])
        print(''.join(map(lambda x: decode(x, shift), args[2])))


if __name__ == '__main__':
    main.ascii_lowercase = 'abcdefghijklmnopqrstuvwxyz'
    main.ascii_uppercase = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    main(*sys.argv)
