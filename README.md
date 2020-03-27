Een simpele webservice/api waarmee systeemperformance opgevraagd kan worden. Denk aan de CPU-belasting, het in gebruik zijnde geheugen, diskruimte enz.

Voor de systeem perfomance opdracht ben ik op internet gaan zoeken naar modules die hier voor gebruikt kunnen worden. Ik kreeg niets gevonden dus ben ik rond gaan vragen bij klasgenoten. Een van mijn challenge-genoten heeft me een tutorial gestuurd die ik ook bij de bronvermelding heb gezet. 
Allereerst ben ik begonnen met het importeren van ‘psutil’ voor het ophalen van mijn hardware gegevens. Hierna importeer ik ‘platform’ voor het ophalen van mijn systeeminformatie.
Hierna maak ik een functie ‘get_size’ aan die ervoor zorgt dat de correcte grootte van bijvoorbeeld RAM weer wordt gegeven. Dit zet de GB achter 16.
Hierna laat ik de gebruiker kiezen welke gegevens hij op wil halen door middel van een nummer in te voeren. Hierna wordt de gemarkeerde keuze uitgevoerd en print je eigenlijk functies van psutil.
Bij keuze 5 wordt nog een try aangemaakt die checkt of de schijf waar de informatie van weergegeven wordt benaderbaar is. Als je bijvoorbeeld Bitlocker op een schijf hebt staan en de schijf is vergrendeld dan kan hij hem niet uitlezen.
Na de keuzes vraagt het programma nog of je nog iets wil checken. Als je hier ja op antwoord gaat hij terug naar de vraag wat je wilt checken. Als je nee antwoord dan eindigt het programma.
