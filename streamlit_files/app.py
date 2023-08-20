import streamlit as st
import numpy as np

from backend import sample_preparer, load_model


def process_file(file, model):
    prediction = model.predict(np.array(sample_preparer(file)))

    type_num = np.argmax(prediction, axis=1)

    drum_types = ['Clap', 'Closed Hat', 'Kick', 'Open Hat', 'Snare']

    return drum_types[int(type_num)]


def main_page():
    st.set_page_config(page_title="Drum Classifier",
                       page_icon="🥁")

    st.markdown("# Drum Classifier 🥁")
    st.markdown("Classify Drum audio samples through the use of Artificial Intelligence / Machine Learning. The Drum "
                "Audio Classifier, uses a Convolutional Neural Network to predict the most likely drum type of a "
                "audio file. The dataset used to create this model was 2,700+ of my freelance music production audio "
                "samples.")
    st.markdown("Currently supported drums: Clap, Closed Hat, Kick, Open Hat, Snare.")
    st.markdown("Drag and Drop a WAV or Mp3 audio File to classify.")

    if "model" not in st.session_state:
        with st.spinner("Loading Database..."):
            st.session_state.model = load_model()

    with open("samples.zip", "rb") as file:
        st.download_button(
            label="Download Sample Files",
            data=file,
            file_name="samples.zip",
            mime="application/zip"
        )

    file = st.file_uploader(
        "Upload an Audio File",
        accept_multiple_files=False,
        type=['wav', 'mp3'],
        label_visibility="hidden"
    )

    if st.session_state.model and file:
        st.audio(file)

        with st.spinner("Processing..."):
            drum_type = process_file(file, st.session_state.model)

        st.markdown(f"\"{file.name}\" is a {drum_type}.")


if __name__ == '__main__':
    main_page()
