import string
import secrets


def gen_key(parts=4, chars_per_part=8):
    alphabet = string.ascii_uppercase
    return '-'.join(''.join(secrets.choice(alphabet)
                    for i in range(chars_per_part)) for j in range(parts))
