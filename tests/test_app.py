import pytest                                # Framework pre testovanie
from unittest.mock import AsyncMock, patch   # Nástroje na simulovanie (mockovanie) objektov

@pytest.fixture                               # Definícia opakovane použiteľnej testovacej vzorky
def mock_raw_data():                          # Funkcia vracajúca simulované dáta z API
    return {
        "daily": {                            # Štruktúra kopírujúca reálnu odpoveď Open-Meteo
            "time": ["2026-03-02"],           # Ukážkový dátum
            "temperature_2m_mean": [15.0],    # Ukážková teplota
            "wind_speed_10m_max": [10.0],     # Ukážková rýchlosť vetra
            "precipitation_sum": [5.0],       # Ukážkové zrážky
            "precipitation_hours": [2.0],     # Trvanie zrážok
            "sunshine_duration": [3600.0],    # Trvanie slnka v sekundách
            "daylight_duration": [43200.0]    # Dĺžka dňa v sekundách
        }
    }

