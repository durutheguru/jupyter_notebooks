# To add a new cell, type '# %%'
# To add a new markdown cell, type '# %% [markdown]'
# %%
import matplotlib.pyplot as plt
from sklearn.datasets import fetch_openml
import matplotlib.cm as cm


mnist = fetch_openml('mnist_784')

counter = 1
# for i in range(1, 4):
#     for j in range(1, 6):
#         plt.subplot(3, 5, counter)
#         plt.imshow(mnist.data[(i - 1) * 8000 + j].reshape((28, 28)), cmap=cm.Greys_r)
#         plt.axis('off')
#         counter += 1
# plt.show()


# %%



