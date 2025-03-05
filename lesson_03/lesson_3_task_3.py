from address import Address
from mail import Mailing

address1 = Address("12345", "Курган", "Ленина", 12, 30)
address2 = Address("51412", "Курган", "Бажова", 14, 99)

mail = Mailing(address1, address2, 1000, 987514)


print(mail)