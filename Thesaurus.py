from matplotlib import pyplot as plt
import pandas as pd

thesaurus_cogent = pd.read_excel(r"C:\Users\vandewsa\Documents\train the Trainer\datasetTTT2.xlsx")
print(thesaurus_cogent)

aantal_dmg = thesaurus_cogent.loc[thesaurus_cogent["Instelling"] == "Designmuseum Gent"].count()[0]
print(aantal_dmg)

aantal_hva = thesaurus_cogent.loc[thesaurus_cogent["Instelling"] == "Het Huis van Alijn"].count()[0]
aantal_stam = thesaurus_cogent.loc[thesaurus_cogent["Instelling"] == "STAM"].count()[0]
aantal_im = thesaurus_cogent.loc[thesaurus_cogent["Instelling"] == "Industriemuseum"].count()[0]
aantal_archief = thesaurus_cogent.loc[thesaurus_cogent["Instelling"] == "Archief Gent"].count()[0]

colors = ["#CD5C5C", "#F08080", "#FA8072", "#E9967A", "#FFA07A"]
labels = ["Archief Gent", "Industriemuseum", "STAM", "Huis van Alijn", "Design Museum Gent"]
explode = [0.3,0,0.2,0,0]
slices = [aantal_archief, aantal_im, aantal_stam, aantal_hva, aantal_dmg]
plt.pie(slices, labels=labels, colors=colors, explode=explode, startangle=90, autopct="´%1.1f%%")
plt.show()


aat = thesaurus_cogent[thesaurus_cogent["bron"].str.contains("aat", case=False)].count()[0]
print(aat)