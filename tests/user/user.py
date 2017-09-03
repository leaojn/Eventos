from django.test import TestCase
from user.models import *
from utils.models import *
from core.models import *
from pagamento.models import *


class TestUser(TestCase):
    def setUp(self):
        usuario = Usuario(username="t", email="teste@ail.com", nome="teste",
                          password="pbkdf2_sha256$36000$kG8PeNu2p4yf$TH6YRbpIXPoua4tOOkkubhD9Gdc8Oc850//xu8ykcEM=")
        usuario.save()
        self.user = usuario

        novo_usuario = Usuario(username="tsad", email="tesadsdasdte@ail.com", nome="dasdasdaf",
                               password="pbkdf2_sha256$36000$kG8PeNu2p4yf$TH6YRbpIXPoua4tOOkkubhD9Gdc8Oc850//xu8ykcEM=")
        novo_usuario.save()
        self.new_user = novo_usuario

        endereco = Endereco.objects.create(pais="Brasil", estado="Piaui", logradouro="Praca", numero="3130",
                                           cidade="Teresina",
                                           bairro="Macauba", cep="64532-123")

        endereco.save()
        self.edereco = endereco

        periodo = Periodo.objects.create(data_inicio=datetime.date.today(), data_fim=datetime.date(2018, 1, 1))
        periodo.save()
        self.periodo = periodo

        evento = Evento(nome="Festival",
                        descricao="Evento criado no intuito de promover o turismo em pedro II alem de disseminar cultura",
                        valor=0, tipo_evento=TipoEvento.SEMINARIO, periodo=self.periodo, endereco=endereco,
                        dono=usuario)
        evento.save()
        self.evento = evento

        new_evento = Evento(nome="Festival123",
                            descricao="Evento 2 criado no intuito de promover o turismo em pedro II alem de disseminar cultura",
                            valor=0, tipo_evento=TipoEvento.CONGRESSO, periodo=self.periodo, endereco=endereco,
                            dono=novo_usuario)
        new_evento.save()
        self.new_evento = new_evento

        atividade = AtividadeContinua(nome="teste", descricao="Credenciamento dos participantes", evento=evento,
                                      periodo=periodo)
        atividade.save()
        self.atividade = atividade

        inscricao = Inscricao(usuario=novo_usuario, evento=evento)
        inscricao.save()
        self.inscricao = inscricao


        # self.new_inscricao = new_inscricao

        pagamento = Pagamento(status=StatusPagamento.PAGO, usuario_recebimento=evento.dono, data="2017-10-10",
                              hora="20:00", valor_pagamento=0, inscricao=inscricao)
        pagamento.save()
        self.pagamento = pagamento

        return inscricao

    def create_user(self):
        usuario = Usuario(username="Will", email="teste@teste", nome="Will")
        return usuario

    def usuario(self):
        return Usuario()

    def create_item_inscricao(self):
        item_inscricao = ItemInscricao()
        return item_inscricao

    def item_inscricao(self):
        return ItemInscricao()

    def create_inscricao(self):
        inscricao = Inscricao()
        return inscricao

    def inscricao(self):
        return Inscricao()

    def create_checkin(self):
        checkin = CheckinItemInscricao()
        return checkin

    def checkin(self):
        return CheckinItemInscricao()
