class Usuario:
    def __init__(self, id, preferencias):
        self.id = id
        self.preferencias = preferencias  # Preferências é um dicionário com listas
        self.historico = []

    def avaliar_filme(self, filme, avaliacao):
        self.historico.append({'filme': filme, 'avaliacao': avaliacao})


class Filme:
    def __init__(self, titulo, genero, diretor, atores):
        self.titulo = titulo
        self.genero = genero
        self.diretor = diretor
        self.atores = atores


class SistemaRecomendacao:
    def __init__(self, base_dados):
        self.base_dados = base_dados

    def recomendar(self, usuario):
        recomendacoes = []
        for filme in self.base_dados.filmes:
            if self.corresponde_preferencias(filme, usuario.preferencias):
                recomendacoes.append(filme)
        return recomendacoes

    def corresponde_preferencias(self, filme, preferencias):
        if 'genero' in preferencias and filme.genero in preferencias['genero']:
            return True
        if 'atores' in preferencias:
            if any(ator in filme.atores for ator in preferencias['atores']):
                return True
        if 'diretor' in preferencias and filme.diretor == preferencias['diretor']:
            return True
        return False


class BaseDados:
    def __init__(self):
        self.filmes = []
        self.usuarios = []

    def adicionar_filme(self, filme):
        self.filmes.append(filme)

    def adicionar_usuario(self, usuario):
        self.usuarios.append(usuario)


# Exemplo de uso
if __name__ == "__main__":
    # Inicializando a base de dados e o sistema de recomendação
    base_de_dados = BaseDados()
    sistema = SistemaRecomendacao(base_de_dados)

    # Adicionando filmes à base de dados
    base_de_dados.adicionar_filme(Filme("Filme A", "Ação", "Diretor A", ["Ator A", "Ator B"]))
    base_de_dados.adicionar_filme(Filme("Filme B", "Comédia", "Diretor B", ["Ator C", "Ator D"]))
    base_de_dados.adicionar_filme(Filme("Filme C", "Ação", "Diretor C", ["Ator A", "Ator E"]))

    # Criando um usuário e adicionando ao sistema
    usuario = Usuario(1, {
        "genero": ["Ação"],
        "atores": ["Ator A"],
        "diretor": "Diretor A"
    })
    base_de_dados.adicionar_usuario(usuario)

    # Obtendo recomendações para o usuário
    recomendacoes = sistema.recomendar(usuario)
    for filme in recomendacoes:
        print(f"Recomendado: {filme.titulo} - Gênero: {filme.genero}, Diretor: {filme.diretor}, Atores: {', '.join(filme.atores)}")
