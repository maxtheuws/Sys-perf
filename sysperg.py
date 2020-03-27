import psutil
import platform
from datetime import datetime

keuze = 0
def get_size(bytes, suffix="B"):
    factor = 1024
    for unit in ["", "K", "M", "G", "T", "P"]:
        if bytes < factor:
            return f"{bytes:.2f}{unit}{suffix}"
        bytes /= factor

while True:
    print("1. Systeem informatie")
    print("2. Boot Datum/Tijd")
    print("3. Processor informatie")
    print("4. RAM Informatie")
    print("5. Schijf Informatie")
    keuze = int(input("Welke informatie wil je ophalen? (Voer het nummer in): "))
    if keuze == 1:
        print("-"*40, "Systeem Informatie", "-"*40)
        uname = platform.uname()
        print(f"Systeem: {uname.system}")
        print(f"Computernaam: {uname.node}")
        print(f"Release: {uname.release}")
        print(f"Versie: {uname.version}")

    elif keuze == 2:
        print("-"*40, "Boot Datum/Tijd", "-"*40)
        boot_time_timestamp = psutil.boot_time()
        bt = datetime.fromtimestamp(boot_time_timestamp)
        print(f"Boot Datum/Tijd: {bt.year}/{bt.month}/{bt.day} {bt.hour}:{bt.minute}:{bt.second}")

    elif keuze == 3:
        print("-"*40, "Processor Informatie", "-"*40)
        print("Aantal Fysieke cores:", psutil.cpu_count(logical=False))
        print("Totaal aantal cores:", psutil.cpu_count(logical=True))
        cpufreq = psutil.cpu_freq()
        print(f"Huidige Frequentie: {cpufreq.current:.2f}Mhz")
        print(f"Maximale Frequentie: {cpufreq.max:.2f}Mhz")
        print(f"Processor Gebruik: {psutil.cpu_percent()}%")

    elif keuze == 4:
        print("-"*40, "RAM Informatie", "-"*40)
        svmem = psutil.virtual_memory()
        print(f"Totaal: {get_size(svmem.total)}")
        print(f"Beschikbaar: {get_size(svmem.available)}")
        print(f"Gebruikt: {get_size(svmem.used)}")
        print(f"Percentage: {svmem.percent}%")

    elif keuze == 5:
        print("-"*40, "Schijf Informatie", "-"*40)
        print("Partities en verbruik:")
        partitions = psutil.disk_partitions()
        for partition in partitions:
            print(f"--- Schijf: {partition.device} ---")
            print(f"  Drive Letter: {partition.mountpoint}")
            print(f"  Bestandssysteem: {partition.fstype}")
            try:
                partition_usage = psutil.disk_usage(partition.mountpoint)
            except PermissionError:
                continue
            print(f"  Total Grootte: {get_size(partition_usage.total)}")
            print(f"  Gebruikt: {get_size(partition_usage.used)}")
            print(f"  Beschikbaar: {get_size(partition_usage.free)}")
            print(f"  Percentage: {partition_usage.percent}%")
    else:
        print("Dat is geen gelding nummer")
    while True:
        antwoord = input("Wil je nog iets checken? (Voer ja of nee in): ")
        if antwoord in ("ja", "nee"):
            break
        print("Voer ja of nee in.")
    if antwoord == "ja":
        continue
    else:
        print("Houdoe!")
        break
