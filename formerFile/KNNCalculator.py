from sklearn.datasets import load_iris
from sklearn.model_selection import cross_val_score
import matplotlib.pyplot as plt
from sklearn.neighbors import KNeighborsClassifier

iris = load_iris()
x = iris.data
y = iris.target
Krange = range(1, 51)
Kerror = []
for k in Krange:
    knn = KNeighborsClassifier(k)
    scores = cross_val_score(knn, x, y, cv=5, scoring='accuracy')
    Kerror.append(1 - scores.mean())

plt.plot(Krange, Kerror)
plt.xlabel('value of k for KNN')
plt.ylabel('Error')
plt.show()
