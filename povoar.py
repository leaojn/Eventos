from core.models import *
from user.models import *
from utils.models import *
from pagamento.models import *
import datetime

# para rodar o Script use
# pyhton manage.py shell
# exec(open('povoar.py').read())
print("Script para povoar tabela e estabelecer relacionamentos para teste")

# Criando um Usuario
usuario = Usuario()
usuario.username = "will"
usuario.email = "will@gmail.com"
usuario.nome = "Wildrimak"
usuario.password = "pbkdf2_sha256$36000$kG8PeNu2p4yf$TH6YRbpIXPoua4tOOkkubhD9Gdc8Oc850//xu8ykcEM="
usuario.save()
print("Usuario Criado")

# criando um Evento
evento = Evento()
evento.nome = "Festival de Musica de Pedro II"
evento.descricao = "Evento criado no intuito de promover o turismo em pedro II alem de disseminar cultura"
evento.valor = 0
evento.tipo_evento = TipoEvento.SEMINARIO
print("Evento Criado")

# criando um endereco para evento
endereco = Endereco()
endereco.pais = "Brasil"
endereco.estado = "Piaui"
endereco.logradouro = "Praca"
endereco.numero = "N/A"
endereco.cidade = "Teresina"
endereco.bairro = "Macauba"
endereco.cep = "64532-123"
endereco.save()
print("endereco para evento Criado")

# criando um periodo para evento
periodo = Periodo()
periodo.data_inicio = datetime.date.today()
periodo.data_fim = datetime.date(2019, 12, 1)
periodo.save()
print("periodo para evento Criado")

# voltando aos atributos de evento
evento.periodo = periodo
evento.endereco = endereco
evento.dono = usuario
evento.save()
print("evento finalizado")

# Criando outro Usuario
usuario_gerente = Usuario()
usuario_gerente.username = "jaum"
usuario_gerente.email = "jaum@gmail.com"
usuario_gerente.nome = "JaumNeto"
usuario_gerente.password = "pbkdf2_sha256$36000$kG8PeNu2p4yf$TH6YRbpIXPoua4tOOkkubhD9Gdc8Oc850//xu8ykcEM="
usuario_gerente.save()
print("Usuario Criado")

# criando/definindo um gerente de Evento
gerente = GerenciaEvento()
gerente.gerente = usuario_gerente
gerente.evento = evento
gerente.tipo_gerencia = TipoGerencia.STAFF
gerente.save()
print("gerente Criado e adicionado")

# criando uma tag
tag = Tag()
tag.nome = "Jazz"
tag.save()
print("Tag Criada")

# definindo tag a um evento
tag_evento = TagEvento()
tag_evento.tag = tag
tag_evento.evento = evento
tag_evento.save()
print("tag adicionada a um evento")

# definindo a mesma tag a um usuario
tag_usuario = TagUsuario()
tag_usuario.tag = tag
tag_usuario.usuario = usuario
tag_usuario.save()
print("tag adicionada a um usuario")

# criando um espaco fisico e atrelando a um evento e atividade
espaco = EspacoFisico()
espaco.nome = "Palco X"
espaco.tipoEspacoFisico = TipoEspacoFisico.AR_LIVRE
espaco.capacidade = 50
espaco.evento = evento
espaco.save()

# horario atividade
data = datetime.date.today()
hora_inicio = datetime.datetime.now().time()
hora_fim = datetime.datetime.now().time()
horario_atividade = HorarioAtividade.objects.create(data_inicio=data, data_fim=data, hora_inicio=hora_fim,
                                                    hora_fim=hora_fim)
# criando atividade Neutra
atividade_neutra = AtividadeAdministrativa()
atividade_neutra.nome = "Credenciamento"
atividade_neutra.descricao = "Credenciamento dos participantes"
atividade_neutra.evento = evento
atividade_neutra.horario_atividade = horario_atividade
atividade_neutra.espaco_fisico = espaco

print("Atividade Neutra Criada")

# criando um periodo para atividade Neutra
periodo_neutra = Periodo()
periodo_neutra.data_inicio = "2019-10-10"
periodo_neutra.data_fim = "2019-10-10"
periodo_neutra.save()
print("periodo criado")

# craindo um horario para atividade Neutra
horario_neutra = Horario()
horario_neutra.data = "2019-1-1"
horario_neutra.hora_inicio = "20:00"
horario_neutra.hora_fim = "22:00"
horario_neutra.save()

# voltando aos atributos de atividade Neutra
atividade_neutra.periodo = periodo_neutra
# atividade_neutra.horario = horario_neutra
atividade_neutra.save()
print("periodo para atividade Criado")

# criando um espaco fisico e atrelando a um evento e atividade
espaco = EspacoFisico()
espaco.nome = "Teresina Hall"
espaco.tipoEspacoFisico = TipoEspacoFisico.AR_LIVRE
espaco.capacidade = 50
espaco.evento = evento
espaco.save()

