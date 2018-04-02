import csv
from keras.models import Sequential, Model
from keras.layers import Dense
from keras.layers import Input
from keras.layers import concatenate
from sklearn.model_selection import train_test_split
from sklearn.utils import shuffle
from keras.optimizers import Adam
import numpy as np
from keras.callbacks import ModelCheckpoint
from keras.models import model_from_json
#from keras.layers import Dense, Flatten, Input, merge, Lambda
#from keras.initializations import normal, identity

X=[]
Y=[]
with open('trainingdata.csv') as File:
    reader=csv.reader(File)
    for row in reader:
        X.append([float(row[0]),float(row[1]),float(row[2]),float(row[3]),float(row[4]),float(row[5]),float(row[6]),float(row[7]),float(row[8])])
        Y.append([float(row[11]),float(row[9])])

train_samples,validation_samples=train_test_split(X,test_size=0.1)
def generator(samples, batch_size=32):
    num_samples = len(samples)
    while 1: # Loop forever so the generator never terminates
        shuffle(samples)
        for offset in range(0, num_samples, batch_size):
            batch_samples = samples[offset:offset+batch_size]

            inputs = []
            outputs = []
            for batch_sample in batch_samples:
                inputs.append(batch_sample[0:9])
                outputs.append(batch_sample[9:12])

            X_train = np.array(inputs)
            y_train = np.array(outputs)
            
            yield shuffle(X_train, y_train)

# compile and train the model using the generator function
#train_generator = generator(train_samples, batch_size=32)
#validation_generator = generator(validation_samples, batch_size=32)

#model=Sequential()
#model.add(Dense(12,input_dim=9,activation='relu'))
#model.add(Dense(8, activation='relu'))
#model.add(Dense(2, activation='tanh'))

#model.add(Dense(12,input_dim=9,activation='relu'))
#model.add(Dense(6, activation='relu'))
#model.add(Dense(3, activation='relu'))
#model.add(Dense(1, activation='tanh'))

inp=Input(shape=(9,))
layer1=Dense(20,activation='relu')(inp)
layer2=Dense(20,activation='relu')(layer1)
layer3=Dense(20,activation='relu')(layer2)
layer4=Dense(20,activation='relu')(layer3)
layer4a=Dense(1,activation='tanh')(layer4)
layer4b=Dense(1,activation='sigmoid')(layer4)
out=concatenate([layer4a, layer4b])
model=Model(inputs=inp, outputs=out)

#S=Input(shape=[9])
#h0 = Dense(6, activation='relu')(S)
#h1 = Dense(3, activation='relu')(h0)
#Steering = Dense(1,activation='tanh')(h1)   
#Acceleration = Dense(1,activation='sigmoid')(h1)   
#Brake = Dense(1,activation='sigmoid')(h1)   
#V = merge([Steering,Acceleration,Brake],mode='concat')          
#model = Model(input=S,output=V)
model.compile(loss='mse', optimizer='adam',metrics=['accuracy'])
#print("Model summary:\n", model.summary())

batch_size = 32
nb_epoch = 10
#model.fit(X, Y, nb_epoch=10, batch_size=10)
#model.fit_generator(train_generator, 
#                    samples_per_epoch=len(train_samples), 
#                    validation_data=validation_generator,
#                    nb_val_samples=len(validation_samples), nb_epoch=nb_epoch)

model.fit(np.array(X),np.array(Y),nb_epoch=1,batch_size=32)
model_json = model.to_json()
with open("model.json", "w") as json_file:
    json_file.write(model_json)
    
model.save_weights("model.h5")
print("Saved model to disk")


