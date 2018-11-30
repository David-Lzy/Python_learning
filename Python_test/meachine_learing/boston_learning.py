from sklearn.datasets import load_boston
boston = load_boston()
print(boston.data.shape)
from sklearn.datasets import load_digits
digits = load_digits()
import matplotlib.pyplot as plt
plt.matshow(digits.images[1])
plt.show()