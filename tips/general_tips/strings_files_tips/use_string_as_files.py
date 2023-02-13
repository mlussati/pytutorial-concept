import io

# Outra opcao e ler diretamente da string, mascarando a string como um arquivo aberto.


# O módulo io fornece a classe StringIO que converte uma string 
# em um objeto semelhante a um arquivo com operações familiares, como read() e readline().
# with io.StringIO('Hello,\nworld!') as source:
#     print(source.readlines())

# Para usar 0 StringIO como destino, crie um fluxo vazio e grave nele. O _io.StringIO.write()
#  retorna o número de bytes gravados, assim como sua contraparte convencional.
with io.StringIO() as dest:
    dest.write('Hello,\n')
    dest.write('World!')
    # Or pass dest to another function
    print(dest.getvalue())