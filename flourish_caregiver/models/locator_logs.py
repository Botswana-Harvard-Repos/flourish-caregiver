import arrow

from django.db.models.deletion import PROTECT
from django.db import models

from django_crypto_fields.fields import EncryptedTextField
from edc_base.model_managers import HistoricalRecords
from edc_base.model_mixins import BaseUuidModel
from edc_base.model_validators import datetime_not_future
from edc_base.utils import get_utcnow

from ..choices import LOCATOR_LOG_STATUS


class LocatorLog(BaseUuidModel):
    """A system model to track an RA\'s attempts to confirm a Plot
    (related).
    """

    study_maternal_identifier = models.CharField(
        verbose_name="Study maternal Subject Identifier",
        max_length=50,
        unique=True)

    report_datetime = models.DateTimeField(
        verbose_name="Report date",
        default=get_utcnow)

    history = HistoricalRecords()

    def __str__(self):
        return self.study_maternal_identifier


class LocatorLogEntry(BaseUuidModel):
    """A model completed by the user to track an RA\'s attempts to
    confirm a Plot.
    """

    locator_log = models.ForeignKey(LocatorLog, on_delete=PROTECT)

    report_datetime = models.DateTimeField(
        verbose_name="Report date",
        validators=[datetime_not_future],
        default=get_utcnow)

    report_date = models.DateField(
        help_text='date value of report_datetime for unique constraint')

    log_status = models.CharField(
        verbose_name='What is the status of the locator?',
        max_length=25,
        choices=LOCATOR_LOG_STATUS)

    comment = EncryptedTextField(
        verbose_name="Comments",
        max_length=250,
        null=True,
        blank=True,)

    history = HistoricalRecords()

    def save(self, *args, **kwargs):
        self.report_date = arrow.Arrow.fromdatetime(
            self.report_datetime, self.report_datetime.tzinfo).to('utc').date()
        super().save(*args, **kwargs)

    def __str__(self):
        return f'{self.locator_log.study_maternal_identifier} ({self.report_datetime})'

    class Meta:
        unique_together = ('locator_log', 'report_datetime')
        ordering = ('report_datetime', )
