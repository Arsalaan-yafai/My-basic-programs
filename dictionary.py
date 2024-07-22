d1={"arsalaan":"yafai",
    "abdul rehman":"american",
    "uzair":{"arsalaan":'gappu',"abdul rahman":"MR.bumble","zaid":"mota"},
    "numan":"lumdi",
    "hussain":"Ainakchi",
    "gucci zaid":"Criminal"}
print(type(d1))
d1["imran"] = "150RS"
d1["Junaid"] ="bakery"
d1.update({"Awais":"Chor"})
print(d1)
d2 = d1.copy()
del d2 ["Junaid"]
print(d2)
print(d1.keys())
print(d1.items())


