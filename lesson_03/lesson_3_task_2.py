from smarthone import Smartphone

catalog = [
    Smartphone("LQ", "534", "+79080069155"),
    Smartphone("SMSNG", "10+", "+79123261018"),
    Smartphone("Sony", "7x", "+79991514146")
]

for smartphone in catalog:
    print(f"{smartphone.marka} - {smartphone.model} - {smartphone.number}")