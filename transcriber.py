import openai
from pydub import AudioSegment
import os

# Set your API key
openai.api_key = "enter your api key"

# Load audio file
audio_file_path = "path to your file"
audio = AudioSegment.from_file(audio_file_path)

# Set chunk duration in milliseconds (e.g., 120 seconds)
chunk_duration_ms = 120 * 1000  # 120 seconds

# Split the audio into chunks
chunks = [audio[i:i + chunk_duration_ms] for i in range(0, len(audio), chunk_duration_ms)]

# Create or clear the transcription file
with open("transcription.txt", "w") as f:
    f.write("")  # Clear existing content

# Process each chunk
for i, chunk in enumerate(chunks):
    # Save the chunk as a temporary WAV file
    chunk_path = f"chunk_{i}.wav"
    chunk.export(chunk_path, format="wav")

    # Load the chunk for transcription
    with open(chunk_path, "rb") as audio_chunk:
        # Transcribe the audio chunk using the Whisper model
        transcription = openai.Audio.transcribe(
            model="whisper-1",
            file=audio_chunk
        )

    # Append the transcribed text to the file
    with open("transcription.txt", "a") as f:
        f.write(transcription["text"] + "\n")

    # Remove the temporary chunk file
    os.remove(chunk_path)

print("Transcription completed and saved to 'transcription.txt'.")
