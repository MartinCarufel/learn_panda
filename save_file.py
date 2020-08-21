import os


def add_resto_keyword():
    kw = input("Entrer le mot clef: ")

    with open("resto.csv", "a"):
        pass

    with open("resto.csv", "r") as f:
        if len(f.read()) > 0:
            resto_list = read_resto_list()
            print(resto_list)
            if kw.upper() not in resto_list:
                with open("resto.csv", "a") as f:
                    f.write("," + kw.upper())
            else:
                print("deja la")
        else:
            with open("resto.csv", "a") as f:
                f.write(kw.upper())

def read_resto_list():
    with open("resto.csv", "r") as f:
        return f.read().split(",")

add_resto_keyword()
x = read_resto_list()
print(x)