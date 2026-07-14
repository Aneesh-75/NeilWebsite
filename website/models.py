from django.db import models


class Inquiry(models.Model):
    SESSION_CHOICES = [
        ("legacy", "Legacy — Generational Portraits"),
        ("celebration", "Celebration of Life"),
        ("headshots", "Headshots"),
        ("dogs", "Dogs — Companion Portraits"),
        ("unsure", "Not sure yet"),
    ]

    full_name = models.CharField("Full name", max_length=120)
    email = models.EmailField("Email address")
    phone = models.CharField("Phone", max_length=40, blank=True)
    session_type = models.CharField(
        "Session type",
        max_length=20,
        choices=SESSION_CHOICES,
        default="unsure",
    )
    preferred_date = models.DateField(
        "Preferred date",
        blank=True,
        null=True,
        help_text="Approximate is fine — a firm date is set on the call.",
    )
    message = models.TextField("Message", help_text="Tell Neil a little about what you have in mind.")
    contacted = models.BooleanField("Contacted?", default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Inquiry"
        verbose_name_plural = "Inquiries"
        ordering = ["-created_at"]

    def __str__(self):
        return f"{self.full_name} — {self.get_session_type_display()}"
