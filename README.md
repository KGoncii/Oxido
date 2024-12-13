# Opis działania kodu:
Ten program umożliwia generowanie pełnej strony HTML na podstawie artykułu, który jest przechowywany w pliku tekstowym. Program wykorzystuje model OpenAI (ChatGPT) do przekształcenia treści artykułu na format HTML. W rezultacie użytkownik otrzymuje kompletny plik HTML, który może być użyty do podglądu artykułu w przeglądarce.

# Instrukcja uruchomienia:
Program wymaga zainstalowania Python 3 oraz biblioteki openai i python-dotenv. Jeśli ich nie masz, zainstaluj je za pomocą pip:
pip install openai python-dotenv

# Pliki wejściowe:
Upewnij się, że masz dwa pliki:
input_article.txt: Plik tekstowy zawierający artykuł, który chcesz przekształcić na HTML.
szablon.html: Szablon HTML, który zawiera tagi <body>, w które zostanie wstawiona treść artykułu.

W pliku .env umieść swój klucz API OpenAI:
OPENAI_API_KEY=twój_klucz_api

Program wczyta artykuł z pliku input_article.txt, przekształci go na HTML i zapisze wynikowy plik HTML w artykul.html.

Program wygeneruje plik artykul.html, który będzie zawierał artykuł w formacie HTML, gotowy do otwarcia w przeglądarce internetowej.
