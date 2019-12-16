import pandas as pd
import matplotlib.pyplot as plt
import numpy as np




# def articlefortranall():
#     df = pd.read_excel("/Users/dingding/Desktop/plot/article_Fortranall.xlsx")
#     z = df['z']
#     egamma=df['egamma']
#     ep=df['ep']
#     epz=ep*z
#     seita=df['seita']
#     plt.figure(figsize=(10, 5))
#     plt.scatter(z, seita, s=5, alpha=1, marker='o', c='r')
#     plt.xlim(0, 8)
#     plt.ylim(0,50)
#     plt.axis()
#     plt.title("Z-Seita_FromArticle_byFortran")
#     plt.xlabel("z")
#     plt.ylabel("Seita[degree]")
#     # plt.savefig("/Users/dingding/Desktop/plot/Z-Seita_FromArticle_byFortran.jpg")
#     plt.show(Block=False)
#
#     plt.figure(figsize=(7, 5))
#     plt.scatter(np.log10(egamma), np.log10(epz), s=5, alpha=1, marker='o', c='r')
#     plt.xlim(48, 53)
#     plt.ylim(1, 4)
#     plt.axis()
#     plt.title("Egamma-Ep,z_FromArticle_byFortran")
#     plt.ylabel("log[Ep,z]")
#     plt.xlabel("log[Egamma]")
#     # plt.savefig("/Users/dingding/Desktop/plot/Egamma-Ep,z_FromArticle_byFortran.jpg")
#     # plt.show()