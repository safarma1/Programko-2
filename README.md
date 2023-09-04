**Textová dokumentace k souboru main.py**

**Zadání programu** 

V souboru jsou uloženy polohy hvězd na nebeské sféře (v rovníkových souřadnicích), program dostane zadané místo na Zemi, datum a čas a zobrazí oblohu tak, jak je v daný okamžik vidět. 

**Popis pro uživatele**

Program má za cíl vytvořit a zobrazit na výstup hvězdnou mapu na základě vstupních dat od uživatele. Program je psaný v jazyce Python, před jeho spuštěním je tedy potřeba mít nainstalovaný Python 3 a některé jeho knihovny, které program využívá pro svou práci. Instalaci těchto knihoven je možné provést zadáním těchto příkazů přímo v terminálu: 

pip install geopy 

pip install tzwhere

pip install pytz 

pip install numpy 

pip install matplotlib

pip install skyfield

pip install timezonefinder
  
Při spuštění souboru si program vyžádá postupně celkem tři textové vstupy, přičemž každý z nich je potřeba ukončit klávesou Enter. Nejprve je potřeba zadat místo, odkud si přeje uživatel oblohu zobrazit, ať už jako město, ulici či GPS souřadnice. Pokud je vstup platný, tedy program dokáže identifikovat požadované místo, přistoupí k dalšímu dotazu, v opačném případě načítá tento vstup tak dlouho, dokud není validní. 
Dále je potřeba zadat datum, a to ve formátu „yyyy-mm-dd“ (jak je uvedeno i při samotné výzvě v programu), tedy nejprve čtyři číslice označující rok, poté pomlčka, poté dvě číslice označující měsíc, poté opět pomlčka, a nakonec dvě číslice označující den. Mezi jednotlivými daty nemá být žádná mezera, ani jiný bílý znak. Opět platí, že pokud je vstup takto vyhodnocen jako validní, zobrazí se poslední dotaz, v opačném případě, probíhá tento dotaz tak dlouho, dokud není zadán ve správném formátu. 
Na závěr je potřeba zadat správný čas ve formátu „hh:mm“, tedy dvě číslice označující hodinu, poté dvojtečka a dvě číslice označující minuty. Pokud je takto vstup platný, program již zobrazí hvězdnou oblohu a tu poté uloží ve formátu pdf na stejné místo v adresáři, ve kterém je uložen i samotný program.  


**Programátorský popis**

Tento kód je určen pro vizualizaci hvězdné oblohy v určitém místě a čase. Představuje interaktivní skript, který požádá uživatele o zadání místa, data a času, a následně zobrazí hvězdnou oblohu v daném okamžiku.
Celkově lze tento kód rozdělit na několik hlavních částí: načítání dat a knihoven, interakci s uživatelem pro získání vstupních údajů, výpočty pro pozici pozorovatele a hvězd, vizualizaci a úpravy grafu.


1.	Importy:
o	Importují se potřebné knihovny a balíčky, které jsou použity během skriptu. Patří sem práce s datem a časem, geografickými souřadnicemi, matematickými výpočty, grafickým zobrazením atd.
2.	Funkce pro kontrolu formátu data a času:
o	Jsou definovány dvě funkce je_spravny_format_data a je_spravny_format_casu, které slouží k ověření, zda zadané datum a čas mají správný formát.
3.	Načítání ephemerid a dat Hipparcos katalogu:
o	Ephemeridy pro Zemi a Slunce jsou načteny ze souboru 'de421.bsp'. Ephemeridy obsahují předpovězené polohy těles (planety, Slunce, atd.) v naší sluneční soustavě v čase. Tato data jsou základem pro výpočty astronomických jevů.
o	with load.open(hipparcos.URL) as f:: Otevření datového souboru Hipparcos katalogu hvězd.
o	stars = hipparcos.load_dataframe(f): Načtení dat z Hipparcos katalogu do DataFrame. DataFrame je struktura dat v Pandas knihovně, která umožňuje pracovat s tabulkovými daty.
4.	Funkce pro získání správného místa od uživatele:
o	Funkce ziskat_spravny_vstup_pro_misto žádá uživatele, aby zadal místo. Používá knihovnu Nominatim k geokódování zadaného místa na zeměpisné souřadnice.
5.	Funkce pro získání správného data a času od uživatele:
o	Funkce ziskat_spravny_vstup_pro_datum a ziskat_spravny_vstup_pro_cas žádají uživatele, aby zadal správný formát data a času.
6.	Získání souřadnic a časové zóny:
o	Získaná místa od uživatele jsou použita pro získání zeměpisných souřadnic (šířka a délka).
o	Pomocí knihovny TimezoneFinder je získána časová zóna na základě zadaných souřadnic.
7.	Konverze data a času na UTC:
o	Získané datum a čas jsou konvertovány na objekt datetime a následně na UTC.
8.	Definice pozorovaných objektů:
o	Jsou definovány objekty pro Slunce a Zemi.
9.	Výpočet pozice pozorovatele:
o	Výpočet pozice pozorovatele na základě zeměpisných souřadnic a času.
10.	Projekce na zobrazení hvězdné oblohy:
o	Výpočet projekce pro zobrazení hvězdné oblohy.
11.	Výpočet pozice hvězd:
o	Výpočet pozice hvězd na obloze na základě dat Hipparcos katalogu.
12.	Vytvoření grafu:
o	Inicializace parametrů pro graf.
o	Výběr hvězd podle jejich jasu (magnitudy).
o	Vytvoření grafu s označenými hvězdami na základě jejich pozic a jasu.
13.	Úpravy grafu:
o	příkaz ax.add_patch(hranice): Přidání kruhu (oblasti) reprezentujícího horizont do grafu. Proměnná hranice obsahuje informace o této oblasti, např. střed a poloměr.
o	Nastavení hranic a velikosti znaky pro hvězdy.
14.	Zobrazení grafu a uložení do PDF:
o	Zobrazení grafu s hvězdami.
o	Uložení grafu do PDF souboru.


