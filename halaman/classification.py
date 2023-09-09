import streamlit as st
import pandas as pd
import time

def app() :
    from sklearn.model_selection import train_test_split
    from sklearn.preprocessing import LabelEncoder

    #penambahan upload_TF_IDF
    data = pd.read_csv('data/main_data.csv')
    data_encoder = pd.read_csv('data/main_data.csv')
    feature = pd.read_csv('data/meta/feature_data.csv')
    data_encoder[list(feature['column'])] = data_encoder[list(feature['column'])].apply(LabelEncoder().fit_transform)
    label = pd.read_csv('data/meta/label_data.csv')
    test_size = pd.read_csv('data/meta/test_size.csv')

    # ## pembagian data test dengan data secara otomatis
    st.subheader('Klasifikasi')
    from sklearn.metrics import accuracy_score, confusion_matrix
    from sklearn.naive_bayes import MultinomialNB
    from mlxtend.plotting import plot_confusion_matrix
    X_train, X_test, y_train, y_test = train_test_split(data_encoder[list(feature['column'])], data_encoder[str(label['label'][0]).strip()], test_size = test_size['test size'][0],random_state=1221)
    
    modelnb = MultinomialNB()
    nbtrain = modelnb.fit(X_train, y_train)
    y_pred = nbtrain.predict(X_test)
    accuracy = accuracy_score(y_test,y_pred)
    c_matrik = confusion_matrix(y_test,y_pred)
    column = st.multiselect('Pilih kolom yang akan di digunakan, kecuali kolom label',
                list(data_encoder.columns), list(feature['column'])
                )
    data_pred = pd.DataFrame({'Predsi Kelas':y_pred,'Kelas Sesunggunya':y_test})
    data_pred = (data_pred.join(data[column]))
    st.write(data_pred)
    st.write(f'akurasi yang didapatkan yaitu : {round(accuracy,3)}')
    fig, ax = plot_confusion_matrix(conf_mat=c_matrik,class_names=nbtrain.classes_)
    ax.set_title('Confusion Matrik')
    ax.set_ylabel('Actual Label')
    ax.set_xlabel('Predicted Label')
    st.pyplot(fig)
