from langchain_community.document_loaders import PyPDFLoader
from dotenv import load_dotenv
load_dotenv() 
import os
import openai

from openai import OpenAI


loader = PyPDFLoader(r"C:\Users\hp\Desktop\ResumeBuilderProject\chandani_resume.pdf")
pages = loader.load_and_split()


client = OpenAI()
completion = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "system", "content": "You are a professional resume extractor, your task is to extract name, email id, phone number, skills from the given text. Give the output in json format"},
        {
            "role": "user",
            "content": f"Here is the text{pages}"
        }
    ]
)

print(completion.choices[0].message)


# print(pages)