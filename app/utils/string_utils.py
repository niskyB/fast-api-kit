import random
import secrets
import string


def gen_session(length: int):
    return secrets.token_urlsafe(length)


def gen_verification_code(length: int):
    letters = string.digits
    return "".join(random.choice(letters) for i in range(length))
