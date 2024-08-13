# Face Mask Detection By CNN

This project is a Streamlit web application that detects whether a person is wearing a face mask using a Convolutional Neural Network (CNN). The application offers three options for input: uploading an image, entering an image URL, or capturing a live image using a webcam.

## Features

- **Image Upload**: Upload an image from your device, and the app will classify whether the person in the image is wearing a mask or not.
- **URL Input**: Enter the URL of an image, and the app will fetch and classify the image.
- **Live Image Capture**: Capture a live image from your webcam and classify it.

## Installation

1. **Clone the repository:**

    ```bash
    git clone https://github.com/alihassanml/Face-mask-detection-By-CNN.git
    ```

2. **Navigate to the project directory:**

    ```bash
    cd Face-mask-detection-By-CNN
    ```

3. **Create a virtual environment (optional but recommended):**

    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

4. **Install the required packages:**

    ```bash
    pip install -r requirements.txt
    ```

## Usage

1. **Run the Streamlit application:**

    ```bash
    streamlit run your_app.py
    ```

2. **Open your web browser and go to the URL provided by Streamlit (usually http://localhost:8501).**

3. **Select the input method from the sidebar:**
   - **Image Upload**: Upload an image file.
   - **URL Input**: Enter the URL of an image.
   - **Live Image Capture**: Capture an image from your webcam.

## Requirements

- Python 3.x
- TensorFlow
- OpenCV
- Pillow
- Requests
- Streamlit
- NumPy

You can find the `requirements.txt` file in the repository to install all dependencies.

## Contact

- **LinkedIn**: [Ali Hassan](https://www.linkedin.com/in/alihassanml)
- **GitHub**: [alihassanml](https://github.com/alihassanml)

**Developed by**: Ali Hassan
