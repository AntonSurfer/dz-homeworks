from django.db import migrations

def migrate_teacher_to_teachers(apps, schema_editor):
    Student = apps.get_model('school', 'Student')
    for student in Student.objects.all():
        if student.teacher_id:
            student.teachers.add(student.teacher)

def reverse_migrate(apps, schema_editor):
    pass

class Migration(migrations.Migration):
    dependencies = [
        ('school', '0003_student_teachers'),
    ]

    operations = [
        migrations.RunPython(migrate_teacher_to_teachers, reverse_migrate),
    ]
