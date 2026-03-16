from database import create_table
from isci_repository import add_isci, get_all_isciler
from statistika_department import en_yuksek_maas

create_table()

add_isci("Elvin", 7500)
add_isci("Yusif", 4500)
add_isci("Seid", 6500)

print(get_all_isciler())
print(en_yuksek_maas())