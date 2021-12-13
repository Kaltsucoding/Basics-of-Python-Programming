# Kysytään käyttäjältä etunimi ja sukunimi. 
# Tulostetaan etunimen pituinen merkkijono ensimmäisen kirjaimen mukaan ja tulostetaan sukunimi väärinpäin alkaen lopusta

Etunimi = str(input("Anna Etunimesi: "))
print(Etunimi[0] * len(Etunimi))
Sukunimi = str(input("Anna Sukunimesi: "))
print(Sukunimi[::-1])