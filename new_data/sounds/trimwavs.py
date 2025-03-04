import os
from pydub import AudioSegment

# Configuration
input_folder = "./"  # Change to your source folder
output_folder = "copy"  # Change to your destination folder
duration_ms = 5000  # 5 seconds in milliseconds

# Ensure output folder exists
os.makedirs(output_folder, exist_ok=True)

# Process all .wav files
for filename in os.listdir(input_folder):
    if filename.endswith(".wav"):
        input_path = os.path.join(input_folder, filename)
        output_path = os.path.join(output_folder, filename)
        
        # Load audio file
        audio = AudioSegment.from_wav(input_path)
        
        # Trim or pad to 5 seconds
        if len(audio) > duration_ms:
            audio = audio[:duration_ms]
        elif len(audio) < duration_ms:
            silence = AudioSegment.silent(duration=duration_ms - len(audio))
            audio = audio + silence  # Pad with silence
        
        # Export the processed file
        audio.export(output_path, format="wav")
        print(f"Processed: {filename}")

print("Processing complete!")
