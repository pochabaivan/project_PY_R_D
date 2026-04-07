# project_PY_R_D
This is repository to programming course in PYTHON from Robot Dreams.
# PROJEKT METEO INFORMÁCIE

Zobrazuje meteorologické údaje z iného Web portálu napr. Weatherbit alebo Open Meteo.
Spracúva meteorologické údaje spôsobom, že z nich vypočíta vybrané štatisticky vyčíslené hodnoty.
Nakoniec vypočítané hodnoty zobrazí na jednoduchej webstránke.

Upresnenie:
Údaje, ktoré budú preberané z portálu a následne spracúvané a zobrazované sú evidované
pre mestá: Bratislava": (48.1486, 17.1077) a Victoria": (48.4284, -123.3656)
Sú to nasledovné údaje:
 - temperature_2m_mean - priemerná teplota 2m nad zemou [°C]
 - wind_speed_10m_mean - priemerná rýchlosť vetra 10m nad zemou [m/s]
 - percipitation_sum - celkový úhrn zrážok [mm]
 - precipitation_hours - dĺžka trvania zrážok celkom [s]
 - daylight_duration - obdobie dňa kedy je svetlo [s] 
 - sunshine_duration - obdobie dňa kedy je slnenčný svit [s]
   ## Vypočítavané veličiny pre vyššie spomenuté mestá 
   ## Bratislava": (48.1486, 17.1077) a Victoria": (48.4284, -123.3656)
   ## Údaje pre obe mestá budú zakreslené do grafov pre porovnanie údajov
   ## oboch vyššie spomenutých miest
  - Srel: pomer trvania slnečného svitu a dĺžky dňa v percentách
  - GDD: výpočet rastových dní ako rozdiel priemernej teploty a bázy 5°C (minimum 0)
  - Rdi: intenzita zrážok (množstvo / čas), ak pršalo viac ako 0 hodín
  - Di: Index vetra vynásobený slnečným svitom prevedeným na hodiny