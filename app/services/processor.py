import pandas as pd  # Knižnica pre manipuláciu a analýzu dát
import numpy as np  # Knižnica pre numerické výpočty
from pathlib import Path  # Modul pre prácu so súborovými cestami


class WeatherService:  # Trieda pre spracovanie biznis logiky
    def __init__(self, repo):  # Inicializácia s injektovaným repozitárom
        self.repo = repo  # Uloženie inštancie repozitára do atribútu

    def _process_logic(self, raw_data: dict, city_name: str) -> pd.DataFrame:  # Interná metóda na výpočty
        try:  # Blok pre ošetrenie chýb pri spracovaní dát
            df = pd.DataFrame(raw_data['daily'])  # Konverzia JSON dát na Pandas DataFrame

            # Srel: pomer trvania slnečného svitu a dĺžky dňa v percentách (ošetrenie delenia nulou)
            df['s_rel'] = (df['sunshine_duration'] / df['daylight_duration']).replace([np.inf, -np.inf], 0).fillna(
                0) * 100

            # GDD: výpočet rastových dní ako rozdiel priemernej teploty a bázy 5°C (minimum 0)
            df['gdd'] = (df['temperature_2m_mean'] - 5).clip(lower=0)

            # Rdi: intenzita zrážok (množstvo / čas), ak pršalo viac ako 0 hodín
            df['rdi'] = df.apply(
                lambda r: r['precipitation_sum'] / r['precipitation_hours'] if r['precipitation_hours'] > 0 else 0,
                axis=1)

            # Di: Index vetra vynásobený slnečným svitom prevedeným na hodiny
            df['di'] = df['wind_speed_10m_max'] * (df['sunshine_duration'] / 3600)

            output_dir = Path("output")  # Definovanie priečinka pre export
            output_dir.mkdir(exist_ok=True)  # Vytvorenie priečinka, ak neexistuje
            df.to_csv(output_dir / f"{city_name.lower()}.csv", index=False)  # Uloženie výsledkov do CSV

            return df  # Vrátenie spracovaného DataFrame
        except KeyError as e:  # Ak v API odpovedi chýba očakávaný kľúč
            raise HTTPException(status_code=500, detail=f"Chýbajúce dáta v odpovedi API: {e}")

    async def get_city_comparison(self):  # Hlavná metóda pre získanie a porovnanie miest
        cities = {  # Definícia súradníc pre sledované mestá
            "Bratislava": (48.1486, 17.1077),
            "Victoria": (48.4284, -123.3656)
        }
        combined_results = {}  # Prázdny slovník pre finálne výsledky

        for name, coords in cities.items():  # Cyklus cez definované mestá
            # Volanie repozitára pre získanie historických dát
            raw = await self.repo.get_historical_data(coords[0], coords[1], "2026-03-02", "2026-03-15")
            processed_df = self._process_logic(raw, name)  # Výpočet metrík cez pomocnú metódu

            # Konverzia DataFrame na zoznam slovníkov vhodný pre JSON odpoveď a frontend
            combined_results[name] = processed_df.rename(columns={'time': 'date'}).to_dict(orient='records')

        return combined_results  # Vrátenie skombinovaných dát

