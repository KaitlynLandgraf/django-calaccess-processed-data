#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Custom administration panels for campaign models.
"""
from __future__ import unicode_literals
from django.contrib import admin
from calaccess_processed import models
from calaccess_raw.admin.base import BaseAdmin

@admin.register(models.Candidate)
class CandidateAdmin(BaseAdmin):
    """
    Custom admin for the Candidate model.
    """
    list_display = (
        'filer_id',
        'last_name',
        'first_name',
        'middle_name',
        'name_suffix',
        'election_year',
        'f501_filing_id',
        'last_f501_amend_id',
        'office',
        'district',
        'agency',
        'party',
    )

@admin.register(models.F460Summary)
class F460SummaryAdmin(BaseAdmin):
    """
    Custom admin for the F460Summary model.
    """
    list_display = (
        'filing_id',
        'amend_id',
        'filer_id',
        'filer_lastname',
        'filer_firstname',
        'total_contributions',
        'total_expenditures_made',
        'ending_cash_balance',
    )
