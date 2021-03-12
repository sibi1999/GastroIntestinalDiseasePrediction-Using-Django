from django.shortcuts import render
from django.core.files.storage import FileSystemStorage
from keras.models import load_model
from keras.preprocessing import image
import tensorflow as tf
import json
from tensorflow import Graph


img_height, img_width=256,256
with open('./models/label.json','r') as f:
    labelInfo=f.read()

labelInfo=json.loads(labelInfo)


model_graph = Graph()
with model_graph.as_default():
    tf_session = tf.compat.v1.Session()
    with tf_session.as_default():
        model=load_model('./models/fp(15epoch).h5')


def home(request):
    return render(request,'imageprocessor/home.html')


def predictimage(request):
    print (request)
    print (request.POST.dict())
    fileObj=request.FILES['imgfile']
    fs=FileSystemStorage()
    filePathName=fs.save(fileObj.name,fileObj)
    fileUrl=fs.url(filePathName)
    testimage='.'+fileUrl
    img = image.load_img(testimage, target_size=(img_height, img_width))
    x = image.img_to_array(img)
    x=x/255
    x=x.reshape(1,img_height, img_width,3)
    with model_graph.as_default():
        with tf_session.as_default():
            predi=model.predict(x)

    import numpy as np
    predictedLabel=labelInfo[str(np.argmax(predi[0]))]
    print(predictedLabel,predi)

    context={'up_image':fileUrl,'predictedLabel':predictedLabel}
    return render(request,'imageprocessor/home.html',context) 

