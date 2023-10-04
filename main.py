class Editora:
  def __init__ (self, codigoeditora, razaosocial, nomecontato, telefone):
      self.codigoeditora = codigoeditora
      self.razaosocial = razaosocial
      self.nomecontato = nomecontato
      self.telefone = telefone
  def setCodigoeditora(self, codigoeditora):
      self.Codigoeditora = codigoeditora
  def setRazaosocial(self, razaosocial):
      self.razaosocial = razaosocial
  def setNomecontato(self, nomecontato):
      self.nomecontato = nomecontato
  def setTelefone(self, telefone):
      self.telefone = telefone
  def getCodigoeditora(self):
      return self.codigoeditora
  def getRazaoSocial(self):
      return self.razaosocial
  def getNomecontato(self):
      return self.nomecontato
  def getTelefone(self):
      return self.telefone

class Livro:
  def __init__ (self, codigolivro, titulo, codigoISBN, editora):
    self.codigolivro = codigolivro
    self.titulo = titulo
    self.codigoISBN = codigoISBN
    self.editora = editora
  def setCodigolivro(self, codigolivro):
    self.codigolivro = codigolivro
  def setTitulo(self, titulo):
    self.titulo = titulo
  def setCodigoISBN(self, codigoISBN):
    self.codigoISBN = codigoISBN
  def setEditora(self, editora):
    self.editora = editora
  def getCodigolivro(self):
    return self.codigolivro
  def getTitulo(self):
    return self.titulo
  def getCodigoISBN(self):
    return self.codigoISBN
  def getEditora(self):
    return self.editora
    
listaed = []
while True:
  print('1 - Cadastrar Editora')
  print('2 - Cadastrar Livro')
  print('3 - Pesquisar Editora')
  print('4 - Pesquisar Livro')
  print('5 - Sair')
  função = int(input('Digite o número da função que você deseja realizar: '))

  if função == 1:
    while True:
      operação = input('Cadastrar editora? [S/N]: ')
      if operação == 'S' or operação == 's':
        codigoeditora = int(input('Código da editora: '))
        razaosocial = input('Razão Social: ')
        nomecontato = input('Nome do contato: ')
        telefone = input('Telefone: ')
        editora = Editora(codigoeditora, razaosocial, nomecontato, telefone)
        listaed.append(editora)
      if operação == 'N' or operação == 'n':
        break

  if função == 2:
      Livros = []
      while True:
        cadastrolivro = input('Cadastrar livro? [S/N]: ')
        if cadastrolivro == 'S' or cadastrolivro == 's':
          codigolivro = int(input('Código do livro: '))
          titulo = input('Titulo: ')
          codigoISBN = input('Codigo ISBN: ')
          editora = int(input('Código da editora: '))
          for l in listaed:
              if editora == l.getCodigoeditora():
                    editora = l
        livro = Livro(codigolivro, titulo, codigoISBN, editora)
        Livros.append(livro)
        if cadastrolivro == 'N' or cadastrolivro == 'n':
          break

  if função == 3:
    razaoSocial = input('nome da editora: ')
    for l in listaed:
            if razaoSocial == l.getRazaoSocial():
                print('INFORMAÇÕES DA EDITORA')
                print(f'Código: {l.getCodigoeditora()}')
                print(f'Razão Social: {l.getRazaoSocial()}')
                print(f'Nome do Contato: {l.getNomecontato()}')
                print(f'Telefone: {l.getTelefone()}')

  if função == 4:
    titulo = input('Título do livro: ')
    for l in Livros:
      if titulo == l.getTitulo():
        print('INFORMAÇÕES DO LIVRO')
        print(f'Código: {l.getCodigolivro()}')
        print(f'Título: {l.getTitulo()}')
        print(f'Código ISBN: {l.getCodigoISBN()}')
        print(f'Editora: {l.editora.getRazaoSocial()}')

  if função == 5:
    break