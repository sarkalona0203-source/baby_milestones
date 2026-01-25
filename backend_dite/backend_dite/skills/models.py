from django.db import models
from django.core.exceptions import ValidationError


class Skill(models.Model):
    CATEGORY_CHOICES = [
        ("motor", "Motorika"),
        ("speech", "Řeč"),
        ("social", "Sociální vývoj"),
        ("cognitive", "Kognitivní"),
    ]

    name = models.CharField(max_length=200)
    description = models.TextField()

    min_age_months = models.PositiveIntegerField()
    max_age_months = models.PositiveIntegerField()

    category = models.CharField(
        max_length=100,
        choices=CATEGORY_CHOICES,
        default="motor"
    )

    icon = models.CharField(
        max_length=100,
        blank=True,
        help_text="Název ikony na frontendu (bez cesty)"
    )

    def clean(self):
        if self.min_age_months > self.max_age_months:
            raise ValidationError(
                "min_age_months nemůže být větší než max_age_months"
            )

    def __str__(self):
        return self.name


class NutritionGuide(models.Model):
    min_age_months = models.PositiveIntegerField()
    max_age_months = models.PositiveIntegerField()

    title = models.CharField(max_length=200)
    text = models.TextField()

    type = models.CharField(
        max_length=20,
        choices=[
            ("feeding", "Doporučení"),
            ("warning", "Warning"),
        ]
    )

    def clean(self):
        if self.min_age_months > self.max_age_months:
            raise ValidationError(
                "min_age_months nemůže být větší než max_age_months"
            )

    def __str__(self):
        return f"{self.title} ({self.min_age_months}–{self.max_age_months} m)"