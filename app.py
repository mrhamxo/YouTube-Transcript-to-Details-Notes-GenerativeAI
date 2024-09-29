import streamlit as st
from dotenv import load_dotenv
import os
import google.generativeai as genai
from youtube_transcript_api import YouTubeTranscriptApi
import time  # Import time for sleep functionality

# Load environment variables
load_dotenv()

# Configure Google Gemini API
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# Advanced Streamlit app for YouTube transcript summary
st.set_page_config(page_title="YouTube to Detailed Notes", page_icon="🎥", layout="wide")

# Sidebar - Input fields and settings
st.sidebar.title("YouTube Transcript to Advanced Notes 🎥")
st.sidebar.write("Convert YouTube video transcripts into summarized notes with key points using AI.")

# YouTube link input in the sidebar
youtube_link = st.sidebar.text_input("Enter YouTube Video Link:")

# Summary length option
summary_length = st.sidebar.selectbox("Select Summary Length:", ["Short (100 words)", "Medium (250 words)", "Long (500 words)"])

# Key points slider
key_points = st.sidebar.slider("Number of Key Points:", min_value=3, max_value=10, value=5)

# Generate Notes button in the sidebar
generate_notes = st.sidebar.button("Generate Detailed Notes")

# Prompt configuration
def build_prompt(summary_length, key_points):
    length_map = {
        "Short (100 words)": 100,
        "Medium (250 words)": 250,
        "Long (500 words)": 500,
    }
    prompt = f"""
    You are a YouTube video summarizer. You will take the transcript text and summarize the entire video.
    Provide a summary in {length_map[summary_length]} words, emphasizing the most important details. 
    List the key points in {key_points} bullet points.
    Here is the transcript: 
    """
    return prompt

# Extract YouTube video transcript
def extract_transcript_details(youtube_video_url):
    try:
        video_id = youtube_video_url.split("=")[1]
        transcript_text = YouTubeTranscriptApi.get_transcript(video_id)
        transcript = " ".join([i["text"] for i in transcript_text])
        return transcript
    except Exception as e:
        st.error(f"Error extracting transcript: {e}")
        return None

# Generate summary using Google Gemini
def generate_gemini_content(transcript_text, prompt):
    try:
        model = genai.GenerativeModel("gemini-pro")
        response = model.generate_content(prompt + transcript_text)
        return response.text
    except Exception as e:
        st.error(f"Error generating summary: {e}")
        return None

# Main content area for displaying video thumbnail and summary
if youtube_link:
    try:
        # Display video thumbnail on the right bar
        video_id = youtube_link.split("=")[1]
        st.image(f"http://img.youtube.com/vi/{video_id}/0.jpg", width=400)
    except Exception:
        st.error("Invalid YouTube link. Please check and try again.")

# Add progress bar
progress_bar = st.progress(0)

# When the user clicks the "Generate Detailed Notes" button
if generate_notes and youtube_link:
    # Extract transcript
    st.info("Extracting transcript... Please wait.")
    progress_bar.progress(10)

    transcript_text = extract_transcript_details(youtube_link)
    if transcript_text:
        time.sleep(2)
        progress_bar.progress(50)
        
        st.info("Generating summary... Please wait.")
        prompt = build_prompt(summary_length, key_points)
        summary = generate_gemini_content(transcript_text, prompt)

        if summary:
            time.sleep(2)
            progress_bar.progress(100)
            st.success("Summary generated successfully!")

            # Display summary on the right panel
            st.markdown("### Summary:")
            st.write(summary)

            # Option to download transcript
            st.download_button(
                label="Download Transcript",
                data=transcript_text,
                file_name="transcript.txt",
                mime="text/plain"
            )
    else:
        st.error("Failed to retrieve transcript. Please try again.")

# Footer
st.markdown("---")
st.markdown("Developed with ❤️ by Muhammad Hamza Khattak.")
