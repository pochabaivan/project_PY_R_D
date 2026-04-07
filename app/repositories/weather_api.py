import httpx  # Knižnica pre asynchrónne HTTP požiadavky
from fastapi import HTTPException, status  # Import pre vyvolanie HTTP chýb a kódov


class WeatherRepository:  # Trieda zodpovedná za komunikáciu s externým API
    URL = "https://open-meteo.com"  # Základná URL adresa pre Open-Meteo API

    async def get_historical_data(self, lat: float, lon: float, start: str, end: str):  # Metóda na získanie dát
        params = {  # Definícia parametrov pre GET požiadavku
            "latitude": lat, "longitude": lon,  # Súradnice miesta
            "start_date": start, "end_date": end,  # Časový rozsah
            "daily": ["temperature_2m_mean", "wind_speed_10m_max", "precipitation_sum",
                      "precipitation_hours", "sunshine_duration", "daylight_duration"],  # Požadované premenné
            "timezone": "GMT"  # Časové pásmo nastavené na GMT
        }

        async with httpx.AsyncClient() as client:  # Otvorenie asynchrónneho HTTP klienta
            try:  # Blok pre odchytenie chýb pri sieťovej komunikácii
                response = await client.get(self.URL, params=params, timeout=15.0)  # Odoslanie požiadavky

                if response.status_code == 400:  # Ak sú parametre nesprávne
                    raise HTTPException(status_code=400, detail="Neplatné parametre pre Open-Meteo API.")
                elif response.status_code == 429:  # Ak sme poslali príliš veľa požiadaviek
                    raise HTTPException(status_code=429, detail="Prekročený limit požiadaviek (Rate limit).")
                elif response.status_code >= 500:  # Ak má server Open-Meteo vnútorný problém
                    raise HTTPException(status_code=502, detail="Meteo server je momentálne nedostupný.")

                response.raise_for_status()  # Vyvolá chybu pre ostatné neúspešné HTTP kódy
                return response.json()  # Vráti spracované dáta vo formáte JSON (slovník)

            except httpx.ConnectError:  # Ak sa nedá pripojiť k internetu/serveru
                raise HTTPException(status_code=503, detail="Nepodarilo sa nadviazať spojenie so serverom.")
            except Exception as e:  # Zachytenie akejkoľvek inej neočakávanej chyby
                raise HTTPException(status_code=500, detail=f"Neočakávaná chyba repozitára: {str(e)}")
