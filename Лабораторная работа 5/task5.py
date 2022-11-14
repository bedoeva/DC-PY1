import string
from random import sample


def get_random_password(l=8) -> str:
    words_ = string.ascii_letters + string.digits
    pass_ = "".join(sample(words_, l))
    return pass_


print(get_random_password())
