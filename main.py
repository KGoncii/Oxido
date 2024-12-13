import openai
import os
import tiktoken
import re
from dotenv import load_dotenv

load_dotenv()
def load_dotenv():
    try:
        openai.api_key = os.getenv("OPENAI_API_KEY")
    except Exception as e:
        print("Wystąpił błąd podczas pobierania klucza API z pliku .env:", e)


def ask_gpt4o(question, model):
    try:
        prompt = f"Generate an article on the following topic. The article should contain a title and at least two paragraphs with two <p></p> section:\n\n{question}\n"
        response = openai.ChatCompletion.create(
            model=model,
            messages=[{"role": "user", "content": prompt}],
            max_tokens=500,
            temperature=0.7,
            stop=None
        )
        return response['choices'][0]['message']['content'].strip()
    except Exception as e:
        print("Wystąpił błąd podczas komunikacji z API OpenAI:", e)
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


def read_file(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            content = file.read().strip()
        return content
    except Exception as e:
        print(f"Nie udało się wczytać pliku: {e}")
        return 0


def create_html_page(title, content, template_path="szablon.html"):
    try:
        with open(template_path, 'r', encoding='utf-8') as template_file:
            template = template_file.read()

        html_content = template.replace("{{title}}", title).replace("{{content}}", content)

        return html_content
    except Exception as e:
        print(f"Nie udało się wczytać lub przetworzyć szablonu: {e}")
        return 0

def get_content(article):
    content = "\n".join(article.split("\n")[1:]).strip()
    return content

model = "gpt-4o-mini"
file_path = "tiger article.txt"

content_from_file = read_file(file_path)

if content_from_file:
    article = ask_gpt4o(content_from_file, model)

    title = article.split("\n")[0].replace("*", "").replace("#", "").strip()

    content = "\n".join(article.split("\n")[1:]).strip()

    html_content = create_html_page(title, content = re.sub(r'```|html|#', '', content))

    print("Title:", title)
    print("Content:", content)

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
