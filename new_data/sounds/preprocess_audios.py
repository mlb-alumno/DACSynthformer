import os
from pydub import AudioSegment

def process_audio(input_folder, output_folder, target_duration=5000):
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)
    
    for filename in os.listdir(input_folder):
        if filename.endswith(".wav"):
            filepath = os.path.join(input_folder, filename)
            audio = AudioSegment.from_wav(filepath)
            
            # Convert to mono
            audio = audio.set_channels(1)
            
           
            
            # Trim or pad to exactly 5 seconds
            if len(audio) > target_duration:
                audio = audio[:target_duration]
            else:
                silence = AudioSegment.silent(duration=target_duration - len(audio))
                audio = audio + silence
            
            # Export processed audio
            output_path = os.path.join(output_folder, filename)
            audio.export(output_path, format="wav")
            print(f"Processed: {filename}")

# Example usage
input_folder = "new_birds"
output_folder = "new_audios_clean"
process_audio(input_folder, output_folder)
