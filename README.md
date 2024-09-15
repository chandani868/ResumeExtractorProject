Resume Information Extractor
This project extracts key information (name, email ID, phone number, skills) from a resume PDF using the OpenAI API (GPT-3.5-turbo). It leverages the langchain_community library for loading and processing PDF files, and openai for the information extraction. The extracted information is returned in JSON format.

Table of Contents
Prerequisites
Installation
Project Structure
Environment Variables
Usage
Troubleshooting
Notes
License
Prerequisites
Python 3.7+
An OpenAI API key
pip (Python package installer)
Installation
Clone the repository (if this is part of a larger project, skip this step):

bash
Copy code
git clone https://github.com/yourusername/resume-extractor.git
cd resume-extractor
Install required Python packages:

bash
Copy code
pip install openai python-dotenv langchain-community
openai: For interacting with OpenAI's GPT-3.5-turbo model.
python-dotenv: For loading environment variables from a .env file.
langchain_community: To handle PDF file loading and splitting.
Set up the .env file:

Create a .env file in the root directory of your project and add your OpenAI API key:
makefile
Copy code
OPENAI_API_KEY=your_openai_api_key_here
Project Structure
bash
Copy code
.
├── chandani_resume.pdf              # The resume PDF file
├── extractor.py                    # The main Python script
├── .env                            # Environment file to store API key
└── README.md                       # This README file
Environment Variables
This project uses the OpenAI API, which requires an API key for authentication. The API key is stored in a .env file for security.

Example .env file
makefile
Copy code
OPENAI_API_KEY=your_openai_api_key_here
Usage
Add the PDF file:

Place the PDF file you want to extract information from in a suitable location. Update the file path in the script accordingly.
Run the script:

Execute the Python script to extract resume information:
bash
Copy code
python extractor.py
Output:

The script will output the extracted information (name, email ID, phone number, and skills) in JSON format.
Example Output
json
Copy code
{
  "name": "Chandani Sharma",
  "email": "chandani.sharma@example.com",
  "phone_number": "+1234567890",
  "skills": ["Python", "Machine Learning", "Data Analysis"]
}
Script Details
The script performs the following steps:

Loads environment variables using python-dotenv.
Reads and splits the PDF file into pages using PyPDFLoader.
Combines the content of all pages into a single string.
Uses the OpenAI GPT-3.5-turbo model to extract resume details by sending the concatenated text.
Returns the extracted information in JSON format.
Troubleshooting
Missing or incorrect OpenAI API key: Make sure your .env file contains a valid API key for OpenAI.
File path issues: Ensure the path to the PDF file is correct in the script.
Module not found: If you encounter errors related to missing modules, verify you installed the required packages with pip install openai python-dotenv langchain-community.
Notes
This script assumes that the resume PDF is formatted in a way that the OpenAI model can parse. The accuracy of the extraction may vary depending on the structure and content of the resume.
The OpenAI API usage is billed, so ensure you have sufficient credits in your OpenAI account.
License
This project is licensed under the MIT License. See the LICENSE file for details.

