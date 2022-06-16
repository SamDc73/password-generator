import secrets
import string
import argparse

parser = argparse.ArgumentParser(description="Generate strong and complicated password")
parser.add_argument('length', type=int, help='The length of the number')

parser.add_argument(
    "--no-symbols",
    default=False,
    action="store_true",
    help="Generate a password with no special characters",
)

parser.add_argument(
    "--only-numbers",
    default=False,
    action="store_true",
    help="Generate a password consisting of only numbers",
)

args = parser.parse_args()


def main(length):
    if args.no_symbols:
        alphabet = string.ascii_letters + string.digits
    elif args.only_numbers:
        alphabet = string.digits
    else:
        alphabet = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(secrets.choice(alphabet) for i in range(length))
    return password


if __name__ == "__main__":
    password_final = main(args.length)
    print(password_final)
