from fastapi.templating import Jinja2Templates
from pathlib import Path

# Získanie absolútnej cesty k priečinku so šablónami
# Predpokladáme, že šablóny sú v app/templates vzhľadom na koreň projektu
BASE_DIR = Path(__file__).resolve().parent.parent.parent
TEMPLATES_DIR = BASE_DIR / "templates"

# Inicializácia Jinja2 objektu, ktorý sa importuje v routeri
templates = Jinja2Templates(directory=str(TEMPLATES_DIR))

# Tu môžete pridať vlastné filtre pre Jinja2, ak sú potrebné
def format_float(value: float) -> str:
    """Formátuje desatinné čísla na dve desatinné miesta pre krajší výpis."""
    return f"{value:.2f}"

# Registrácia filtra do prostredia šablón
templates.env.filters["format_float"] = format_float
