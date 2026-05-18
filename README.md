# Rice Classification with CNN

## Overview
This project implements a Convolutional Neural Network (CNN) model to classify five different types of rice grains: Arborio, Basmati, Ipsala, Jasmine, and Karacadag. Using deep learning techniques, the model analyzes high-resolution rice images to distinguish varieties, supporting agricultural quality control and food production consistency.

The project includes:
- A Jupyter Notebook for data preprocessing, model training, and evaluation
- A trained CNN model saved in HDF5 format
- A Streamlit web application for real-time rice classification from uploaded images

## Dataset
The dataset is sourced from the Rice Image Dataset on Kaggle, containing high-resolution images of five rice varieties captured under controlled conditions. Images are resized to 64x64 pixels and normalized for model input.

- **Classes:** Arborio, Basmati, Ipsala, Jasmine, Karacadag
- **Total Images:** ~75,000 (varies by class)
- **Image Format:** RGB, high-resolution

## Technologies Used
- **Python** for scripting and data processing
- **TensorFlow/Keras** for building and training the CNN model
- **OpenCV** for image preprocessing
- **Pandas & NumPy** for data manipulation
- **Matplotlib** for visualization
- **Scikit-learn** for data splitting
- **Streamlit** for the web application interface
- **PIL** for image handling

## Model Architecture
The CNN model consists of:
- Input layer: 64x64x3 images
- Convolutional layers with ReLU activation and max pooling
- Flatten layer
- Dense layers with softmax output for 5-class classification

**Training Results:**
- Epochs: 10
- Optimizer: Adam
- Loss: Sparse Categorical Crossentropy
- Metrics: Accuracy
- Validation Accuracy: ~85-90% (approximate, run evaluation for exact figures)

## How to Run

### Prerequisites
- Python 3.8+
- Install dependencies: `pip install -r requirements.txt`

### Training the Model
1. Clone the repository.
2. Ensure the `Rice_Image_Dataset/` folder is in the root directory.
3. Open `Rice Classification.ipynb` in Jupyter Notebook.
4. Run all cells to preprocess data, train the model, and save `my_rice_cnn_model.h5`.

### Running the Web App
1. After training, run: `streamlit run app.py`
2. Upload a rice image (JPG/PNG) via the web interface.
3. View the predicted rice variety.

### Model Evaluation
- Use the notebook to evaluate on test data.
- Metrics include accuracy, precision, and recall per class.

## Future Improvements
- Add data augmentation for better generalization
- Implement transfer learning with pre-trained models (e.g., ResNet)
- Deploy the app on cloud platforms (Heroku, AWS)
- Add more rice varieties or multi-class extensions

## License
This project is open-source under the MIT License.

## Acknowledgments
- Dataset: Rice Image Dataset from Kaggle
- Inspired by agricultural AI applications