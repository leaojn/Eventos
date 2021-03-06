from django.db import models
from localflavor.br.br_states import STATE_CHOICES
import datetime
from django.core.exceptions import ValidationError
from django.core import validators
import re


class Periodo(models.Model):
    data_inicio = models.DateField("Data inicio", blank=True, null=False)
    data_fim = models.DateField("Data fim", blank=True, null=False)

    class Meta:
        verbose_name = "Periodo"
        verbose_name_plural = "Periodos"

    def validate_periodo(self):
        if self.data_inicio < datetime.date.today():
            raise ValidationError("Periodo tem que ser maior que a data atual")
        if self.data_fim < self.data_inicio:
            raise ValidationError("Data final tem que ser maior ou igual a data inicial")

    def clean(self):
        super(Periodo, self).clean()
        self.validate_periodo()

    def save(self, *args, **kwargs):
        self.full_clean()
        super(Periodo, self).save()

    def __str__(self):
        return self.data_inicio.__str__() + " para " + self.data_fim.__str__()


class Endereco(models.Model):
    pais = models.TextField(blank=False, null=False)
    cidade = models.TextField(blank=False, null=False)
    bairro = models.TextField(blank=False, null=False)
    logradouro = models.TextField(blank=True, null=False)
    numero = models.TextField(blank=False, null=False)
    cep = models.CharField(max_length=9, blank=False, validators=[
        validators.RegexValidator(re.compile(r"^\d{8}$|^\d{5}-\d{3}$"),
                                  message="Informe um cep valido no formato 88888888 ou 88888-888", code="invalid")])
    estado = models.TextField(blank=False, null=False)

    class Meta:
        verbose_name = "Endereco"
        verbose_name_plural = "Enderecos"

    def __str__(self):
        return self.pais

    def save(self, *args, **kwargs):
        self.full_clean()
        super(Endereco, self).save()


class Horario(models.Model):
    data = models.DateField("Data inicio", blank=True, null=True)
    hora_inicio = models.TimeField("Hora inicio", blank=True, null=False)
    hora_fim = models.TimeField("Hora Fim", blank=True, null=False)

    class Meta:
        verbose_name = "Horario"
        verbose_name_plural = "Horario"

    def __str__(self):
        return self.hora_inicio.__str__() + "  para  " + self.hora_fim.__str__()

    def validate_horario(self):
        if self.hora_inicio > self.hora_fim:
            raise ValidationError("Periodo tem que ser maior que a data atual")

    def clean(self):
        super(Horario, self).clean()
        self.validate_horario()

    def save(self, *args, **kwargs):
        self.full_clean()
        super(Horario, self).save()


class HorarioAtividade(models.Model):
    data_inicio = models.DateField("Data inicio", blank=False, null=False)
    data_fim = models.DateField("Data fim", blank=False, null=False)
    hora_inicio = models.TimeField("Hora inicio", blank=False, null=False)
    hora_fim = models.TimeField("Hora Fim", blank=False, null=False)

    def get_dias_atividade(self):
        dias = self.data_fim - self.data_inicio
        dias = dias.days
        dict = {}
        for i in range(dias + 1):
            dict[str(i)] = self.data_inicio + datetime.timedelta(i)
        return dict

    def validate_horario(self):
        if self.hora_inicio > self.hora_fim:
            raise ValidationError("Periodo tem que ser maior que a data atual")

    def clean(self):
        super(HorarioAtividade, self).clean()
        self.validate_horario()

    def save(self, *args, **kwargs):
        self.full_clean()
        super(HorarioAtividade, self).save()


class HorarioAtividadeContinua(Horario):
    atividade = models.ForeignKey("core.AtividadeContinua",
                                  verbose_name="Atividade",
                                  related_name="Atividade",
                                  default="")

    class Meta:
        verbose_name = "Horario_da_atividdade"
        verbose_name_plural = "Horarios_da_ativiade "


class Observador(models.Model):
    observado = models.ForeignKey("utils.Observador",
                                  verbose_name="Observador",
                                  related_name="Observador",
                                  default="")

    def atualizar(self):
        return "sobrescreva"


class Notificador(Observador):
    class Meta:
        verbose_name = "Notificador"
        verbose_name_plural = "notificadores "

    def atualizar(self, msg):
        "enviar email para usuarios da atividade"
        return True


class Observado(models.Model):
    def addObservador(self, observador):
        observador.observado = self
        return True

    def removeObservador(self, observador):
        observador.observado = None
        return True

    def notificar(self, msg):
        for observador in self.Observador:
            observador.atualizar(msg)


class MsgFactory():
    def gerar_msg_simples(self, atributo):
        msg = MsgSimples()
        msg.atual = str(atributo)
        return msg

    def gerar_msg_completa(self, atributo):
        msg = MsgCompleta()
        msg.atual = str(atributo)
        msg.data = datetime.now()
        return msg


class MsgSimples(models.Model):
    atual = models.TextField(default="")

    def str(self):
        return "novo " + self.atual + "."


class MsgCompleta(MsgSimples):
    data = models.DateTimeField(null=False)
    anterior = models.TextField(default="")

    def str(self):
        return "Data :" + self.data + " Estado antigo :" + self.anterior + " Estado atual :" + self.atual + "."
