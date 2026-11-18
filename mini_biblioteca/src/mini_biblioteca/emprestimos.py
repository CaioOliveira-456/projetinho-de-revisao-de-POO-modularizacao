from livros import Livro
from usuarios import Usuario

class Emprestimo(Livro, Usuario):
    def __init__(self, livro: Livro, usuario: Usuario):
        if not livro.disponivel:
            raise ValueError

        self.livro = livro
        self.usuario = usuario
        self.ativo = True

        livro.disponivel = False

    def devolver(self):
        if self.ativo:
            self.ativo = False 
            self.livro.disponivel = True


