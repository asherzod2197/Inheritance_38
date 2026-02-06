# 38. Kino chiptalari

class Ticket:
    def __init__(self, ticket_type, price):
        self.ticket_type = ticket_type    # "Kattalar", "Bolalar", "Talaba" va h.k.
        self.price = price                # narx ($)

    def get_price(self):
        """Chipta narxi"""
        return self.price

    def __str__(self):
        return f"{self.ticket_type:12} | {self.price:6.2f}$"


# -----------------------------------------------
# Voris sinflar (chiroyli chiqish + emoji)
# -----------------------------------------------

class AdultTicket(Ticket):
    def __str__(self):
        return f"👨‍🦰 {self.ticket_type:10} → {self.price:6.2f}$"


class ChildTicket(Ticket):
    def __str__(self):
        return f"👶 {self.ticket_type:10} → {self.price:6.2f}$"


# Qo‘shimcha variantlar (foydali bo‘lishi mumkin)
class StudentTicket(Ticket):
    def __str__(self):
        return f"🎓 {self.ticket_type:10} → {self.price:6.2f}$"


class SeniorTicket(Ticket):
    def __str__(self):
        return f"👴 {self.ticket_type:10} → {self.price:6.2f}$"


# --------------------------------------------------
# Kino chiptalari ro‘yxatini chiqarish
# --------------------------------------------------

def show_cinema_tickets(tickets):
    print("\n" + "═" * 55)
    print("       KINO CHIPTALARI — NARX RO‘YXATI       ".center(55))
    print("═" * 55)
    print("Chipta turi          Narxi ($)")
    print("─" * 55)

    total = 0

    for ticket in tickets:
        print(ticket)
        total += ticket.get_price()

    print("─" * 55)
    print(f"Jami chiptalar narxi:          {total:8.2f}$")
    print("═" * 55 + "\n")


# Test ma'lumotlari
chiptalar = [
    AdultTicket("Kattalar", 12.00),
    ChildTicket("Bolalar (3-12 yosh)", 6.50),
    StudentTicket("Talabalar (talaba guvohnomasi bilan)", 8.00),
    SeniorTicket("Keksalar (60+)", 7.00),
    AdultTicket("Kattalar (3D)", 15.00),
    ChildTicket("Bolalar (3D)", 8.00),
]

show_cinema_tickets(chiptalar)


# Sizning misol qiymatlaringiz bilan:
print("\nSizning misol chiptalaringiz:\n")
misol_chiptalar = [
    AdultTicket("Kattalar", 10),
    ChildTicket("Bolalar", 5),
]

show_cinema_tickets(misol_chiptalar)
