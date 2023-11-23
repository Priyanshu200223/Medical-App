# Generated by Django 4.2.7 on 2023-11-22 18:44

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("Accounts", "0003_healthcareprovider_fees"),
    ]

    operations = [
        migrations.AddField(
            model_name="healthcareprovider",
            name="about",
            field=models.TextField(
                default="Greetings, I am Dr. [Your Name], a dedicated and compassionate healthcare professional with [X] years of experience in [specialty]. Holding a [Degree] from [Institution], my commitment to patient well-being extends beyond diagnosis and treatment. Proficient in [specific skills], I strive for excellence in providing evidence-based care. My passion for [specific area of medicine] is complemented by a patient-centric approach, fostering trust and open communication. With a strong belief in continuous learning, I stay abreast of the latest medical advancements to ensure the highest standard of care. I am honored to contribute to the field of medicine, promoting health and enhancing lives."
            ),
        ),
    ]
