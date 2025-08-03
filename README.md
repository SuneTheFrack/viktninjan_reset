# 🥷 ViktNinjan – Google Sheets-loggare via Replit

Loggar måltidsdata från GPT direkt till Google Sheet med följande kolumner:

- Datum
- Tid
- Person
- Måltid
- Innehåll
- Kalorier
- Fett
- Mättat fett
- Salt
- Fibrer

## Instruktioner

1. Skapa ett Google Sheet och döp det till **ViktNinjan**
2. Lägg in följande kolumner på rad 1:
   `Datum`, `Tid`, `Person`, `Mål`, `Innehåll`, `Kcal`, `Fett`, `Mättat fett`, `Salt`, `Fibrer`
3. Gå till [Google Cloud Console](https://console.cloud.google.com/)
   - Skapa projekt, aktivera Google Sheets API
   - Skapa servicekonto, hämta JSON-nyckel som `credentials.json`
   - Dela ditt ark med servicekontots mejladress
4. Kör projektet i Replit. Testa med en `POST` till `/loggmaltid`.

## Exempel på data som GPT kan skicka:

```json
{
  "datum": "2025-07-17",
  "tid": "12:15",
  "person": "Henrik",
  "mål": "Lunch",
  "innehåll": "Kycklingsallad med quinoa",
  "kcal": 540,
  "fett": 18,
  "mättat_fett": 4,
  "salt": 1.2,
  "fibrer": 5.6
}
```