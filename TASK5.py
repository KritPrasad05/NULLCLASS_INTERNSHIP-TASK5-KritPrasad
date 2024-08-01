from transformers import MarianMTModel, MarianTokenizer
from datetime import datetime
import streamlit as st

model_name_hi = 'Helsinki-NLP/opus-mt-en-hi'
model_en_hi = MarianMTModel.from_pretrained(model_name_hi)
tokenizer_en_hi = MarianTokenizer.from_pretrained(model_name_hi)

def translate_text_to_hindi(text, model, tokenizer):
    current_time = datetime.now().time()
    start_time = datetime.strptime("21:00", "%H:%M").time()
    end_time = datetime.strptime("22:00", "%H:%M").time()
    
    if text[0].lower() in ['a','e','i','o','u']:
        if not (start_time <= current_time <= end_time):
            return "This word starts with a vowel. Please provide another word or try between 9 PM and 10 PM IST."

    encoded_text = tokenizer(text, return_tensors='pt')
    translated_tokens = model.generate(**encoded_text)
    translated_text = tokenizer.decode(translated_tokens[0], skip_special_tokens=True)

    return translated_text

text = st.text_input("Enter an English word to translate: ")
if text:
    translation = translate_text_to_hindi(text, model_en_hi, tokenizer_en_hi)
    st.write("Translation:", translation)

    if "This word starts with a vowel" in translation:
        st.error("This word starts with a vowel. Please provide another word or try between 9 PM and 10 PM IST.")

