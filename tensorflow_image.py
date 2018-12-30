import tensorflow as tf
import matplotlib.pyplot as plt
import numpy as np
from PIL import Image


randomInt = np.random.randint(256, size=(1000, 1000))
randomFloat = tf.to_float(randomInt)

with tf.Session() as session:
	result = session.run(randomFloat)
	im = Image.fromarray(result, "RGB")
	
	plt.imshow(im)
	plt.show()
