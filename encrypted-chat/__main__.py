import random
from __init__ import Encrypt


def get_key_from_exchange(p):
    a = random.randint(960, 1460)
    print("[Send] %s" % str((g**a) % p))
    g_b = int(str(input("Type what your target sent.\n[Input] ")))
    return (g_b**a) % p


try:
    try:
        g = int(input("Welcome to encrypted chat.\nPlease enter your g-code: "))
    except ValueError:
        print("\n[Error] Invalid g input.\n")
        exit(0)
    try:
        p = int(input("Please enter your p-code: "))
    except ValueError:
        print("\n[Error] Invalid p input.\n")
        exit(0)
    while True:
        try:
            option = int(
                input(
                    "Enter your option. 1 for encrypting, 2 for decrypting.\n[Option] "
                )
            )
            if option not in [1, 2]:
                print("\n[Warning] Invalid option.\n")
                continue
        except ValueError:
            print("\n[Warning] Invalid option.\n")
            continue
        if option == 1:
            print("(Ctrl+C to quit encrypting mode)")
            key = get_key_from_exchange(p)
            de = Encrypt(str(key + 1e8)[-8:], "abcdefgh")
            while True:
                try:
                    m = de.encrypt(input("[Input] Your message: ").encode("utf8"))
                    print("[Send] %s" % m)
                except KeyboardInterrupt:
                    break
        if option == 2:
            print("(Ctrl+C to quit decrypting mode)")
            key = get_key_from_exchange(p)
            de = Encrypt(str(key + 1e8)[-8:], "abcdefgh")
            while True:
                try:
                    m = de.decrypt(input("[Input] Your code: ").encode("utf8"))
                    print("[Return] %s" % m)
                except KeyboardInterrupt:
                    break
except KeyboardInterrupt:
    print("\n[Warning] User exited the program.\n")
    exit(0)
