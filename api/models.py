# -*- coding: utf-8 -*-
"""
Custom models for users that will be used accross the store app.
"""
from django.contrib.auth.models import (
    AbstractBaseUser, PermissionsMixin, UserManager
)
from django.core.mail import EmailMultiAlternatives
from django.db import models
from django.utils.translation import ugettext_lazy as _

from core.db.models import TimeStampedModel


class User(AbstractBaseUser, PermissionsMixin, TimeStampedModel):
    """
    Custom user model to be used accross the store app.
    """
    email = models.CharField(
        unique=True,
        max_length=60,
        verbose_name=_('email')
    )
    first_name = models.CharField(
        blank=True,
        max_length=60,
        verbose_name=_('first name')
    )
    last_name = models.CharField(
        blank=True,
        max_length=60,
        verbose_name=_('last name')
    )
    birthdate = models.DateField(
        null=True,
        blank=True,
        verbose_name=_('birthdate')
    )

    # Control fields
    is_active = models.BooleanField(
        default=False,
        verbose_name=_('is active')
    )
    is_staff = models.BooleanField(
        default=False,
        verbose_name=_('is staff')
    )

    objects = UserManager()

    USERNAME_FIELD = 'email'

    class Meta:
        verbose_name = _('user')
        verbose_name_plural = _('users')

    def get_full_name(self):
        """
        Return the full name for the current user, composed by its first name
        and its last name with a space between.
        """
        return '{0} {1}'.format(self.first_name, self.last_name)

    def get_short_name(self):
        """
        Return the short name for the current user, composed by its first name.
        """
        return self.first_name

    def send_email(self, subject, body, html=None, from_email=None, **kwargs):
        """
        Send an email which can have an html alternative to the current user.
        """
        email = EmailMultiAlternatives(
            subject=subject,
            body=body,
            from_email=from_email,
            to=[self.email],
            **kwargs
        )

        if html is not None:
            email.attach_alternative(html, 'text/html')

        email.send()
