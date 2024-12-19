import openai
import os
import tiktoken
import re
import logging
from dotenv import load_dotenv

DEFAULT_ENCODING = 'utf-8'
TITLE_PLACEHOLDER = "{{title}}"
CONTENT_PLACEHOLDER = "{{content}}"
COLOR1 = "{{color1}}"
COLOR2 = "{{color2}}"
COLOR3 = "{{color3}}"
COLOR4 = "{{color4}}"
COLOR5 = "{{color5}}"
COLOR6 = "{{color6}}"
COLOR7 = "{{color7}}"

HTML_PROMPT_GUIDELINES = """
Write a detailed inside of HTML <article> tag on the topic: '{question}' using proper semantic structure. Follow these guidelines:
1.Use appropriate <section> tags to divide the content into logical parts, such as overview, introduction, main content, and conclusion.
2.Ensure that each paragraph is wrapped in <p> tags. 
3.Do not use <header> tags and anything other then inside of <article> tag. 
4.First verb must be short title without HTML tags, then <article> tag and anything else, not even "Title:" before.   
5.After </article> include <footer> tag, with elements like author name, publication date, and related links.    
6.Use other words then in article and remember about <h2> tag before every paragraph.
7.Put some <img alt=""> to this article and in alt="" put description of the image.
"""
HTML_PROMPT_COLOR = """
Generate seven colors in hexadecimal format which are most suitable for the topic: '{question}' using proper semantic structure.
Write them strictly in the following format: #000000, #FFFFFF, #FF0000 and nothing more.
Color1 is body background, color2 is header background, color3 is article background,  color4 is footer background, color5 is text color, color6 is header color, color7 is footer color.
Remember that background and text color of the tag should not be similar
"""

load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

def get_chat_response(model_name, prompt):
    return openai.ChatCompletion.create(
        model=model_name,
        messages=[{"role": "user", "content": prompt}],
        max_tokens=500,
        temperature=1,
        stop=None
    )


def ask_gpt(question, model_name, HTML_PROMPT):
    try:
        prompt = HTML_PROMPT.format(question=question)
        response = get_chat_response(model_name, prompt)
        return response['choices'][0]['message']['content'].strip()
    except Exception as e:
        print(
            "Wystąpił błąd podczas komunikacji z API OpenAI. Sprawdź swoje poświadczenia API lub poprawność zapytania:",
            e)
        return "Nie udało się uzyskać odpowiedzi."


def count_tokens(text, model):
    try:
        encoding = tiktoken.encoding_for_model(model)
        tokens = encoding.encode(text)
        return len(tokens)
    except KeyError:
        print(f"Nie znaleziono kodowania dla modelu {model}. Używam domyślnego kodowania.")
        encoding = tiktoken.get_encoding("cl100k_base")
        tokens = encoding.encode(text)
        return len(tokens)


def read_file_contents(path):
    try:
        with open(path, 'r', encoding=DEFAULT_ENCODING) as file:
            content = file.read().strip()
        return content
    except Exception as error:
        logging.error(f"Failed to read file at '{path}': {error}")
        return None


def load_template(template_path, encoding):
    with open(template_path, 'r', encoding=encoding) as file:
        return file.read()


def create_html_page(title, content, color_list , template_path="szablon.html", encoding="utf-8"):
    try:
        template_content = load_template(template_path, encoding)
        final_html = (
            template_content
            .replace(TITLE_PLACEHOLDER, title)
            .replace(CONTENT_PLACEHOLDER, content)
            .replace(COLOR1, color_list[0])
            .replace(COLOR2, color_list[1])
            .replace(COLOR3, color_list[2])
            .replace(COLOR4, color_list[3])
            .replace(COLOR5, color_list[4])
            .replace(COLOR6, color_list[5])
            .replace(COLOR7, color_list[6])
        )
        return final_html
    except FileNotFoundError as e:
        print(f"Nie udało się wczytać pliku szablonu: {e}")
        return None

model = "gpt-4o-mini"
file_path = "article.txt"

content_from_file = read_file_contents(file_path)

if content_from_file:
    article = ask_gpt(content_from_file, model, HTML_PROMPT_GUIDELINES)
    article = re.sub(r'```|html|#', "", article).strip()
    title = article.split("\n")[0].replace("*", "").replace("#", "").strip()

    content = "\n".join(article.split("\n")[1:]).strip()
    colors = ask_gpt(title, model, HTML_PROMPT_COLOR)
    color_list = colors.split(", ")

    html_content = create_html_page(
        title,
        content=re.sub(r'```|html|#', '', content),
        color_list=color_list
    )
    print("Title:", title)
    print("Content:", content)
    print("Colors:", colors)

    plik = open('wynik.html', 'w')
    plik.write(html_content)
    plik.close()

    open("wynik.html")

    if html_content:
        with open('wynik.html', 'w', encoding='utf-8') as file:
            file.write(html_content)

        os.startfile("wynik.html")

    print("\nWygenerowany artykuł:\n", article)

    print("\nTreść z pliku zajęła ", count_tokens(content_from_file, model), " tokenów")
    print("Artykuł zajęł ", count_tokens(article, model), " tokenów")
    print("Łącznie ", count_tokens(article, model) + count_tokens(content_from_file, model), " tokenów")
