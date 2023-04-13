import tensorflow as tf

model = tf.keras.models.load_model('Model_test.h5')
tf.saved_model.save(model, 'model')

config = model.get_config()
print(config["layers"][0]["config"]["batch_input_shape"])
