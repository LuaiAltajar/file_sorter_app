import os
import shutil
import fisier_extensii

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
            shutil.move(fr'{path_curent}\{file}', fr'{path_curent}\{item.keys()}')