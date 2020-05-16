# wd-1-scraping-exercise

## Naloga

1. Pojdite na spletno stran Bolha.com in s pomočjo inspektorja poglejte od kod dobi spletna stran podatke za artikle

2. Inštalirajte `requests` in poskusite s Pythonom poustvarit requeste, da dobite rezultate za iskalni niz.
Opomba: rezultati bodo v obliki JSON, zato uporabite `requests` metodo `json`

3. Shranite rezultate v CSV

4. Inptalirajte paket `click` in ustvarite cli (command line interface), ki bo sprejel naslednje ukaze:
- search [article]: pridobi, shrani (vse) in prikaži zadnjih 10 novih artiklov za nek iskalni niz
- show [article]: pokaži vse shranjenen zadetke za nek iskalni niz
- show --list: pokaži vse shranjenen iskalne nize
- remove [article]: odstrani iskanje za artikel

5. (bonus) naredi cronjob, da se bo program samodjeno izvajala vsakih 6 ur

NOTE: Naloga je samo za potrebe učenja. Vsaka drugačna uporaba je na lastno odgovornost.
