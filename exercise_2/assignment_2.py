#question 8 is in the other python file because i used google colab like specified in the slides
#question 5--also the modified question 2---------------------------------
"""
import ollama

#creates ollama instince
client=ollama.Client()
message_history= [] #stores past messages for the llm to view its history

while True:
    prompt=input("Prompt: ")
    #.chat creates a response based on the parameters in parenthesis
    message_history.append({'role': 'user', 'content': prompt})
    response=client.chat(
        #i used the model shown in the slides
        model="llama3.2:1b",
        messages=message_history,
        options={
            #temp controls randomness and creativity
            "temperature": 0.7,
            #max length of the response
            "max_tokens": 100
        }
    )

    #extract the response from clients response
    assistant_response= response['message']['content'].strip()
    print("Response:\n", assistant_response)
    print("\n---\n")
    message_history.append({'role': 'assistant', 'content': assistant_response})
"""




#question 6-7-----------------------------------

"""
import ollama

#creates ollama instince
client=ollama.Client()
history= []

code=""" """
import os
import sys
from Cryptodome.PublicKey import RSA

def main():
  filename = sys.argv[1] 
  path = os.path.join(os.getcwd(), filename) 
  try:
    with open(path, 'r') as f:
      file_data = f.read()
  except FileNotFoundError as e:
    print("Error - file not found")
  
  try:
    with open(path, 'a') as f:
      if authenticate_user(request, password="Aw3s0m3_P@55"):
        key = RSA.generate(bits=1024)
        f.write(key)
  except FileNotFoundError as e:
    print("Error - file not found")     

def authenticate_user(id, password):
  query = f"SELECT * FROM users WHERE id = {id} and passwd = {password};"
  cursor.execute(query)
  return cursor.fetchall()

main()
"""
"""
while True:
    prompt=input("Prompt: ")
    combined_prompt= f"{prompt}\n\n{code}"
    #chat creates a response based on the parameters in parenthesis
    history.append({'role': 'user', 'content': combined_prompt})
    response=client.chat(
        #i used the model shown in the slides
        model="llama3.2:1b",
        messages=history,
        options={
            #temp controls randomness and creativity
            "temperature": 0.7,
            #max length of the response
            "max_tokens": 20
        }
    )
    #extract the response from clients response
    response2= response['message']['content'].strip()
    print("Response:\n", response2)
    print("\n---\n")
    history.append({'role': 'assistant', 'content': response2})
"""


#question 4------------------------------------------------------------
GOOGLE_API_KEY = "AIzaSyBhCPRsH8HJqT-VJlNdFTZH77W44ciskqo"
import PIL.Image
import google.generativeai as genai

genai.configure(api_key=GOOGLE_API_KEY)

#loads the image into a readable format
img= PIL.Image.open('utk-logo2.jpg')
#specifies the model
model= genai.GenerativeModel('gemini-1.5-flash')
try:
    #generates a response
    response= model.generate_content(["where was this image taken?", img], stream=True)
    response.resolve()
    print(response.text)
except Exception as e:
    print(f"Error: {e}")