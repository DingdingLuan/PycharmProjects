import pandas as pd
import matplotlib.pyplot as plt
import numpy as np


def zseita():
    # 读取数据文件
    df = pd.read_excel("/Users/dingding/Desktop/Angle/5.6/containseita5.xlsx")
    # 取出身高和体重两列数据
    z = df['z']
    seita = df['seita']
    plt.figure(figsize=(10, 5))
    plt.scatter(z, seita,s=5,alpha=1,marker='o',c='r')
    # x，y取值范围设置
    # 可以过滤掉一部分脏数据

    plt.xlim(0, 5.5)
    plt.ylim(0, 1.5)
    plt.axis()
    # 设置title和x，y轴的label
    plt.title("Z-seita")
    plt.xlabel("z")
    plt.ylabel("seita[degree]")
    # 保存图片到指定路径
    # plt.savefig("/Users/dingding/Desktop/zseita.jpg")
    # 展示图片 *必加
    plt.show()


def zeiso():
    df = pd.read_excel("/Users/dingding/Desktop/Angle/5.6/containseita5.xlsx")
    z = df['z']
    eiso = df['eisocalculate']
    plt.figure(figsize=(10, 5))
    plt.scatter(z, np.log10(eiso), s=5, alpha=1, marker='o', c='r')
    plt.xlim(0, 5.5)
    # plt.ylim(10**48, 10**55)
    plt.axis()
    plt.title("Z-Eisocalculate")
    plt.xlabel("z")
    plt.ylabel("Eiso")
    plt.savefig("/Users/dingding/Desktop/zEiso.jpg")
    plt.show()

def zegamma():
    df = pd.read_excel("/Users/dingding/Desktop/Angle/5.6/containseita5.xlsx")
    z = df['z']
    egamma = df['egammacalculate']
    plt.figure(figsize=(10, 5))
    plt.scatter(z, np.log10(egamma), s=5, alpha=1, marker='o', c='r')
    plt.xlim(0, 5.5)
    # plt.ylim(0, 1.5)
    plt.axis()
    plt.title("Z-Egammacalculate")
    plt.xlabel("z")
    plt.ylabel("Egamma")
    plt.savefig("/Users/dingding/Desktop/zEgamma.jpg")
    plt.show()

# zseita()
zeiso()
zegamma()
