from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Inquiry",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("full_name", models.CharField(max_length=120, verbose_name="Full name")),
                ("email", models.EmailField(max_length=254, verbose_name="Email address")),
                ("phone", models.CharField(blank=True, max_length=40, verbose_name="Phone")),
                ("session_type", models.CharField(choices=[("legacy", "Legacy — Generational Portraits"), ("celebration", "Celebration of Life"), ("headshots", "Headshots"), ("dogs", "Dogs — Companion Portraits"), ("unsure", "Not sure yet")], default="unsure", max_length=20, verbose_name="Session type")),
                ("preferred_date", models.DateField(blank=True, help_text="Approximate is fine — a firm date is set on the call.", null=True, verbose_name="Preferred date")),
                ("message", models.TextField(help_text="Tell Neil a little about what you have in mind.", verbose_name="Message")),
                ("contacted", models.BooleanField(default=False, verbose_name="Contacted?")),
                ("created_at", models.DateTimeField(auto_now_add=True)),
            ],
            options={
                "verbose_name": "Inquiry",
                "verbose_name_plural": "Inquiries",
                "ordering": ["-created_at"],
            },
        ),
    ]
