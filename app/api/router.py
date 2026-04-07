from fastapi import APIRouter, Request, Depends  # Importy pre routovanie a správu requestov
from fastapi.templating import Jinja2Templates  # Modul pre renderovanie HTML šablón

# (Predpokladané importy WeatherService a WeatherRepository sú vyššie)

router = APIRouter()  # Inicializácia routera pre API koncové body
templates = Jinja2Templates(directory="app/templates")  # Nastavenie cesty k HTML šablónam


@router.get("/")  # Definícia GET endpointu na domovskej adrese
async def index(request: Request):  # Funkcia obsluhujúca požiadavku na webovú stránku
    repo = WeatherRepository()  # Vytvorenie inštancie repozitára
    service = WeatherService(repo)  # Vytvorenie inštancie servisu s repozitárom

    try:  # Pokus o získanie a zobrazenie dát
        data = await service.get_city_comparison()  # Získanie spracovaných dát pre mestá
        return templates.TemplateResponse("index.html", {  # Vrátenie vyrenderovanej HTML stránky
            "request": request,  # Povinný objekt požiadavky pre Jinja2
            "data": data,  # Úspešne načítané dáta
            "error": None  # Žiadna chyba
        })
    except HTTPException as e:  # Ak počas procesu nastane kontrolovaná chyba
        return templates.TemplateResponse("index.html", {  # Vrátenie stránky s chybovým hlásením
            "request": request,
            "data": {},  # Prázdne dáta
            "error": e.detail  # Popis chyby z výnimky
        }, status_code=e.status_code)  # Nastavenie správneho HTTP kódu odpovede

