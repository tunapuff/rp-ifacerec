# train.py
import cv2, sys, numpy, os, pickle
fn_dir = 'faces'

# Create a list of images and a list of corresponding names
(images, lables, names, id) = ([], [], {}, 0)
for (subdirs, dirs, files) in os.walk(fn_dir):
    for subdir in dirs:
        names[id] = subdir
        subjectpath = os.path.join(fn_dir, subdir)
        for filename in os.listdir(subjectpath):
            path = subjectpath + '/' + filename
            lable = id
            images.append(cv2.imread(path, 0))
            lables.append(int(lable))
        id += 1

# Create a Numpy array from the two lists above
(images, lables) = [numpy.array(lis) for lis in [images, lables]]

# OpenCV trains a model from the images
model = cv2.createFisherFaceRecognizer()
#model = cv2.createEigenFaceRecognizer()
#model = cv2.createLBPHFaceRecognizer()

print('Training model...')
model.train(numpy.asarray(images), numpy.asarray(lables))

print('Saving training data')
model.save('trainingdata.xml')
with open("names.txt",'wb') as f:
    pickle.dump(names, f)

print('Training complete!')

