import os
import shutil
import fisier_extensii


def filtru_exstensii(folder_name):
    """
    Selecteaza textul de dupa ultimul punct ca si extensie
    :param folder_name: locatia fisierelor
    :return:
    """
    for file in os.listdir(folder_name):
        extension = file.split('.')[-1]
        mutare_fisier(extension, file, folder_name)


def mutare_fisier(extension, file, path_curent):
    """
    Muta fisierele in directorul specific
    :param extension: determina directorul in care se muta fisierul
    :param file: fisierul
    :param path_curent: Locatia initiala
    :return:
    """
    for item in fisier_extensii.extensions():
        if extension in item.values():
            creare_director(item.keys(), path_curent)
            shutil.move(fr'{path_curent}\{file}', fr'{path_curent}\{item.keys()}')


def creare_director(nume_fisier, loc):
    """
    Verifica daca exista un fisier cu numele primit, si creaza unul daca nu exista
    :param nume_fisier: folosit pentru verificare
    :param loc: locatia e folosita pentru a crea pathul nou
    :return:
    """
    if os.path.exists(fr'{loc}\{nume_fisier}'):
        pass
    else:
        os.mkdir(nume_fisier)


if __name__ == '__main__':

    locatie = input("Locatie:")
    filtru_exstensii(locatie)
