import matplotlib.pyplot as plt
import numpy as np
from matplotlib.colors import ListedColormap
from sklearn import neighbors, datasets
n_neighbors = 11  # K 的取值
# 导入鸢尾花的数据，这里只采用前两个特征值,方便画图在二维平面显示
iris = datasets.load_iris()
x = iris.data[:, :2]
y = iris.target


h = .01  # 网格中的步长

# 设置决策边界、以及样本颜色
cmap_light = ListedColormap(['#FFAAAA', '#AAFFAA', '#AAAAFF'])
cmap_bold = ListedColormap(['#FF0000', '#00FF00', '#0000FF'])


#这里绘制两种权重参数下 KNN 的效果图
for weights in ['uniform', 'distance']:
# 创建了一个 knn 分类器的实例，并训练模型。
    clf = neighbors.KNeighborsClassifier(n_neighbors, weights=weights)
    clf.fit(x, y)
    # 绘制决策边界。
    # [x_min, x_max]x[y_min, y_max]为坐标轴范围
    x_min, x_max = x[:, 0].min() - 1, x[:, 0].max() + 1
    y_min, y_max = x[:, 1].min() - 1, x[:, 1].max() + 1
    xx, yy = np.meshgrid(np.arange(x_min, x_max, h),
                        np.arange(y_min, y_max, h))
    Z = clf.predict(np.c_[xx.ravel(), yy.ravel()])
    print(Z)
    # 将结果放入一个图中
    Z = Z.reshape(xx.shape)
    plt.figure()
    plt.pcolormesh(xx, yy, Z, cmap=cmap_light)

    # 绘制训练点
    plt.scatter(x[:, 0], x[:, 1], c=y, cmap=cmap_bold)
    plt.xlim(xx.min(), xx.max())
    plt.ylim(yy.min(), yy.max())
    plt.title("3-Class classification (k = %i, weights = '%s')"
            % (n_neighbors, weights))

plt.show()