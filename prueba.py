import tensorflow as tf

# Imprime las GPUs disponibles
print("GPUs disponibles: ", tf.config.list_physical_devices('GPU'))

# Crea un tensor aleatorio de 500x500
a = tf.random.normal([500, 500])

# Multiplica el tensor por sí mismo
b = tf.matmul(a, a)

# Imprime el resultado
print(b)
