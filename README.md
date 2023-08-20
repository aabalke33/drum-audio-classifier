# drum-audio-classifier
Classify Drum audio samples through the use of Artifical Intelligence / Machine Learning.

The Drum Audio Classifier, uses a Convolutional Neural Network to predict the most likely drum type of a audio file. The dataset used to create this model was 2,700+ of my freelance music production audio samples.     

## Advantages
The advatange of a CNN model for audio classification is that the model works with spacial transformations and when dimensional data is offset. This means the shape of the audio data over time and frequency is modelled, not the exact locations. If a "Kick Drum" audio sample is higher pitches than the modelled samples, it will still register as a Kick Drum. If a "Snare Drum" sample doesn't strike until 2-3 seconds in, it will still register as a Snare Drum.

<img src="https://github.com/aabalke33/drum-audio-classifier/assets/22086435/3767d05c-bc95-4a09-8cc1-948082ac1fa2" width="50%">

## Youtube Video Breakdown

[<img src="https://github-production-user-asset-6210df.s3.amazonaws.com/22086435/248511694-40649f81-b0ae-4cde-8a3e-72bfa75b7805.jpg" width="50%">](https://www.youtube.com/watch?v=4DkwWLhBtOo)

## Usage
### Cloud Demo
![shot](https://github.com/aabalke33/drum-audio-classifier/assets/22086435/2f75f4ba-969e-4436-8f81-e639c6307ce3)

[A streamlit demo is available on Huggingface Spaces.](https://balkite-drum-classifier.hf.space) You may test your own drum samples, or use the samples provided on streamlit.

### Locally
Dependencies: Python 3.10, matplotlib 3.7.0, pandas 1.5.3, librosa 0.10.0, sklearn 0.0, numpy 1.23.5, tensorflow 2.10.0, IPython 8.10.0

I would suggest using Jupyter Notebooks and following the Cloud Demo Steps.

## Important Considerations
1. The saved model only classifies: Kick Drum, Snare Drum, Closed Hat Cymbal, Open Hat Cymabl and Clap Drum sample.
2. The saved model has a Validation Loss of 5.00+. This implies overfitting and that the saved model is "memorizing" patterns. In practice I did not see problems with classifying samples; however, you mileage may vary.
![Figure](https://github.com/aabalke33/drum-audio-classifier/blob/main/documentation/task2/graphs/graph_3_1.png)

## Dataset
The raw dataset is directly from H3 Music Corp, consisting of 2,746 drum audio samples with a CSV File associating the file with a drum type classification. These files were provided and maintained in Uncompressed WAV file formats. The reasoning for this is for development and post-development it is easier for users and developers to verify and interact with audio files rather than arrays. If a developer needs to verify the type of drum sample, they can just listen to it, removing a lot of hassle. The raw Uncompressed WAV Files are available in the dataset/samples folder. The CSV File to associate types is available in the dataset folder, titled “samples_metadata.csv”. The "drum_prediction.ipynb" file converts the WAV files into arrays of Amplification at Pitches (0 - 128) over Time.

It is important to note that CNNs are intended to use image data not audio data. To remedy this audio amplification data has to be duplicatd across all 3 color channels (rgb). This makes the CNN "think" it is looking at a color image. Instead of height and width dimensions, the model uses pitch and time as the dimensions.
![cnndata](https://github.com/aabalke33/drum-audio-classifier/assets/22086435/c9003944-97ca-46a1-b26a-b5b686b9ce84)

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
