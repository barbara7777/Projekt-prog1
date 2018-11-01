import re
import os
import csv

pot = "D:/NE_BRIŠI,_SISTEM/NAMIZJE/Programiranje-1/naloga/podatki/"
datoteka = pot+"izhod.html"


def datoteka_v_niz():
    with open(datoteka, 'r', encoding='utf-8') as dat:
        return dat.read()


def shrani_vsebino(directory, ime_datoteke):
    os.makedirs(directory, exist_ok=True)
    path = os.path.join(directory, ime_datoteke)
    with open(path, 'w', encoding='utf-8') as file_out:
        file_out.write(datoteka_v_niz())
    return None


def loci_oglase():
    vzorec = re.compile(
        r'<span class="title">(.*?)<div class="col actionBlock">',
        re.DOTALL)
    ads = re.findall(vzorec, datoteka_v_niz())
    return ads


def slovar_iz_oglasa(oglas):
    vzorci = re.compile(
        r'(?P<delovno_mesto>.*?)</span>.*?'
        r'icon_euro\.png" />\s*<strong>(?P<placilo>.*?)<.*?'
        r'location\.png" />\s*?<strong>(?P<lokacija>.*?)<.*?'
        r'jobContent col">\s*?<p>(?P<opis>.*?)[\n<].*?'
        r'prostih mest:</strong>(?P<st_prostih_mest>.*?)<.*?'
        r'Trajanje:</strong>(?P<trajanje>.*?)<.*?'
        r'Delovnik:</strong>(?P<delovnik>.*?)<.*?'
        r'šifra:</strong>(?P<sifra>.*?)<.*?',
        re.DOTALL)
    data = re.search(vzorci, oglas)
    return data.groupdict()


def seznam_slovarjev_oglasov():  # ads_from_file
    oglasi = loci_oglase()
    seznam = [slovar_iz_oglasa(oglas) for oglas in oglasi]
    return seznam


def write_csv(fieldnames, rows, directory, filename):
    '''Write a CSV file to directory/filename. The fieldnames must be a list of
    strings, the rows a list of dictionaries each mapping a fieldname to a
    cell-value.'''
    os.makedirs(directory, exist_ok=True)
    path = os.path.join(directory, filename)
    with open(path, 'w') as csv_file:
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames, delimiter=';')
        writer.writeheader()
        for row in rows:
            writer.writerow(row)
    return None


def spravi_v_csv():
    vrstice = seznam_slovarjev_oglasov()
    write_csv(vrstice[0].keys(), vrstice, pot, 'izhodni_podatki.csv')
    print('narejeno')

print('zacetek')
spravi_v_csv()
