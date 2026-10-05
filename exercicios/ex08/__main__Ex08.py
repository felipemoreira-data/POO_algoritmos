from ex08 import ContaBancaria

p1 = ContaBancaria(id = 111, nome= 'Ana', saldo = 4_000)
p1.sacar(-200)
p1.depositar(-300)
p1.titular = 'Nonato'
p1.saldo = 0
print(p1.__dict__)
