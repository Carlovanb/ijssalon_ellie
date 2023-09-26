def presenteer(invoer_dict, totaal):
    for item, bedrag in invoer_dict.items():
        print(f"{item} : {bedrag} euro")
    
    print("==================")
    print(f"totaal : {totaal} euro")
       
mijn_dict = {'vis': 10, 'vlees': 25, 'overig': 15}
totaal = 50

presenteer(mijn_dict, totaal) 