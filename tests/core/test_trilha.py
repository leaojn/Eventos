import datetime
from django.utils import timezone
from utils.models import *
from user.models import *
from core.models import *
from .core import TestCore


class TestePacte(TestCore):
    def test_validar_criacao_de_trilha(self):
        self.create_trilha()
