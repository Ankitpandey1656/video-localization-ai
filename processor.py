import yt_dlp
import os
import sys
import datetime
from faster_whisper import WhisperModel
from deep_translator import GoogleTranslator
from gtts import gTTS


def process_video(url, mode):
    timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")

    # Generate unique filenames for the current processing job.
    base_name = f"job_{timestamp}"
    eng_file = f"{base_name}_english.txt"
    hindi_file = f"{base_name}_hindi.txt"
    audio_file = f"{base_name}_hindi_audio.mp3"

    # Download the audio stream from the provided YouTube video.
    print("INFO: Downloading audio...")

    ydl_opts = {
        "format": "bestaudio/best",
        "postprocessors": [
            {
                "key": "FFmpegExtractAudio",
                "preferredcodec": "mp3"
            }
        ],
        "outtmpl": "input_audio"
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])

    # Generate the English transcript using the Whisper model.
    print("INFO: Generating English transcript...")

    model = WhisperModel("tiny", device="cpu", compute_type="int8")
    segments, _ = model.transcribe("input_audio.mp3")
    eng_text = " ".join([segment.text for segment in segments])

    # Save the generated English transcript.
    with open(eng_file, "w", encoding="utf-8") as file:
        file.write(eng_text)

    # Translate the transcript and generate Hindi audio if requested.
    if mode == "Full":
        print("INFO: Translating to Hindi...")

        hindi_text = GoogleTranslator(
            source="en",
            target="hi"
        ).translate(eng_text)

        # Save the translated Hindi transcript.
        with open(hindi_file, "w", encoding="utf-8") as file:
            file.write(hindi_text)

        # Convert the translated text into Hindi speech.
        print("INFO: Generating Hindi audio...")

        tts = gTTS(text=hindi_text, lang="hi")
        tts.save(audio_file)

    print("INFO: Processing completed successfully.")


if __name__ == "__main__":
    process_video(sys.argv[1], sys.argv[2])