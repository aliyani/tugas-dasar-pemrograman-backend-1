# belajar tipe data dictionary

customer = {"name" : "eko", "age":19, "address" : "banyuwangi"}

name = customer["name"]
age = customer["age"]
address = customer["address"]

customer["company"] = "x"
customer["name"] = "aliyani khoirun nisa"

del customer["address"]

for key, value in customer.items():
    print(f"{key}:{value}")