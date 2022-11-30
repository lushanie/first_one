
# treat this key like a password and keep it secret!
key = "777969f0-6b1e-11ed-9a01-ab90ff78a057a28b7bfb-e324-4d0e-9e7c-0bdca43ff35e"

# this will train your model and might take a little while
myproject = MLforKidsImageProject(key)
myproject.train_model()

# CHANGE THIS to the image file you want to recognize
demo = myproject.prediction("dogs.jpg")

label = demo["class_name"]
confidence = demo["confidence"]

# CHANGE THIS to do something different with the result
print ("result: '%s' with %d%% confidence" % (label, confidence))
