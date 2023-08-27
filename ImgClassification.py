# This is a Sample CNN code for Image Classification
import tensorflow as tf
from tensorflow import keras
from tensorflow.python.keras import layers
from keras.preprocessing.image import ImageDataGenerator

num_classes = 6

datagen = ImageDataGenerator(
    rescale=1./255,  # Normalize pixel values
    rotation_range=20,  # Randomly rotate images
    width_shift_range=0.2,  # Randomly shift image width
    height_shift_range=0.2,  # Randomly shift image height
    horizontal_flip=True,  # Randomly flip images horizontally
    shear_range=0.2,  # Apply shear transformation
    zoom_range=0.2  # Apply zoom transformation
)

train_generator = datagen.flow_from_directory(
    'D://VU//EthirNeechal//CV//CNN//Train//',
    target_size=(150, 150),  # Resize images to a consistent size
    batch_size=32,  # Batch size for training
    class_mode='categorical'  # For multi-class classification
)

test_generator = datagen.flow_from_directory(
    'D://VU//EthirNeechal//CV//CNN//Test//',
    target_size=(150, 150),
    batch_size=32,
    class_mode='categorical'
)


model = keras.Sequential([
    layers.Conv2D(32, (3, 3), activation='relu', input_shape=(150, 150, 3)),
    layers.MaxPooling2D((2, 2)),
    layers.Conv2D(64, (3, 3), activation='relu'),
    layers.MaxPooling2D((2, 2)),
    layers.Conv2D(128, (3, 3), activation='relu'),
    layers.MaxPooling2D((2, 2)),
    layers.Flatten(),
    layers.Dense(128, activation='relu'),
    layers.Dense(num_classes, activation='softmax')  # Number of classes
])


model.compile(optimizer='adam',
              loss='categorical_crossentropy',
              metrics=['accuracy'])

history = model.fit(
    train_generator,
    epochs=10,  # Number of training epochs
    validation_data=test_generator
)

test_loss, test_accuracy = model.evaluate(test_generator, verbose=2)
print('\nTest accuracy:', test_accuracy)
