# YouTube AI Assistant

An AI-powered application that downloads audio from YouTube videos, generates English transcripts using Faster-Whisper, and optionally translates them into Hindi with Hindi speech generation.

This project is built using Python and Streamlit, providing a simple interface for processing YouTube videos locally.

---

## Features

* Download audio from YouTube videos.
* Generate accurate English transcripts using Faster-Whisper.
* Translate English transcripts into Hindi.
* Generate Hindi speech using Google Text-to-Speech (gTTS).
* Simple and responsive Streamlit-based web interface.
* Built-in processing history with download and delete functionality.
* Runs locally on your machine.

---

## Workflow

```text
YouTube URL
      │
      ▼
yt-dlp
      │
      ▼
Audio Download
      │
      ▼
Faster-Whisper
      │
      ▼
English Transcript
      │
      ▼
Google Translator
      │
      ▼
Hindi Transcript
      │
      ▼
gTTS
      │
      ▼
Hindi Audio
```

---

## Tech Stack

* Python
* Streamlit
* yt-dlp
* Faster-Whisper
* Google Translator (deep-translator)
* gTTS
* FFmpeg

---

## Prerequisites

Before running the application, make sure the following are installed:

* Python 3.9 or later
* FFmpeg

### Install FFmpeg

**Windows**

1. Download FFmpeg.
2. Extract the archive.
3. Add the `bin` folder to your system PATH.

**macOS**

```bash
brew install ffmpeg
```

**Ubuntu / Debian**

```bash
sudo apt install ffmpeg
```

---

## Installation

Clone the repository:

```bash
git clone https://github.com/your-username/youtube-video-localizer.git
cd youtube-video-localizer
```

Install the required dependencies:

```bash
pip install -r requirements.txt
```

---

## Run the Application

Start the Streamlit application:

```bash
streamlit run app.py
```

Open the URL displayed in your terminal (usually `http://localhost:8501`).

---

## Usage

1. Paste a YouTube video URL.
2. Select one of the following modes:

   * Transcript Only
   * Transcript + Hindi Audio
3. Click **Start Processing**.
4. Wait until processing is complete.
5. Download the generated transcript or Hindi audio from the sidebar.

---

## Project Structure

```
youtube-video-localizer/
│
├── app.py
├── processor.py
├── requirements.txt
├── README.md
├── .gitignore
├── LICENSE
└── assets/
```

---

## Output Files

The application automatically generates timestamp-based output files such as:

* `job_<timestamp>_english.txt`
* `job_<timestamp>_hindi.txt`
* `job_<timestamp>_hindi_audio.mp3`

These files can be downloaded or deleted directly from the application's sidebar.

---

## Known Limitations

* Translation requires an active internet connection.
* Hindi speech generation uses Google Text-to-Speech (gTTS).
* Processing speed depends on your system hardware.
* Some YouTube videos may not be supported because of platform restrictions or unavailable transcripts.

---

## Future Improvements

* Support for multiple languages
* Subtitle (.srt) generation
* AI-powered video summarization
* Speaker diarization
* GPU acceleration
* Docker support

---

## Contributing

Contributions, suggestions, and feature requests are welcome. Feel free to fork the repository and submit a pull request.

---

## License

This project is licensed under the MIT License.

---

Built with Python, Streamlit, Faster-Whisper, yt-dlp, Google Translator, gTTS, and FFmpeg.


Note:
FFmpeg must be installed separately and added to your system PATH.
It is not installed through requirements.txt.