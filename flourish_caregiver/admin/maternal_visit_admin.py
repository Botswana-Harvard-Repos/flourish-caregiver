from dateutil import relativedelta
from django.apps import apps as django_apps
from django.contrib import admin
from django.urls.base import reverse
from django.urls.exceptions import NoReverseMatch
from django_revision.modeladmin_mixin import ModelAdminRevisionMixin
from edc_base.utils import get_utcnow
from edc_constants.constants import NO, POS, YES
from edc_fieldsets import FieldsetsModelAdminMixin, Insert
from edc_model_admin import (
    ModelAdminFormAutoNumberMixin, ModelAdminInstitutionMixin,
    ModelAdminNextUrlRedirectMixin,
    ModelAdminNextUrlRedirectError, ModelAdminReplaceLabelTextMixin)
from edc_model_admin import audit_fieldset_tuple

from edc_visit_schedule.fieldsets import visit_schedule_fieldset_tuple
from edc_visit_tracking.modeladmin_mixins import VisitModelAdminMixin

from ..admin_site import flourish_caregiver_admin
from ..forms import MaternalVisitForm
from ..helper_classes import MaternalStatusHelper
from ..models import MaternalVisit
from .exportaction_mixin import ExportActionMixin


class ModelAdminMixin(ModelAdminNextUrlRedirectMixin, ModelAdminFormAutoNumberMixin,
                      ModelAdminRevisionMixin, ModelAdminReplaceLabelTextMixin,
                      ModelAdminInstitutionMixin, ExportActionMixin,
                      FieldsetsModelAdminMixin):
    list_per_page = 10
    date_hierarchy = 'modified'
    empty_value_display = '-'

    def redirect_url(self, request, obj, post_url_continue=None):
        redirect_url = super().redirect_url(
            request, obj, post_url_continue=post_url_continue)
        if request.GET.dict().get('next'):
            url_name = request.GET.dict().get('next').split(',')[0]
            attrs = request.GET.dict().get('next').split(',')[1:]
            options = {k: request.GET.dict().get(k)
                       for k in attrs if request.GET.dict().get(k)}
            if (obj.require_crfs == NO):
                del options['appointment']
            try:
                redirect_url = reverse(url_name, kwargs=options)
            except NoReverseMatch as e:
                raise ModelAdminNextUrlRedirectError(
                    f'{e}. Got url_name={url_name}, kwargs={options}.')
        return redirect_url


def get_difference(birth_date=None):
    difference = relativedelta.relativedelta(
        get_utcnow().date(), birth_date)
    return difference.years


@admin.register(MaternalVisit, site=flourish_caregiver_admin)
class MaternalVisitAdmin(ModelAdminMixin, VisitModelAdminMixin,
                         admin.ModelAdmin):
    form = MaternalVisitForm

    fieldsets = (
        (None, {
            'fields': [
                'appointment',
                'report_datetime',
                'reason',
                'reason_missed',
                'study_status',
                'info_source',
                'info_source_other',
                'is_present',
                'survival_status',
                'last_alive_date',
                'comments'
                ]
            }),
        visit_schedule_fieldset_tuple,
        audit_fieldset_tuple
        )

    radio_fields = {
        'reason': admin.VERTICAL,
        'study_status': admin.VERTICAL,
        'info_source': admin.VERTICAL,
        'is_present': admin.VERTICAL,
        'survival_status': admin.VERTICAL,
        # 'tb_participation': admin.VERTICAL,
        }

    # def get_key(self, request, obj=None):
        # consent_model = 'subjectconsent'
        # subject_identifier = request.GET.get('subject_identifier')
        # maternal_status_helper = MaternalStatusHelper(
            # subject_identifier=subject_identifier)
        # consent_model_cls = django_apps.get_model(f'flourish_caregiver.{consent_model}')
        # consent_obj = consent_model_cls.objects.filter(
            # subject_identifier=subject_identifier
            # )
        # if (consent_obj and get_difference(consent_obj[0].dob)
                # >= 18 and maternal_status_helper.hiv_status == POS and
                # consent_obj[0].citizen == YES):
            # return 'tb_2_months'
            #
    # conditional_fieldlists = {
        # 'tb_2_months': Insert('tb_participation', after='last_alive_date'),
        # }
