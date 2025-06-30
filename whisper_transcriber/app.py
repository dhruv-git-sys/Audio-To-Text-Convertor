import os
import whisper
from fpdf import FPDF

def transcribe_audio(audio_path):
    model=whisper.load_model("tiny")
    print("Transcribing audio...")
    result=model.transcribe(audio_path)
    return result['text']

def save_as_txt(text,filename='transcription.txt'):
    with open(filename,'w',encoding="utf-8") as f:
        f.write(text)
    print(f"[SAVED] Transcript saved as {filename}")

def save_as_pdf(text,filename='transcript.pdf'):
    pdf=FPDF()
    pdf.add_page()
    pdf.set_auto_page_break(auto=True,margin=15)
    pdf.set_font("Arial",size=12)
    lines=text.split("\n")
    for line in lines:
        pdf.nulti_cell(0,10,line)
    pdf.output(filename)
    print(f"[SAVED] Transcript saved as {filename}")

if __name__ == "__main__":
    path="sample.mp3"

    if not os.path.exists(path):
        print(f"File {path} does not exist.")
    else:
        transcription = transcribe_audio(path)
        print("Transcription completed:")
        print(transcription)