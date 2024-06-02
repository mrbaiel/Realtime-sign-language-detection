Real-Time Sign Language Detection

This project aims to detect and translate sign language gestures into text in real-time using a camera.
Table of Contents

    Introduction
    Features
    Installation
    Usage
    Dataset
    Model Training
    Real-Time Detection
    Contributing
    License

Introduction

Real-Time Sign Language Detection is a project that captures video input from a camera, processes the frames, and uses a machine learning model to recognize sign language gestures. The recognized gestures are then translated into text, which is displayed to the user.
Features

    Real-time video capture and processing
    Machine learning model for gesture recognition
    Translation of recognized gestures into text
    Easy to use interface

Installation

    Clone the repository:

    bash

git clone https://github.com/mrbaiel/Realtime-sign-language-detection.git
cd Realtime-sign-language-detection

Create a virtual environment:

bash

python -m venv env
source env/bin/activate  # On Windows use `env\Scripts\activate`

Install the required dependencies:

bash

    pip install -r requirements.txt

Usage

    Ensure your camera is connected and working.
    Run the real-time detection script:

    bash

    python realtime_detection.py

Dataset

The dataset used for training the model should contain labeled images or videos of sign language gestures. You can use publicly available datasets like ASL (American Sign Language) or create your own.
Model Training

To train the model, follow these steps:

    Prepare your dataset and ensure it is properly labeled.
    Train the model using the train_model.py script:

    bash

    python train_model.py

    Save the trained model to use it in the real-time detection script.

Real-Time Detection

The realtime_detection.py script captures video from your camera, processes the frames, and uses the trained model to recognize and translate gestures into text.

python

python realtime_detection.py

Contributing

Contributions are welcome! Please open an issue or submit a pull request.
