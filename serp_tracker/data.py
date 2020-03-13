def api_key():
    with open("api_key.txt", mode='r') as r_file:
        return r_file.readline().strip()


def load_keywords():
    with open("keywords.txt", mode='r') as r_file:
        return r_file.readlines()
