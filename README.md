## Instrukcje

### Pierwsze uruchomienie

Utworzenie wirtualnego środowiska Python'a

`python -m venv venv`

Aktywacja utworzonego wirtualnego środowiska

`source venv/bin/activate`

Instalacja bibliotek

`pip install -r requirements.txt`

Instalacja biblioteki cec2017-py

```
git clone https://github.com/tilleyd/cec2017-py
cd cec2017-py
python setup.py install
cd ..
```

### Uruchomienie skryptu, który uruchamia algorytm ewolucji różnicowej oraz tworzy wykres przedstwiający zależność średniej wartości funkcji celu wygenerowanych punktów od numeru iteracji

Przed uruchomieniem skryptu należy ustawić parametry algorytmu w pliku konfiguracyjnym `differential_evolution_config.py`.

Uruchomienie skryptu:

`PYTHONPATH=. python run_and_create_plot.py`
