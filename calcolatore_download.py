peso_file = input("Inserisci il peso del file da scaricare in GB: \n")
velocita_download  = input("Inserisci la velocità di rete a cui stai scaricando il file in mb/s (per valori decimali usa il '.': \n")

peso_file = float(peso_file)    # converte da stringa a numero
velocita_download = float(velocita_download)    # converte da stringa a numero

tempo_download = (peso_file*1000)/velocita_download     # conta i secondi che ci impiegherebbe a scaricare

tempo_download = (tempo_download/3600)  # converte i secondi in ore

tempo_download = str(tempo_download)    # converte il numero in stringa

print(tempo_download)   # stampa a schermo il tempo di download