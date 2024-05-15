# Rice Leaf Disease Identification

## Overview
Rice Leaf Disease Identification is a deep learning project aimed at detecting and classifying diseases in rice leaves using computer vision techniques. The project utilizes transfer learning with the ResNet152V2 model, incorporating an attention layer to focus on important parts of the image. The dataset used for training the model contains approximately 2600 images belonging to six different classes.
## Dataset
The dataset used for training the model is sourced from Kaggle and contains images of rice leaves affected by different diseases. You can access the dataset [here](https://www.kaggle.com/datasets/dedeikhsandwisaputra/rice-leafs-disease-dataset).

## Model Training
The deep learning model is trained using transfer learning techniques with the ResNet152V2 architecture. Transfer learning allows leveraging pre-trained models on large datasets and fine-tuning them for specific tasks. In this project, the ResNet152V2 model is fine-tuned on the rice leaf disease dataset to classify different types of diseases.

## Classes
The model is trained to classify rice leaf images into the following disease classes:
- Healthy
- Brown spot
- Leaf blast
- Bacterial leaf blight
- Leaf scald
- Narrow brown spot

## Deployment
The trained model is deployed using Flask, a lightweight Python web framework. It accepts images of rice leaves as input and identifies the disease present in the leaf.

## Usage
To use the deployed model:
1. Clone the repository.
2. Install the required dependencies specified in the `requirements.txt` file.
3. Run the Flask application.
4. Upload an image of a rice leaf to the application.
5. The application will predict the disease present in the leaf and display the result.

## Contributors
- [Umang Rathi](https://github.com/umangrathi110)


