import random
# ______________________________


def get_life():
    quotes = [
        "Get a life, people of New Jersey!",
        "Get a life and stop living mine!",
        "Don't panic"
    ]

    life = random.choice(quotes)
    print(life)
    return life
# ______________________________

def do_not_accept_this():
    raise RuntimeError("You've just done a mistake of your life")
# ______________________________




if __name__ == '__main__':
    get_life()

