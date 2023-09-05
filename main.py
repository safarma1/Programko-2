from datetime import datetime
from geopy import Nominatim
from tzwhere import tzwhere
from pytz import timezone, utc
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.collections import LineCollection
from matplotlib.patches import Circle
from skyfield.api import Star, load, wgs84
from skyfield.data import hipparcos
from skyfield.projections import build_stereographic_projection
import re
from timezonefinder import TimezoneFinder

# Funkce pro kontrolu formátu data a času
def je_spravny_format_data(cas):
    regex = r"\d{4}-\d{2}-\d{2}$"
    if re.match(regex, cas):
        return True
    else:
        return False

def je_spravny_format_casu(cas):
    regex = r"\d{2}:\d{2}$"
    if re.match(regex, cas):
        return True
    else:
        return False

# Načítání ephemerid pro Zemi a Slunce
eph = load('de421.bsp')

# Načítání dat Hipparcos katalogu hvězd
with load.open(hipparcos.URL) as f:
    stars = hipparcos.load_dataframe(f)

# Funkce pro získání správného místa od uživatele
def ziskat_spravny_vstup_pro_misto():
    while True:
        misto = input("Zadejte místo:\n")
        lokalizator = Nominatim(user_agent='myGeocoder')
        umisteni = lokalizator.geocode(misto)
        if umisteni:
            return umisteni
        else:
            print("Zadali jste neznámé místo. Zkuste to znovu.")

umisteni = ziskat_spravny_vstup_pro_misto()

sirka, delka = umisteni.latitude, umisteni.longitude

# Funkce pro získání správného data od uživatele
def ziskat_spravny_vstup_pro_datum():
    while True:
        datum = input("Zadejte datum ve formátu 'yyyy-mm-dd':\n")
        if je_spravny_format_data(datum):
            return datum
        else:
            print("Neplatný formát datumu. Zkuste to znovu.")

platne_datum = ziskat_spravny_vstup_pro_datum()

# Funkce pro získání správného času od uživatele
def ziskat_spravny_vstup_pro_cas():
    while True:
        cas = input("Zadejte čas ve formátu 'hh:mm':\n")
        if je_spravny_format_casu(cas):
            return cas
        else:
            print("Neplatný formát času. Zkuste to znovu.")

platny_cas = ziskat_spravny_vstup_pro_cas()

kdy = platne_datum + ' ' + platny_cas

dt = datetime.strptime(kdy, '%Y-%m-%d %H:%M')

# Inicializace TimezoneFinder
tf = TimezoneFinder()

# Získání časové zóny z daných zeměpisných souřadnic
znacka_casoveho_pasma = tf.timezone_at(lng=delka, lat=sirka)
lokalni = timezone(znacka_casoveho_pasma)

# Konverze na UTC
casova_jednotka = lokalni.localize(dt, is_dst=None)
utc_jednotka_casu = casova_jednotka.astimezone(utc)

# Definice pozorovaných objektů
slunce = eph['sun']
zem = eph['earth']

ts = load.timescale()
t = ts.from_datetime(utc_jednotka_casu)

pozorovatel = wgs84.latlon(latitude_degrees=sirka, longitude_degrees=delka).at(t)

pozice = pozorovatel.from_altaz(alt_degrees=90, az_degrees=0)
ra, dec, vzdalenost = pozorovatel.radec()
stredni_objekt = Star(ra=ra, dec=dec)

stred = zem.at(t).observe(stredni_objekt)
projekce = build_stereographic_projection(stred)
uhel_pohledu = 180.0

pozice_hvezd = zem.at(t).observe(Star.from_dataframe(stars))
stars['x'], stars['y'] = projekce(pozice_hvezd)

velikost_grafu = 10
maximalni_velikost_hvezd = 100
magnituda = 10

jas_hvezdy = (stars.magnitude <= magnituda)
magnituda = stars['magnitude'][jas_hvezdy]
fig, ax = plt.subplots(figsize=(velikost_grafu, velikost_grafu))
    
hranice = plt.Circle((0, 0), 1, color='navy', fill=True)
ax.add_patch(hranice)

velikost_znacky = maximalni_velikost_hvezd * 10 ** (magnituda / -2.5)

ax.scatter(stars['x'][jas_hvezdy], stars['y'][jas_hvezdy],
           s=velikost_znacky, color='white', marker='.', linewidths=0, 
           zorder=2)

horizont = Circle((0, 0), radius=1, transform=ax.transData)
for col in ax.collections:
    col.set_clip_path(horizont)

ax.set_xlim(-1, 1)
ax.set_ylim(-1, 1)
plt.axis('off')

plt.savefig(f"{umisteni}.pdf", dpi=400, format="pdf", orientation="portrait")
plt.show()
plt.close()
