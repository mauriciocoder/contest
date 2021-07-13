# https://codeforces.com/problemset/problem/705/A


def get_hulk_sentence(layers):
    sentence = "I "
    for i in range(layers):
        sentence += "hate " if i % 2 == 0 else "love "
        if i == layers - 1:
            sentence += "it"
        else:
            sentence += "that I "
    return sentence


if __name__ == "__main__":
    layers = int(input("Layers: "))
    print(get_hulk_sentence(layers))
