<header>
        <h1>README.md</h1>
    </header>
    <section>
        <h2>Opis projektu</h2>
        <p>
            Ten projekt generuje stronę HTML na podstawie treści podanej przez użytkownika w pliku tekstowym. Zawiera dynamicznie stworzoną
            treść wewnątrz taga <code>&lt;article&gt;</code> oraz generuje schemat kolorów dopasowany tematycznie do tematu artykułu. 
            Projekt korzysta z modelu językowego GPT-4o-mini za pomocą API OpenAI.
        </p>
    </section>

  <section>
        <h2>Funkcje</h2>
        <ul>
            <li>Wczytanie treści z pliku tekstowego <code>article.txt</code>.</li>
            <li>Wygenerowanie artykułu w strukturze semantycznego HTML zgodnie z wytycznymi.</li>
            <li>Generowanie dopasowanego schematu kolorów w formacie szesnastkowym (hexadecimal).</li>
            <li>Tworzenie strony HTML z wypełnionym szablonem <code>szablon.html</code>.</li>
            <li>Obliczanie liczby tokenów używanych przez model GPT-4o-mini.</li>
            <li>Obsługa wyjątków w przypadku błędów API lub nieprawidłowych plików.</li>
        </ul>
    </section>

  <section>
        <h2>Wymagania</h2>
        <p>Aby uruchomić projekt, wymagane są:</p>
        <ul>
            <li>Python 3.12.8 lub nowszy.</li>
            <li>Zainstalowane biblioteki:
                <ul>
                    <li><code>openai</code></li>
                    <li><code>tiktoken</code></li>
                    <li><code>python-dotenv</code></li>
                    <li><code>os</code> i <code>re</code> (standardowe biblioteki Pythona).</li>
                </ul>
            </li>
            <li>Plik <code>.env</code> przechowujący klucz API OpenAI:
                <pre>OPENAI_API_KEY=twój_klucz_api</pre>
            </li>
            <li>Plik tekstowy <code>article.txt</code> zawierający treść do analizy.</li>
            <li>Szablon HTML <code>szablon.html</code> do wygenerowania finalnej strony HTML.</li>
        </ul>
    </section>

  <section>
        <h2>Struktura plików</h2>
        <pre>
.
├── main.py                # Główny skrypt projektu
├── article.txt            # Plik wejściowy z treścią artykułu
├── szablon.html           # Szablon HTML dla finalnej strony
├── wynik.html             # Wygenerowana strona HTML
├── .env                   # Plik z kluczem API
└── README.md              # Dokumentacja projektu
        </pre>
    </section>

  <section>
        <h2>Jak uruchomić</h2>
        <ol>
            <li>Zainstaluj wymagane pakiety:
                <pre>pip install openai python-dotenv tiktoken</pre>
            </li>
            <li>Utwórz plik <code>.env</code> i dodaj do niego klucz API w formacie:
                <pre>OPENAI_API_KEY=twój_klucz_api</pre>
            </li>
            <li>Dodaj treść tematu lub pytanie do pliku <code>article.txt</code>.</li>
            <li>Uruchom skrypt <code>main.py</code>:
                <pre>python main.py</pre>
            </li>
            <li>Otwórz plik <code>wynik.html</code>, który zostanie zapisany w folderze projektu jako wynik.</li>
        </ol>
    </section>
