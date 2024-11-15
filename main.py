import os
import openai
from dotenv import load_dotenv

load_dotenv()
openai_api_key = os.getenv("OPENAI_API_KEY")

openai.api_key = openai_api_key


def read_article(filename):
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            return file.read()
    except FileNotFoundError:
        print(f"Plik {filename} nie został znaleziony.")
        return ""


def read_template(filename):
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            return file.read()
    except FileNotFoundError:
        print(f"Plik szablonu {filename} nie został znaleziony.")
        return ""


def generate_html_body(article_text):
    prompt = f"""
    Przekształć przekazany artykuł na zawartość HTML. 
    Na samym początku dodaj tytuł jaki może mieć ten artyków, nie używaj do tego wyrazów jakie znajdują sie w artykule
    Tekst artykułu ma być w klasie container
    Zastosuj także odpowiednie znaczniki HTML do hierarchii treści i podziału na sekcje. 
    Dodaj tagi <img src="image_placeholder.jpg" alt="opis obrazka"> tam, gdzie odpowiednie są obrazy, najlepiej nad tytułem każdej sekcji.
    Na końcu dodaj sekcję <footer> z prostym tekstem.

    Artykuł:
    {article_text}
    """
    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "user", "content": prompt}
            ],
            max_tokens=3000,
            temperature=0.7
        )

        html_body = response['choices'][0]['message']['content'].strip()
        print("Zawartość <body> wygenerowana pomyślnie.")
        return html_body
    except Exception as e:
        print("Wystąpił błąd podczas komunikacji z API OpenAI:", e)
        return ""


def combine_template_with_body(template, body_content):
    try:
        updated_html = template.replace("<body>", f"<body>\n{body_content}")
        return updated_html
    except Exception as e:
        print("Wystąpił błąd podczas łączenia szablonu z treścią body:", e)
        return template


def save_html_to_file(html_content, filename):
    try:
        with open(filename, 'w', encoding='utf-8') as file:
            file.write(html_content)
        print(f"Kod HTML zapisany w pliku: {filename}")
    except Exception as e:
        print(f"Wystąpił błąd podczas zapisywania pliku {filename}:", e)


def main():
    article_text = read_article("input_article.txt")
    if not article_text:
        return

    body_content = generate_html_body(article_text)
    if not body_content:
        return

    template_html = read_template("szablon.html")
    if not template_html:
        return

    final_html = combine_template_with_body(template_html, body_content)

    save_html_to_file(final_html, "artykul.html")


if __name__ == "__main__":
    main()
