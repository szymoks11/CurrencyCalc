# Raport Konfiguracji Środowiska Programistycznego Python

## Wprowadzenie
Celem niniejszego raportu jest przedstawienie programu, którego zadaniem jest wspomaganie obliczania różnic kursowych dla faktur od zagranicznych kontrahentów. W międzynarodowej działalności gospodarczej często występuje konieczność dokonywania płatności w różnych walutach. Rezultatem takiego rozwiązania są różnice kursowe, które mogą znacząco wpłynąć na wyniki finansowe przedsiębiorstwa.

## Cel Programu
### Program ma na celu pomoc w obliczaniu różnic kursowych dla faktur od zagranicznych kontrahentów. Oto główne funkcje i cechy tego programu:
- **Przyjmowanie danych faktur i płatności**:
  -  Program umożliwia wprowadzenie danych dotyczących faktur, takie jak kwota, waluta oraz data wystawienia. Ponadto, pozwala na dodanie informacji o płatnościach, takie jak kwota, waluta oraz data płatności. Dzięki temu użytkownik może łatwo śledzić i zarządzać informacjami dotyczącymi faktur i płatności.
- **Pobieranie kursów walut**:
  - Program wykorzystuje API Narodowego Banku Polskiego (NBP), aby pobierać kursy walut. Dzięki temu użytkownik może mieć pewność, że obliczenia różnic kursowych są oparte na aktualnych danych.
- **Obliczanie różnic kursowych**:
  - Na podstawie danych faktur i kursów walut, program automatycznie oblicza różnice kursowe. W tym celu porównuje kurs waluty w dniu wystawienia faktury z kursem waluty w dniu jej zapłaty. Dzięki temu użytkownik może łatwo monitorować różnice kursowe powstałe na skutek zmiany kursu walut.
- **Zapisywanie danych**:
  - Program umożliwia zapisywanie wprowadzonych danych faktur i płatności. Dzięki temu użytkownik ma możliwość archiwizowania i sprawdzania swoich danych w przyszłości.
### Proces tworzenia programu
- **Aby utworzyć program, który pomoże w obliczaniu różnic kursowych dla faktur od zagranicznych kontrahentów, wykonaj następujące kroki**:
  - Zaimportować wymagane biblioteki takie jak datetime, requests i json. Jeśli nie są one jeszcze zainstalowane, możesz użyć menedżera pakietów, takiego jak pip, aby je zainstalować.

  - Zdefiniować funkcje walidacyjne: Stwórz funkcje, które będą sprawdzać poprawność danych wprowadzanych przez użytkownika. W przypadku tego programu, funkcje walidacyjne powinny sprawdzać format kwoty, waluty i daty.

  - Utworzyć funkcję main(), która będzie zarządzać procesem wprowadzania danych faktury i obliczania różnic kursowych. Ta funkcja prosi użytkownika o wprowadzenie danych faktury, sprawdzi ich poprawność, zapisze dane do pliku i następnie przejdzie do wprowadzenia danych płatności. Po wprowadzeniu danych płatności, użyje API NBP, aby pobrać kursy walut na odpowiednie daty i obliczyć różnicę kursów.
### Napotkane problemy
- Największym problemem jest API NBP, które nie jest do końca funkcjonalne. Nie da się pobierać kursów z dnia dzisiejszego, oraz czasami z dnia poprzedzającego, ponieważ występuje błąd "Brak danych". Trzeba więc poczekać, aż NBP zaaktualizuje kursy,aby prawidłowo obliczyć różnicę.
### Wnioski
- Przed rozpoczęciem projektu ważne jest zaplanowanie wszystkich kroków, wymagań i zasobów potrzebnych do jego realizacji. Przygotowanie solidnego planu pozwoli uniknąć problemów w trakcie tworzenia programu.
- Testowanie i debugowanie: Regularne testowanie kodu i debugowanie są nieodłącznymi elementami procesu tworzenia programów. Warto zainwestować odpowiednią ilość czasu na testowanie różnych scenariuszy i łatanie błędów.
- Dobra dokumentacja: Ważne jest utrzymanie aktualnej dokumentacji projektowej. Dokumentacja powinna zawierać instrukcje dotyczące instalacji, konfiguracji, używania i rozwiązywania problemów związanych z programem. Dobra dokumentacja ułatwia zrozumienie programu przez innych programistów i ułatwia utrzymanie go w przyszłości.