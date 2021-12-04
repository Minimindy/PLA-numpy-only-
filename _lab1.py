import numpy as np
import matplotlib.pyplot as plt

dataset = np.array([

    [1, 0, 1],
    [1, 3, -1],
    [2, -6, 1],
    [-1, -3, 1],
    [-5, 5, -1],
    [5, 2, 1],
    [-2, 2, -1],
    [-7, 2, -1],
    [4, -4, 1],
    [-5, -1, -1]

])

num = 10
# 切割dataset的數據
x1 = dataset[:, 0]
x2 = dataset[:, 1]
y = dataset[:, 2]


def pla_with_data():

    # 初始值 >> w=[0,0] b=0
    w = np.zeros((2, 1))
    dot = 0
    b = 0
    flag = 1

    for k in range(100):   # 限制無窮迴圈 >> 次數設定100次
        flag = 1
        for i in range(num):     # 看每個點是否為正確

            dot = x1[i]*int(w[0])+x2[i]*int(w[1])   # 將一個點的座標帶入 跟w作內積
            if sign(dot, b) != y[i]:  # 與參考資料y不相符 >> 線劃分錯誤

                flag = 0
                w[0] += y[i] * x1[i]    # 矯正 w = w + y*x
                w[1] += y[i] * x2[i]
                b = b + y[i]            # 矯正 b = b + y
                # print(w, b)

            else:
                continue  # 與參考資料y相符 >> 下一個點

        if flag == 1:
            break  # 全部的點都與參考資料y相符 >> 劃分完成

    return w, b


def sign(dot, b):
    if dot+b >= 0:
        return 1
    else:
        return -1


def draw(x1, x2, y):

    # 製作figure
    fig = plt.figure()

    # 圖表的設定
    ax = fig.add_subplot(1, 1, 1)

    # 散佈圖
    for i in range(num):
        if y[i] == 1:
            ax.scatter(x1[i], x2[i], color='red')
        else:
            ax.scatter(x1[i], x2[i], color='black')

    # data
    x = [2, -5, -2]
    y = [-4, 1, -2]
    ax.scatter(x, y, c='g', marker="x")

    plt.show()


prex1 = [2, -5, -2]
prex2 = [-4, 1, -2]


w, b = pla_with_data()

for i in range(3):
    pre = np.sign((prex1[i]*w[0]+prex2[i]*w[1])+b)
    print('predict example %s = %s' % (i+1, pre))

print('w1 = %s , w2 = %s , b = %s' % (w[0], w[1], b))
draw(x1, x2, y)
