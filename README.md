# 🎥 YouTube Transcript to Advanced Notes Converter Generative AI

This project is a **Streamlit web application** that converts YouTube video transcripts into **detailed summarized notes** with **key points** using AI models like **Google Gemini**. The application provides users with a way to quickly generate a concise summary of YouTube videos and download the transcript.

## Features

- **Convert YouTube Video Transcripts**: Extract video transcripts directly using the video URL.
- **Summarize Transcripts with AI**: Leverage the power of Google Gemini models to summarize transcripts.
- **Customizable Summary Length**: Choose from short (100 words), medium (250 words), or long (500 words) summaries.
- **Highlight Key Points**: Select how many key points to include in the summary.
- **User-Friendly Interface**: Designed with an intuitive sidebar for inputs and real-time summarization results.
- **Video Thumbnail Preview**: Visual confirmation of the video through its thumbnail.
- **Downloadable Transcripts**: Save the full video transcript as a `.txt` file.

## Tech Stack

- **Streamlit**: For building the web application interface.
- **Google Gemini AI**: Used for summarizing the video transcript.
- **YouTubeTranscriptAPI**: For fetching video transcripts directly from YouTube.
- **Python**: Main programming language.

### 1. **Input YouTube Video Link**
   - Enter the full URL of the YouTube video in the provided input field in the sidebar.

### 2. **Select Summary Options**
   - Choose the desired summary length (short, medium, long).
   - Set the number of key points to extract from the video.

### 3. **Generate Summary**
   - Click the "Generate Detailed Notes" button in the sidebar.
   - The transcript will be extracted, and a summary will be generated and displayed in the main content area.

### 4. **Download Transcript**
   - You can download the full transcript as a `.txt` file by clicking the "Download Transcript" button.

## Project Workflow

1. **YouTube Video Link Input**: User provides the YouTube link.
2. **Thumbnail Display**: The video thumbnail is displayed for confirmation.
3. **Transcript Extraction**: The app retrieves the transcript using `YouTubeTranscriptAPI`.
4. **Prompt Generation**: A prompt is built dynamically based on user settings for summary length and key points.
5. **Summary Generation**: The Google Gemini model generates a summary based on the transcript and prompt.
6. **Display Results**: The summary is shown on the main content page, and the user can download the transcript.

## User Interface Screenshot

![user interface](https://github.com/user-attachments/assets/3167ef3a-4468-4b3e-81ce-2fe70c4f0e54)

1. Enter the YouTube link in the sidebar.
2. Select summary length and key points.
3. Click "Generate Detailed Notes."
4. View and download the results.

## Conclusion

The **YouTube Transcript to Advanced Notes Converter** offers an efficient and user-friendly solution for transforming lengthy YouTube video transcripts into concise, easy-to-read summaries. By integrating the power of **Google Gemini AI** with a sleek **Streamlit** interface, this application allows users to quickly extract key information and insights from any video. The customizable summary length and key points feature makes it versatile for various use cases, from academic research to casual content consumption. Overall, this project streamlines the process of digesting video content, enhancing productivity, and saving time.
