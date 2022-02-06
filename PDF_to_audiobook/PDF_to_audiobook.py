import PyPDF2
import requests
from gtts import gTTS
import os

# Convert PDF to a text file
pdffile = open('Test.pdf','rb')
pdfreader = PyPDF2.PdfFileReader(pdffile)
num_of_pages = pdfreader.numPages

# Makes a new line for each page
for x in range(num_of_pages):
    page = pdfreader.getPage(x)
    text = page.extractText()

    file1 = open('PDF_to_text.txt','a')
    file1.writelines(text + '\n')

with open("PDF_to_text.txt", "r") as file:
    data = file.readlines()

# Save a text to speech mp3 file and then play it
print(data)
pdf_string = " ".join(data)
voice = gTTS(text=pdf_string, lang="en", slow=False)
voice.save("PDF_to_text.mp3")
os.system("start PDF_to_text.mp3")