import moviepy.editor as mp
import speech_recognition as sr
from transformers import BartTokenizer, BartForConditionalGeneration

def extract_audio(video_path, output_path):
    video_clip = mp.VideoFileClip(video_path)
    audio_clip = video_clip.audio
    audio_clip.write_audiofile(output_path)
    audio_clip.close()
    video_clip.close()

def convert_audio_to_text(audio_path):
    recognizer = sr.Recognizer()
    with sr.AudioFile(audio_path) as source:
        audio_data = recognizer.record(source)
        text = recognizer.recognize_google(audio_data)
    return text

def summarize_text(summ_text):
    tokenizer = BartTokenizer.from_pretrained('facebook/bart-large-cnn')
    model = BartForConditionalGeneration.from_pretrained('facebook/bart-large-cnn')
    inputs = tokenizer([summ_text], max_length=1024, return_tensors='pt')
    summary_ids = model.generate(inputs['input_ids'], num_beams=4, max_length=100, early_stopping=True)
    summary = tokenizer.decode(summary_ids[0], skip_special_tokens=True)
    return summary

def starter():
    video_path = input("Hello, type the path of the video you want to summarize:\n")
    audio_path = "extracted_audio.wav"  # Temporary file path for the extracted audio

    # Extract audio from the video
    extract_audio(video_path, audio_path)

    # Convert extracted audio to text
    text = convert_audio_to_text(audio_path)

    # Summarize the extracted text
    summary = summarize_text(text)
    print(summary)

starter()
