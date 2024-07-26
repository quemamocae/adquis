import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense

# Define the model
model = Sequential([
    Dense(16, activation='relu', input_shape=(10,)),  # Input layer
    Dense(8, activation='relu'),                      # Hidden layer
    Dense(1, activation='sigmoid')                    # Output layer for binary classification
])

# Compile the model
model.compile(
    loss='binary_crossentropy',
    optimizer='adam',
    metrics=['accuracy']
)

# Summary of the model
model.summary()

# Example data (10 features, binary labels)
import numpy as np
X_train = np.random.rand(100, 10)  # 100 samples, 10 features each
y_train = np.random.randint(0, 2, 100)  # 100 binary labels

# Train the model
model.fit(X_train, y_train, epochs=10, batch_size=32)
