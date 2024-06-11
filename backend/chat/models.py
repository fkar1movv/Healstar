from django.db import models

from users.models import Doctor, Patient


class Chat(models.Model):
    patient: Patient = models.ForeignKey(Patient, on_delete=models.DO_NOTHING, related_name='p')
    doctor: Doctor = models.ForeignKey(Doctor, on_delete=models.DO_NOTHING, related_name='d')

    def __str__(self):
        return f'Chat between Doctor {self.doctor.full_name} and Patient {self.patient.full_name}'

    class Meta:
        db_table = 'chat'


class ChatHistory(models.Model):
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    chat = models.ForeignKey(Chat, on_delete=models.DO_NOTHING)
    sender = models.CharField(max_length=1, null=True)  # can be either d (doctor) or p (patient)

    def __str__(self):
        return f'Chat History - {self.chat}'

    class Meta:
        db_table = 'chat_history'