# horario atividade
data = datetime.date.today()
hora_inicio = datetime.datetime.now().time()
hora_fim = datetime.datetime.now().time()
horario_atividade = HorarioAtividade.objects.create(data_inicio=data, data_fim=data, hora_inicio=hora_fim,
                                                    hora_fim=hora_fim)

# criando atividade
atividade = AtividadePadrao()
atividade.nome = "Gilberto Gil"
atividade.descricao = "Show do Gilberto Gil"
atividade.valor = 0
atividade.espaco_fisico = espaco
atividade.evento = evento
atividade.horario_atividade = horario_atividade
print("Atividade Criada")

# craindo um horario para atividade
horario = Horario()
horario.data = "2019-1-1"
horario.hora_inicio = "20:00"
horario.hora_fim = "22:00"
horario.save()

# voltando aos atributos de atividade
atividade.periodo = periodo
# atividade.horario = horario
atividade.save()
print("periodo para atividade Criado")

# criando um espaco fisico e atrelando a um evento e atividade
espaco = EspacoFisico()
espaco.nome = "Palco Master"
espaco.tipoEspacoFisico = TipoEspacoFisico.AR_LIVRE
espaco.capacidade = 50
espaco.evento = evento

print("espaco fisico Criado")

# criar responsavel por atividade
responsavel = ResponsavelAtividade()
responsavel.responsavel = "Gilberto"
responsavel.descricao = "Musico Profissional"
responsavel.tipo_responsavel = TipoResponsavel.PADRAO
responsavel.atividade = atividade
print("responsavel por atividade Criado")

# criar instituicao
instituicao = Instituicao()
instituicao.nome = "Governo Do Piaui"
instituicao.save()
print("instituicao Criado")

# atrelar uma instituicao a um Evento
evento_instituicao = EventoInstituicao()
evento_instituicao.tipo_relacionamento = TipoInstituicao.REALIZACAO
evento_instituicao.evento_relacionado = evento
evento_instituicao.instituicao = instituicao
evento_instituicao.save()
print("instituicao atrelada a um evento")

# criando uma Trilha
trilha = Trilha()
trilha.nome = "Violonistas em P2"
trilha.valor = 0
trilha.evento = evento
trilha.save()
print("Trilha Criada")

# definir um usuario responsavel pela trilha
responsavel_trilha = ResponsavelTrilha()
responsavel_trilha.responsavel = usuario
responsavel_trilha.trilha = trilha
responsavel_trilha.tipo_responsavel_trilha = "staff"
print("responsavel por trilha definido")

# adicionando atividades a trilhas
atividade_trilha = AtividadePacote()
atividade_trilha.atividade = atividade
atividade_trilha.pacote = trilha
atividade_trilha.save()
print("atividade relacionada a uma trilha")

# Criando usuario para cliente em plataforma
usuario_inscrito = Usuario()
usuario_inscrito.username = "Kassio"
usuario_inscrito.email = "kassio@gmail.com"
usuario_inscrito.nome = "Kassio"
usuario_inscrito.password = "pbkdf2_sha256$36000$kG8PeNu2p4yf$TH6YRbpIXPoua4tOOkkubhD9Gdc8Oc850//xu8ykcEM="
usuario_inscrito.save()
print("Usuario Cliente Criado")

# criando uma inscricao
inscricao = Inscricao()
inscricao.status_inscricao = StatusInscricao.ATIVA
inscricao.tipo_inscricao = TipoInscricao.PARCIAL
inscricao.usuario = usuario_inscrito
inscricao.evento = evento
inscricao.save()
print("inscricao Criada")

# adicionando atividades a uma inscricao
item_inscricao = ItemInscricao()
item_inscricao.inscricao = inscricao
item_inscricao.atividade = atividade
item_inscricao.save()
print("Atividades adcioandas a inscricao")

# adicionando uma trilha a uma inscricao
trilha_inscricao = PacoteInscricao()
trilha_inscricao.pacote = trilha
trilha_inscricao.inscricao = inscricao
trilha_inscricao.save()
print("trilha adicionada a inscricao")

# criando o checkin
checkin = CheckinItemInscricao()
checkin.data = "2019-10-10"
checkin.hora = "10:00:00"
checkin.status = StatusCheckIn.VERIFICADO
checkin.gerente = evento.dono
checkin.save()
print("checkin criado")

# criando um cupom
cupom = Cupom()
cupom.evento = evento
cupom.porcentagem = 10
cupom.tipo = TipoCupom.SIMPLES
cupom.save()
print("cupom criado")

# efetuando o pagamento de uma inscricao
pagamento = Pagamento.objects.create(usuario_recebimento=evento.dono, inscricao=inscricao, cupom_codigo=cupom.codigo)

print("pagamento efetuado")
