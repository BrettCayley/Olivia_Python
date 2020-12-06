from pprint import pprint
import numpy as np
# import matplotlib.pyplot as plt

# import seaborn as sns

# import tensorflow.compat.v2 as tf
# tf.enable_v2_behavior()

# import tensorflow_probability as tfp

# sns.reset_defaults()
# sns.set_context(context='talk',font_scale=0.7)
# plt.rcParams['image.cmap'] = 'viridis'


a = np.array([1,2])
# tfd = tfp.distributions
# tfb = tfp.bijectors

def add(a, b):
    return a + b

sum = add(1,2)
print(sum)
print(a)
# # A standard normal
# normal = tfd.Normal(loc=0., scale=1.)
# print(normal)