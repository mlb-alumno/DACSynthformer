#!/usr/bin/env python3
import os
import argparse
from pydub import AudioSegment

def convert_to_mono(input_folder, output_folder):
    # Create output folder if it doesn't exist
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)
        print(f"Created output folder: {output_folder}")

    # Loop through all files in the input folder
    for filename in os.listdir(input_folder):
        # Process only .wav files
        if filename.lower().endswith('.wav'):
            input_path = os.path.join(input_folder, filename)
            output_path = os.path.join(output_folder, filename)
            try:
                # Load the audio file
                audio = AudioSegment.from_wav(input_path)
                # Convert to mono if necessary
                if audio.channels != 1:
                    audio = audio.set_channels(1)
                # Export the mono audio file
                audio.export(output_path, format="wav")
                print(f"Converted and saved: {filename}")
            except Exception as e:
                print(f"Error processing {filename}: {e}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Convert all .wav files in a folder to mono and save to another folder."
    )
    parser.add_argument(
        "input_folder", help="Path to the folder containing .wav files to convert"
    )
    parser.add_argument(
        "output_folder", help="Path to the folder where mono .wav files will be saved"
    )
    args = parser.parse_args()
    convert_to_mono(args.input_folder, args.output_folder)
