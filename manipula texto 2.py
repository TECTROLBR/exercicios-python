cid = input('digite um nome de uma cidade? ').strip()
cid = cid.upper()
lit = cid.split()
pes = 'SANTO' in lit[0]
print('esta cidade começa com o nome "SANTO"?\n  {}'.format(pes))