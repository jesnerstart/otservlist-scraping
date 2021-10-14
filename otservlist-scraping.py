from bs4 import BeautifulSoup
from urllib.request import urlopen
from urllib.error import HTTPError
from urllib.error import URLError


def getOtserv(url):
    try:
        html = urlopen(url)
    except HTTPError:
        return None
    except URLError:
        return None
    except ValueError:
        return None

    try:
        ots = []
        bs = BeautifulSoup(html, "html.parser")
        listOtserv = bs.find_all("th", {"class": "pl-15"})

        if listOtserv:
            for ot in listOtserv:
                ots.append(ot.getText())
        else:
            return None

    except AttributeError:
        return None

    return ots


def saveOts(listOt):
    for ot in listOt:
        with open("otservlist.txt", "+a") as file:
            file.write(f"{ot} \n")


def getLink():
    url = input("Otservlist URL: ").strip()
    return url


def main():
    ot = getOtserv(getLink())
    if ot == None:
        print("Não foi possivel encontrar!")
    else:
        saveOts(ot)
        print("salvo com sucesso!")


if __name__ == "__main__":
    while True:
        main()
