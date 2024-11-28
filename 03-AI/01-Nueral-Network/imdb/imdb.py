from tensorflow.keras import layers, models
from tensorflow.keras.datasets import imdb
from tensorflow.keras.preprocessing.sequence import pad_sequences
import matplotlib.pyplot as plt
from tensorflow.keras import layers, models, callbacks

max_features = 10000 #vocabulary size
max_len = 100 #maximum revier length (after padding)
x_train = None
y_train = None
x_test = None
y_test = None
history_rnn = None
model_rnn = None

def init_data():
    #load the imdb dataset   - you decide 
    global  x_train, y_train, x_test, y_test, history_rnn, model_rnn

    (x_train, y_train),(x_test, y_test) = imdb.load_data(num_words=max_features)

    #Padding
    x_train = pad_sequences(x_train, maxlen=max_len)
    x_test =  pad_sequences(x_test, maxlen=max_len)

    #RNN
    model_rnn = models.Sequential()

def dump_stats():
    print(f"x_train len :{len(x_train)}")
    print(f"y_train len :{len(y_train)}")
    print(f"      total :{len(x_train) + len(y_train)}")
    print()

    print(f"x_test len :{len(x_test)}")
    print(f"y_test len :{len(y_test)}")
    print(f"     total :{len(x_test) + len(y_test)}")
    print()

def rnn03_imdb_reviews(i, vector_dimensional=32, layers_count=32, epochs=5, batch_size=64):
    global  model_rnn, history_rnn
    #embedding layer
    model_rnn.add(layers.Embedding(max_features, vector_dimensional))

    #simple RNN
    model_rnn.add(layers.SimpleRNN(layers_count))
    model_rnn.add(layers.Dense(1, activation='sigmoid'))    #output
    model_rnn.compile(optimizer="adam", loss='binary_crossentropy', metrics=['accuracy'])

    #implemnt early stopping
    early_stopping = callbacks.EarlyStopping(patience=5, restore_best_weights=True)
    #reduce the learning rate
    reduce_lr = callbacks.ReduceLROnPlateau(factor=0.20, patience=3)


    history_rnn = model_rnn.fit(x_train,y_train, epochs=epochs, batch_size=batch_size,
                                validation_split=0.2, callbacks=[early_stopping, reduce_lr], verbose=False)

    plt.figure(figsize=(6,4))
    plt.plot(history_rnn.history['loss'], label='Ttraining loss (RNN)')
    plt.plot(history_rnn.history['val_loss'], label='Val loss (RNN)')
    plt.title("Simple RNN Model")
    plt.legend()
    plt.grid(True)
    
    # dump_stats()

    # prediction_rnn = model_rnn.predict(x_test[:5])
    loss, accuracy = model_rnn.evaluate(x_test, y_test, verbose=False)
    # print(f"loss :{loss}, Accuracy: {accuracy * 100:.2f}%")
    acc = accuracy * 100

    results = f"{i}, accuracy : {acc:.2f}, vector_dime :{vector_dimensional}, layers_count :{layers_count}, epochs :{epochs}, batch_size :{batch_size}"
    print(results)
    with open('rnn-results.txt', 'a') as file:
        file.write(f"{results}\n")
    
    # for i , prediction in enumerate(prediction_rnn):
    #     sentiment = "P" if prediction > 0.5 else "N"
    #     print(f"Review {i+1} (RNN) : Pred = {sentiment}, Act = {'P' if y_test[i] == 1 else 'N'}")

test_data = [
    {"vector_dimensional": 32, "layers_count"  :32, "epochs" :5, "batch_size" :64},
    {"vector_dimensional": 64, "layers_count"  :32, "epochs" :5, "batch_size" :64},
    {"vector_dimensional": 128, "layers_count" :32, "epochs" :5, "batch_size" :64},

    {"vector_dimensional": 32, "layers_count"  :32, "epochs" :5, "batch_size" :64},
    {"vector_dimensional": 64, "layers_count"  :64, "epochs" :5, "batch_size" :64},
    {"vector_dimensional": 128, "layers_count" :128, "epochs" :5, "batch_size" :64},

    {"vector_dimensional": 32, "layers_count"  :32, "epochs" :10, "batch_size" :64},
    {"vector_dimensional": 64, "layers_count"  :64, "epochs" :20, "batch_size" :64},
    {"vector_dimensional": 128, "layers_count" :128, "epochs" :40, "batch_size" :64},

    {"vector_dimensional": 32, "layers_count"  :32, "epochs" :50, "batch_size" :64},
    {"vector_dimensional": 64, "layers_count"  :64, "epochs" :100, "batch_size" :64},
    {"vector_dimensional": 128, "layers_count" :128, "epochs" :200, "batch_size" :64},
]

def main():
    for i, data in enumerate(test_data, 1):
        tstr = f"{i}. vector_dime :{data['vector_dimensional']}, layers_count :{data['layers_count']}, epochs :{data['epochs']}, batch_size :{data['batch_size']}"
        print(tstr)
        
        init_data()
        rnn03_imdb_reviews(i, data["vector_dimensional"], data["layers_count"], data["epochs"], data["batch_size"])

if __name__ == "__main__":
    main()
    
