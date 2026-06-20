import logging
import pathlib
from datetime import datetime

logs_dir = pathlib.Path("reports/logs") 
logs_dir.mkdir(exist_ok=True, parents=True)   #Crea la carpeta si no existe

timestamp = datetime.now().strftime("%d-%m-%Y_%H-%M-%S")    #Genera timestamp con el horario actual

logging.basicConfig(    # da configuracion al logging global
    encoding="utf-8",
    filename= logs_dir / f"log_{timestamp}.log",    #Donde guarda el log
    level=logging.INFO, #desde que nivel registrar
    format= "%(asctime)s %(levelname)s %(name)s - %(message)s", #formato de cada linea
    force=True  #Si ya hay una config de logging se pisa con esta
)

logger = logging.getLogger("TT 26143 - Automatizacion QA") #crea un logger con el nombre definido