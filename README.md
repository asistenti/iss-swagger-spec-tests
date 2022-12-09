Za pokretanje testova je neophodno imati instaliran python (pozeljno neku od novijih verzija): https://www.python.org/downloads/

Nakon toga, potrebno je instalirati pip alat koji će vam omogućiti da instalirate eksterne biblioteke
u lokalni virutelni environment: https://pip.pypa.io/en/stable/installation/

Kreiranje lokalnog virtual environment-a je pozeljno da uradite u ovom projektu (pozicionirati se u prevucen projekat). Kreiranje i aktivacija:

- Linux i MacOS:
  virtualenv test_env
  source test_env/bin/activate
- Windows:
  virtualenv test_env
  test_env\Scripts\activate

Kada ste aktivirali virtual environment, potrebno je instalirati sledece biblioteke:

- pip install requests
- pip install deepdiff

Nakon toga, testove pokretati sa sledecim komandama:

- python -m unittest test/test_passenger.py
- python -m unittest test/test_driver.py
- python -m unittest test/test_ride.py
- python -m unittest test/test_review.py
- python -m unittest test/test_panic.py
- python -m unittest test/test_vehicle.py
- python -m unittest test/test_user.py
- python -m unittest test/test_unregistered_user.py

Konfiguracija porta (8080) se nalazi u fajlu test/server_port.py pa ako vam je Spring pokrenut na drugom portu, promeniti vrednost u tom fajlu

U folder-u request_bodies se nalaze json-i za sve endpoint-e koji zahtevaju telo u zahtevu.

U folder-u response_bodies se nalaze json-i za povratne vrednosti svih endpoint-a.

Vrednosti u navedenim folderima su uzete spram poslednje verzije OpenAPI specifikacije (1.1.11)

Testovi funkcionisu tako sto proveravaju status odgovora i STRUKTURU odgovora. Proveravanje STRUKTURE znaci da se samo proverava da li postoje svi atributi u odgovoru spram onoga sto
