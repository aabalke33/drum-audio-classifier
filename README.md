# drum-audio-classifier
Classify Drum audio samples through the use of Artifical Intelligence / Machine Learning.

The Drum Audio Classifier, uses a Convolutional Neural Network to predict the most likely drum type of a audio file. The dataset used to create this model was 2,700+ of my freelance music production audio samples.

## Advantages
The advatange of a CNN model for audio classification is that the model works with spacial transformations and when dimensional data is offset. This means the shape of the audio data over time and frequency is modelled, not the exact locations. If a "Kick Drum" audio sample is higher pitches than the modelled samples, it will still register as a Kick Drum. If a "Snare Drum" sample doesn't strike until 2-3 seconds in, it will still register as a Snare Drum.

## Usage
### Cloud Demo
[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/aabalke33/drum-prediction/HEAD)

This GitHub repository includes the user file “drum_prediction.ipynb”, the file used to build the model “drum_prediction_model.ipynb”, the dataset, the saved model and all documentation related to the assessment. The application has been built and tested with mybinder.org hosting in mind.
To run the application:

1. Click the Launch Binder button. This will create a virtual environment to load the application. This process usually takes 2-5 minutes. If an error occurs please retry, you shouldn’t have to retry more than once. Once this page is loaded, all files related to this submission will be accessible, including the ones used to create the model. As a user, the only required file to access is “drum_prediction.ipynb”.
2. Access drum_prediction.ipynb
3. Run the first Code Block (Ctrl + Enter). This will load all required modules and the saved model. You will get warnings regarding Tensorflow dependencies and build suggestions. These do not affect this program.
4. Run the second Code Block (Ctrl + Enter). This will prompt a file path to classify the file. For demonstration purposes, 5 files have been uploaded to classify. After the file has been loaded, an audio player will load to verify the file chosen. The following paths can be copied in as inputs:

   Clap Sample: dataset/samples_reserved/input_clap.wav

   Closed Hat Sample: dataset/samples_reserved/input_closedhat.wav

   Kick Sample: dataset/samples_reserved/input_kick.wav

   Open Hat Sample: dataset/samples_reserved/input_openhat.wav

   Snare Sample: dataset/samples_reserved/input_snare.wav

5. Run the third Code Block (Ctrl + Enter). This final block of code will run a prediction against the saved model to classify the audio sample inputted. The console will print “Drum Sample is: (drum type)” upon completion.

![Code Block](https://github.com/aabalke33/drum-audio-classifier/assets/22086435/edaba9c2-7c04-4025-952c-d8679032f5cd)
*a correctly executed Code Block 2 and Code Block 3.*

### Locally
Dependencies: Python 3.10, matplotlib 3.7.0, pandas 1.5.3, librosa 0.10.0, sklearn 0.0, numpy 1.23.5, tensorflow 2.10.0, IPython 8.10.0

I would suggest using Jupyter Notebooks and following the Cloud Demo Steps.

## Important Considerations
1. The saved model only classifies: Kick Drum, Snare Drum, Closed Hat Cymbal, Open Hat Cymabl and Clap Drum sample.
2. The saved model has a Validation Loss of 5.00+. This implies overfitting and that the saved model is "memorizing" patterns. In practice I did not see problems with classifying samples; however, you mileage may vary.
![Figure](https://github.com/aabalke33/drum-audio-classifier/blob/main/documentation/task2/graphs/graph_3_1.png)

## Dataset
The reasoning for this is for development and post-development it is easier for users and developers to verify and interact with audio files rather than arrays. If a developer needs to verify the type of drum sample, they can just listen to it, removing a lot of hassle. The raw Uncompressed WAV Files are available in the dataset/samples folder. The CSV File to associate types is available in the dataset folder, titled “samples_metadata.csv”. The "drum_prediction.ipynb" file converts the WAV files into arrays of Amplification at Pitches (0 - 128) over Time.

### Waveforms of the First Sample for Each Type in Dataset
![Figure](https://github.com/aabalke33/drum-audio-classifier/blob/main/documentation/task2/graphs/graph_1_1.png)
![Figure](https://github.com/aabalke33/drum-audio-classifier/blob/main/documentation/task2/graphs/graph_1_2.png)
![Figure](https://github.com/aabalke33/drum-audio-classifier/blob/main/documentation/task2/graphs/graph_1_3.png)
![Figure](https://github.com/aabalke33/drum-audio-classifier/blob/main/documentation/task2/graphs/graph_1_4.png)
![Figure](https://github.com/aabalke33/drum-audio-classifier/blob/main/documentation/task2/graphs/graph_1_5.png)

### Spectrograms for all samples, organized by Type
![Figure](https://github.com/aabalke33/drum-audio-classifier/blob/main/documentation/task2/graphs/graph_2_1.png)
![Figure](https://github.com/aabalke33/drum-audio-classifier/blob/main/documentation/task2/graphs/graph_2_2.png)
![Figure](https://github.com/aabalke33/drum-audio-classifier/blob/main/documentation/task2/graphs/graph_2_3.png)
![Figure](https://github.com/aabalke33/drum-audio-classifier/blob/main/documentation/task2/graphs/graph_2_4.png)
![Figure](https://github.com/aabalke33/drum-audio-classifier/blob/main/documentation/task2/graphs/graph_2_5.png)

## Credits
Massive thank you to Dr. Papia Nandi and her work on [CNNs for Audio Classification](https://towardsdatascience.com/cnns-for-audio-classification-6244954665ab).
