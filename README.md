# Rice Image Classification with CNN

A Convolutional Neural Network that classifies five different rice grain varieties from images, with a Streamlit web application for real-time predictions — supporting agricultural quality control and food production consistency.

---

## English

### About

This project implements a CNN model to distinguish between five rice varieties: Arborio, Basmati, Ipsala, Jasmine, and Karacadag. Using ~75,000 high-resolution images from Kaggle, the model is trained to identify subtle visual differences between grain types. The project includes a Jupyter training notebook and a Streamlit web app for user-friendly predictions.

### Features

- 5-class image classification (Arborio, Basmati, Ipsala, Jasmine, Karacadag)
- ~85–90% validation accuracy
- Streamlit web app for real-time predictions from uploaded images
- Supports agricultural quality control use cases

### Dataset

**Source:** [Rice Image Dataset — Kaggle](https://www.kaggle.com/datasets/muratkokludataset/rice-image-dataset)

| Property | Detail |
|---|---|
| Total Images | ~75,000 |
| Classes | 5 |
| Image Format | RGB, high-resolution |
| Input Size (model) | 64 × 64 px (resized & normalized) |

### Model Architecture

```
Input (64, 64, 3)
→ Conv2D (ReLU) → MaxPooling2D
→ Conv2D (ReLU) → MaxPooling2D
→ Flatten
→ Dense (ReLU)
→ Dense (5, softmax)
```

**Training Details:**

| Parameter | Value |
|---|---|
| Epochs | 10 |
| Optimizer | Adam |
| Loss | Sparse Categorical Crossentropy |
| Validation Accuracy | ~85–90% |

Saved model: `my_rice_cnn_model.h5`

### How to Run

**Training the model:**
```bash
git clone https://github.com/MMertAvc/rice-image-classification.git
cd rice-image-classification
pip install -r requirements.txt
```

1. Place the `Rice_Image_Dataset/` folder in the project root
2. Open `Rice Classification.ipynb` in Jupyter Notebook
3. Run all cells — this saves `my_rice_cnn_model.h5`

**Running the web app:**
```bash
streamlit run app.py
```
Upload a rice image (JPG/PNG) via the web interface to view the predicted variety.

### Project Structure

```
├── Rice Classification.ipynb       # Training notebook
├── app.py                          # Streamlit web application
├── my_rice_cnn_model.h5            # Trained model weights
├── requirements.txt
└── README.md
```

### Requirements

```
tensorflow
keras
opencv-python
streamlit
pillow
pandas
numpy
matplotlib
scikit-learn
```

---

## Türkçe

### Hakkında

Bu proje, beş farklı pirinç çeşidini görüntülerden ayırt eden bir CNN modeli uygular: Arborio, Basmati, Ipsala, Jasmine ve Karacadag. Kaggle'dan ~75.000 yüksek çözünürlüklü görüntü kullanan model, tane türleri arasındaki ince görsel farklılıkları tanımlamak için eğitilir. Proje, bir Jupyter eğitim not defteri ve kullanıcı dostu tahminler için bir Streamlit web uygulaması içerir.

### Özellikler

- 5 sınıflı görüntü sınıflandırması (Arborio, Basmati, Ipsala, Jasmine, Karacadag)
- ~%85–90 doğrulama doğruluğu
- Yüklenen görüntülerden gerçek zamanlı tahminler için Streamlit web uygulaması
- Tarımsal kalite kontrol kullanım senaryolarını destekler

### Veri Seti

**Kaynak:** [Pirinç Görüntü Veri Seti — Kaggle](https://www.kaggle.com/datasets/muratkokludataset/rice-image-dataset)

| Özellik | Detay |
|---|---|
| Toplam Görüntü | ~75.000 |
| Sınıf Sayısı | 5 |
| Görüntü Formatı | RGB, yüksek çözünürlük |
| Giriş Boyutu (model) | 64 × 64 piksel (yeniden boyutlandırılmış ve normalize edilmiş) |

### Model Mimarisi

```
Giriş (64, 64, 3)
→ Conv2D (ReLU) → MaxPooling2D
→ Conv2D (ReLU) → MaxPooling2D
→ Flatten
→ Dense (ReLU)
→ Dense (5, softmax)
```

**Eğitim Detayları:**

| Parametre | Değer |
|---|---|
| Epoch Sayısı | 10 |
| Optimizör | Adam |
| Kayıp | Seyrek Kategorik Çapraz Entropi |
| Doğrulama Doğruluğu | ~%85–90 |

Kaydedilen model: `my_rice_cnn_model.h5`

### Nasıl Çalıştırılır

**Modeli eğitmek için:**
```bash
git clone https://github.com/MMertAvc/rice-image-classification.git
cd rice-image-classification
pip install -r requirements.txt
```

1. `Rice_Image_Dataset/` klasörünü proje köküne yerleştirin
2. Jupyter Notebook'ta `Rice Classification.ipynb` dosyasını açın
3. Tüm hücreleri çalıştırın — bu, `my_rice_cnn_model.h5` dosyasını kaydeder

**Web uygulamasını çalıştırmak için:**
```bash
streamlit run app.py
```
Tahmin edilen çeşidi görüntülemek için web arayüzü üzerinden bir pirinç görüntüsü (JPG/PNG) yükleyin.

### Proje Yapısı

```
├── Rice Classification.ipynb       # Eğitim not defteri
├── app.py                          # Streamlit web uygulaması
├── my_rice_cnn_model.h5            # Eğitilmiş model ağırlıkları
├── requirements.txt
└── README.md
```

### Gereksinimler

```
tensorflow
keras
opencv-python
streamlit
pillow
pandas
numpy
matplotlib
scikit-learn
```
