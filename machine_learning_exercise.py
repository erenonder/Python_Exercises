import tensorflow as tf
from tensorflow import keras
import numpy as np
import matplotlib.pyplot as plt
import requests
requests.packages.urllib3.disable_warnings()
import ssl

try:
    _create_unverified_https_context = ssl._create_unverified_context
except AttributeError:
    # Legacy Python that doesn't verify HTTPS certificates by default
    pass
else:
    # Handle target environment that doesn't support HTTPS verification
    ssl._create_default_https_context = _create_unverified_https_context


data = keras.datasets.fashion_mnist

(train_images, train_labels), (test_images, test_labels) = data.load_data()

class_names = ['T-shirt/top', 'Trouser', 'Pullover', 'Dress', 'Coat',
               'Sandal', 'Shirt', 'Sneaker', 'Bag', 'Ankle boot']

train_images = train_images / 255  # not needed only easier to work with
test_images = test_images / 255  # not needed only easier to work with
# print(f'train_labels: {train_labels[7]}')
# print(train_images[7])


model = keras.Sequential([
    keras.layers.Flatten(input_shape=(28, 28)),
    keras.layers.Dense(128, activation="relu"),
    keras.layers.Dense(10, activation="softmax")
])

model.compile(optimizer="adam",
              loss="sparse_categorical_crossentropy", metrics=["accuracy"])

model.fit(train_images, train_labels, epochs=10)

prediction = model.predict(test_images)

for i in range(10):
    plt.grid(False)
    plt.imshow(test_images[i], cmap=plt.cm.binary)
    plt.xlabel("Actual: " + class_names[test_labels[i]])
    plt.title("Prediction: " + class_names[np.argmax(prediction[i])])
    # print(f"image {i} is possibly {class_names[np.argmax(prediction[i])]}")
    plt.show()

# test_loss, test_acc = model.evaluate(test_images, test_labels)

# print(f"Tested Accuracy: {test_acc:.3}")

# plt.imshow(train_images[7])
# plt.show()
