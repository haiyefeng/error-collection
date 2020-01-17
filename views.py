import numpy as np
import matplotlib.pyplot as plt


def test1():
    plt.figure(figsize=(8, 3))
    x = np.arange(-10, 10, 0.1)
    s = (np.exp(x) - np.exp(-x)) / (np.exp(x) + np.exp(- x))
    f = plt.subplot(111)
    # 画出函数曲线
    plt.plot(x, s, color='r')
    # 添加文字说明
    plt.text(-5., 1000, r'$y=\tanh(x)$', fontsize=13)
    # 设置坐标轴格式
    currentAxis=plt.gca()
    currentAxis.xaxis.set_label_text('x', fontsize=15)
    currentAxis.yaxis.set_label_text('y', fontsize=15)

    plt.show()


def test2():
    # 创建一个 10 * 6 点（point）的图，并设置分辨率为 80
    plt.figure(figsize=(10, 6), dpi=100)

    # 创建一个新的 1 * 1 的子图，接下来的图样绘制在其中的第 1 块（也是唯一的一块）
    plt.subplot(1, 1, 1)

    X = np.linspace(-np.pi, np.pi, 256, endpoint=True)
    C, S = np.cos(X), np.sin(X)

    # 绘制余弦曲线，使用蓝色的、连续的、宽度为 1 （像素）的线条
    plt.plot(X, C, color="blue", linewidth=2.5, linestyle="-")

    # 绘制正弦曲线，使用绿色的、连续的、宽度为 1 （像素）的线条
    plt.plot(X, S, color="green", linewidth=2.5, linestyle="-")

    # 根据x，y的最值设置横纵轴的上下限
    xmin, xmax = X.min(), X.max()
    ymin, ymax = S.min(), S.max()

    dx = (xmax - xmin) * 0.1
    dy = (ymax - ymin) * 0.1

    # 设置横轴的上下限
    # plt.xlim(-4.0, 4.0)
    plt.xlim(xmin - dx, xmax + dx)
    # 设置横轴记号
    # plt.xticks(np.linspace(-4, 4, 9, endpoint=True))
    plt.xticks([-np.pi, -np.pi/2, 0, np.pi/2, np.pi], [r'$-\pi$', r'$-\pi/2$', r'$0$', r'$+\pi/2$', r'$+\pi$'])

    # 设置纵轴的上下限
    # plt.ylim(-1.0, 1.0)
    plt.ylim(ymin - dy, ymax + dy)
    # 设置纵轴记号
    # plt.yticks(np.linspace(-1, 1, 5, endpoint=True))
    plt.yticks([-1, 0, +1], [r'$-1$', r'$0$', r'$+1$'])

    # 移动x,y轴
    ax = plt.gca()
    ax.spines['right'].set_color('none')
    ax.spines['top'].set_color('none')
    ax.xaxis.set_ticks_position('bottom')
    ax.spines['bottom'].set_position(('data', 0))
    ax.yaxis.set_ticks_position('left')
    ax.spines['left'].set_position(('data', 0))
    # 添加图例
    plt.plot(X, C, color="blue", linewidth=2.5, linestyle="-", label="cosine")
    plt.plot(X, S, color="red", linewidth=2.5, linestyle="-", label="sine")

    plt.legend(loc='upper left')
    # 添加注解
    t = 2 * np.pi / 3
    plt.plot([t, t], [0, np.cos(t)], color='blue', linewidth=2.5, linestyle="--")
    plt.scatter([t, ], [np.cos(t), ], 50, color='blue')

    plt.annotate(r'$\sin(\frac{2\pi}{3})=\frac{\sqrt{3}}{2}$',
             xy=(t, np.sin(t)), xycoords='data',
             xytext=(+10, +30), textcoords='offset points', fontsize=16,
             arrowprops=dict(arrowstyle="->", connectionstyle="arc3,rad=.2"))

    plt.plot([t, t], [0, np.sin(t)], color='red', linewidth=2.5, linestyle="--")
    plt.scatter([t, ], [np.sin(t), ], 50, color='red')

    plt.annotate(r'$\cos(\frac{2\pi}{3})=-\frac{1}{2}$',
             xy=(t, np.cos(t)), xycoords='data',
             xytext=(-90, -50), textcoords='offset points', fontsize=16,
             arrowprops=dict(arrowstyle="->", connectionstyle="arc3,rad=.2"))

    # 将遮挡坐标轴上记号标签的曲线设置为半透明
    print(ax.get_xticklabels() + ax.get_yticklabels())
    for label in ax.get_xticklabels() + ax.get_yticklabels():
        label.set_fontsize(16)
        label.set_bbox(dict(facecolor='white', edgecolor='None', alpha=0.65))

    # 以分辨率 72 来保存图片
    plt.savefig("exercice_2.png",dpi=72)

    # 在屏幕上显示
    plt.show()


# 手写数字识别
import paddle
import paddle.fluid as fluid
from paddle.fluid.dygraph.nn import FC
import numpy as np
import os
from PIL import Image

# fluid.optimizer.MomentumOptimizer()
trainset = paddle.dataset.mnist.train()
train_reader = paddle.batch(trainset, batch_size=8)
# 以迭代的形式读取数据
for batch_id, data in enumerate(train_reader()):
    # 获得图像数据，并转为float32类型的数组
    img_data = np.array([x[0] for x in data]).astype('float32')
    # 获得图像标签数据，并转为float32类型的数组
    label_data = np.array([x[1] for x in data]).astype('float32')
    # 打印数据形状
    print("图像数据形状和对应数据为:", img_data.shape, img_data[0])
    print("图像标签形状和对应数据为:", label_data.shape, label_data[0])
    print("\n打印第一个batch的第一个图像，对应标签数字为{}".format(label_data[0]))
    # 显示第一batch的第一个图像
    import matplotlib.pyplot as plt
    img = np.array(img_data[0]+1)*127.5
    img = np.reshape(img, [28, 28]).astype(np.uint8)

    plt.figure("Image") # 图像窗口名称
    plt.imshow(img)
    plt.axis('on') # 关掉坐标轴为 off
    plt.title('image') # 图像题目
    plt.show()
    break