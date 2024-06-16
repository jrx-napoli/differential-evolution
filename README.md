## DE/rand/1/bin using TPA and MSR

### Instalacja

Utworzenie wirtualnego środowiska Python'a

`python -m venv env`

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

### Przykładowe wywołanie

`python main.py --y_func f8 --tpa --msr`

### Oddtworzenie eksperymentów z dokumentacji

`experiments.bat`