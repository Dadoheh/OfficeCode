Ze względów na nową polityke bezpieczeństwa kod dostępu do biura zapisujemy w bardzo nietypowej formie, 
jako zbiór ruchów na klawiaturze numerycznej.\
Każdy przycisk, który ma zostać naciśnięty, można znaleźć, zaczynając od pozycji poprzedniego przycisku 
i przechodząc do sąsiednich przycisków na klawiaturze: U przesuwa się w górę, D - w dół, L - w lewo, a R - w prawo. 
Każdy wiersz instrukcji odpowiada jednemu przyciskowi, zaczynając od poprzedniego przycisku 
(lub, w przypadku pierwszego wiersza, przycisku "5"); na końcu każdego wiersza naciśnij przycisk,
 na którym się znajdujesz. Jeśli jakiś ruch nie prowadzi do przycisku, zignoruj go.

Klawiatura:
```
1 2 3
4 5 6
7 8 9
```

## Przykład:
```
ULL
RRDDD
LURDL
UUUUD
```

- Zaczynasz na "5" i poruszasz się w górę (do "2"), w lewo (do "1") i w lewo 
    (nie możesz i zostajesz na "1"), więc pierwszym przyciskiem jest 1.
- Zaczynając od poprzedniego przycisku ("1"), przesuwamy się dwa razy w prawo (do "3"),
 a następnie trzy razy w dół (zatrzymując się na "9" po dwóch ruchach i ignorując trzeci), kończąc na "9".
- Kontynuując od "9", poruszamy się w lewo, w górę, w prawo, w dół i w lewo, kończąc na "8".
- Na koniec poruszamy się cztery razy w górę (zatrzymując się na "2"), a następnie raz w dół, kończąc na 5.

Tak więc w tym przykładzie kod biura to 1985.

## Ocena:
 Ocenie podlegają dwie rzeczy:
  - Poprawność rozwiązania - czy dostarczone rozwiązanie zwraca dobry wynik
  - Czystość implementacji - czytelność kodu, złożoność obliczeniowa
