import pandas as pd
import matplotlib.pyplot as plt
import numpy as np




def articlefortranall():
    df = pd.read_excel("/Users/dingding/Desktop/plot/article_Fortranall.xlsx")
    z = df['z']
    egamma=df['egamma']
    ep=df['ep']
    epz=ep*z
    seita=df['seita']
    plt.figure(figsize=(10, 5))
    plt.scatter(z, seita, s=5, alpha=1, marker='o', c='r')
    plt.xlim(0, 8)
    plt.ylim(0,50)
    plt.axis()
    plt.title("Z-Seita_FromArticle_byFortran")
    plt.xlabel("z")
    plt.ylabel("Seita[degree]")
    plt.savefig("/Users/dingding/Desktop/plot/Z-Seita_FromArticle_byFortran.jpg")
    # plt.show(Block=False)

    plt.figure(figsize=(7, 5))
    plt.scatter(np.log10(egamma), np.log10(epz), s=5, alpha=1, marker='o', c='r')
    plt.xlim(48, 53)
    plt.ylim(1, 4)
    plt.axis()
    plt.title("Egamma-Ep,z_FromArticle_byFortran")
    plt.ylabel("log[Ep,z]")
    plt.xlabel("log[Egamma]")
    plt.savefig("/Users/dingding/Desktop/plot/Egamma-Ep,z_FromArticle_byFortran.jpg")
    # plt.show()


def articlepythonall():
    df = pd.read_excel("/Users/dingding/Desktop/plot/artivle_fromPythonall.xlsx")
    z = df['z']
    egamma=df['egamma']
    ep = df['ep']
    epz = ep * z
    seita = df['seita']
    plt.figure(figsize=(10, 5))
    plt.scatter(z, seita, s=5, alpha=1, marker='o', c='r')
    plt.xlim(0, 8)
    plt.ylim(0,50)
    plt.axis()
    plt.title("Z-Seita_FromArticle_byPython")
    plt.xlabel("z")
    plt.ylabel("Seita[degree]")
    plt.savefig("/Users/dingding/Desktop/plot/Z-Seita_FromArticle_byPython.jpg")
    # plt.show()

    plt.figure(figsize=(7, 5))
    plt.scatter(np.log10(egamma), np.log10(epz), s=5, alpha=1, marker='o', c='r')
    plt.xlim(48, 53)
    plt.ylim(1, 4)
    plt.axis()
    plt.title("Egamma-Ep,z_FromArticle_byPython")
    plt.ylabel("log[Ep,z]")
    plt.xlabel("log[Egamma]")
    plt.savefig("/Users/dingding/Desktop/plot/Egamma-Ep,z_FromArticle_byPython.jpg")
    # plt.show()


def unifoABfortran():
    df = pd.read_excel("/Users/dingding/Desktop/plot/uniformab_Fortran_selected.xlsx")
    z = df['z']
    egamma=df['egamma']
    ep = df['ep']
    epz = ep * z
    seita = df['seita']
    plt.figure(figsize=(10, 5))
    plt.scatter(z, seita, s=5, alpha=1, marker='o', c='r')
    plt.xlim(0, 8)
    plt.ylim(0,50)
    plt.axis()
    plt.title("Z-Seita_unifoAB_byFortran")
    plt.xlabel("z")
    plt.ylabel("Seita[degree]")
    plt.savefig("/Users/dingding/Desktop/plot/Z-Seita_unifoAB_byFortran.jpg")
    # plt.show()

    plt.figure(figsize=(7, 5))
    plt.scatter(np.log10(egamma), np.log10(epz), s=5, alpha=1, marker='o', c='r')
    plt.xlim(48, 53)
    plt.ylim(1, 4)
    plt.axis()
    plt.title("Egamma-Ep,z_unifoAB_byFortran")
    plt.ylabel("log[Ep,z]")
    plt.xlabel("log[Egamma]")
    plt.savefig("/Users/dingding/Desktop/plot/Egamma-Ep,z_unifoAB_byFortran.jpg")
    # plt.show()


def unifoABpython():
    df = pd.read_excel("/Users/dingding/Desktop/plot/uniformab_Python_selected.xlsx")
    z = df['z']
    egamma=df['egamma']
    ep = df['ep']
    epz = ep * z
    seita = df['seita']
    plt.figure(figsize=(10, 5))
    plt.scatter(z, seita, s=5, alpha=1, marker='o', c='r')
    plt.xlim(0, 8)
    plt.ylim(0,50)
    plt.axis()
    plt.title("Z-Seita_unifoAB_byPython")
    plt.xlabel("z")
    plt.ylabel("Seita[degree]")
    plt.savefig("/Users/dingding/Desktop/plot/Z-Seita_unifoAB_byPython.jpg")
    # plt.show()

    plt.figure(figsize=(7, 5))
    plt.scatter(np.log10(egamma), np.log10(epz), s=5, alpha=1, marker='o', c='r')
    plt.xlim(48, 53)
    plt.ylim(1, 4)
    plt.axis()
    plt.title("Egamma-Ep,z_unifoAB_byPython")
    plt.ylabel("log[Ep,z]")
    plt.xlabel("log[Egamma]")
    plt.savefig("/Users/dingding/Desktop/plot/Egamma-Ep,z_unifoAB_byPython.jpg")
    # plt.show()





def unifoABEpfortran():
    df = pd.read_excel("/Users/dingding/Desktop/plot/uniformabEp_Fortran_selected.xlsx")
    z = df['z']
    egamma=df['egamma']
    seita = df['seita']
    plt.figure(figsize=(10, 5))
    plt.scatter(z, seita, s=5, alpha=1, marker='o', c='r')
    plt.xlim(0, 8)
    plt.ylim(0,50)
    plt.axis()
    plt.title("Z-Seita_unifoABEp_byFortran")
    plt.xlabel("z")
    plt.ylabel("Seita[degree]")
    plt.savefig("/Users/dingding/Desktop/plot/Z-Seita_unifoABEp_byFortran.jpg")
    # plt.show()






def unifoABEppython():
    df = pd.read_excel("/Users/dingding/Desktop/plot/uniformabEp_Python_Selected.xlsx")
    z = df['z']
    egamma=df['egamma']
    seita = df['seita']
    plt.figure(figsize=(10, 5))
    plt.scatter(z, seita, s=5, alpha=1, marker='o', c='r')
    plt.xlim(0, 8)
    plt.ylim(0,50)
    plt.axis()
    plt.title("Z-Seita_unifoABEp_byPython")
    plt.xlabel("z")
    plt.ylabel("Seita[degree]")
    plt.savefig("/Users/dingding/Desktop/plot/Z-Seita_unifoABEp_byPython.jpg")
    # plt.show()



articlepythonall()
articlefortranall()
unifoABEppython()
unifoABEpfortran()
unifoABfortran()
unifoABpython()