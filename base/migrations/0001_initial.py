# Generated by Django 3.1.1 on 2020-11-07 02:01

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('neighborhood', models.CharField(max_length=200)),
                ('number', models.CharField(blank=True, max_length=20, null=True)),
                ('complement', models.CharField(blank=True, max_length=200, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Answear',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField(max_length=5000)),
                ('is_public', models.BooleanField(blank=True, default=True)),
            ],
        ),
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_created', models.DateTimeField(auto_now_add=True, null=True)),
                ('title', models.CharField(blank=True, max_length=200, null=True)),
                ('is_public', models.BooleanField(blank=True, default=True)),
                ('note', models.CharField(blank=True, max_length=400, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='CommentaryAnswear',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_created', models.DateTimeField(auto_now_add=True, null=True)),
                ('text', models.CharField(max_length=2000)),
                ('is_public', models.BooleanField(blank=True, default=True)),
                ('answear', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='base.answear')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='CommentaryBook',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_created', models.DateTimeField(auto_now_add=True, null=True)),
                ('text', models.CharField(max_length=2000)),
                ('is_public', models.BooleanField(blank=True, default=True)),
                ('book', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='base.book')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='CommentaryQuestion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_created', models.DateTimeField(auto_now_add=True, null=True)),
                ('text', models.CharField(max_length=2000)),
                ('is_public', models.BooleanField(blank=True, default=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='CommentaryUniversity',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_created', models.DateTimeField(auto_now_add=True, null=True)),
                ('text', models.CharField(max_length=2000)),
                ('is_public', models.BooleanField(blank=True, default=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Exam',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_created', models.DateTimeField(auto_now_add=True, null=True)),
                ('title', models.CharField(blank=True, max_length=200, null=True)),
                ('education_Level', models.CharField(choices=[('M', 'Master'), ('H', 'High School'), ('P', 'Phd'), ('D', 'Degree'), ('T', 'Tecnical'), ('F', 'Fundamental')], max_length=1)),
                ('university_name', models.CharField(blank=True, max_length=200, null=True)),
                ('wrong_answears_count', models.IntegerField(blank=True, default=0)),
                ('is_public', models.BooleanField(blank=True, default=True)),
                ('pic_1', models.ImageField(blank=True, null=True, upload_to='')),
                ('pic_2', models.ImageField(blank=True, null=True, upload_to='')),
                ('pic_3', models.ImageField(blank=True, null=True, upload_to='')),
                ('pic_4', models.ImageField(blank=True, null=True, upload_to='')),
                ('pic_5', models.ImageField(blank=True, null=True, upload_to='')),
            ],
        ),
        migrations.CreateModel(
            name='Notification',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_created', models.DateTimeField(auto_now_add=True, null=True)),
                ('not_pic', models.ImageField(blank=True, default='notification.png', upload_to='')),
                ('message', models.CharField(blank=True, max_length=1000, null=True)),
                ('answear', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='base.answear')),
                ('book', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='base.book')),
                ('commentary_answear', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='base.commentaryanswear')),
                ('commentary_book', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='base.commentarybook')),
                ('commentary_question', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='base.commentaryquestion')),
                ('commentary_university', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='base.commentaryuniversity')),
            ],
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_created', models.DateTimeField(auto_now_add=True, null=True)),
                ('text', models.CharField(max_length=10000)),
                ('teacher_name', models.CharField(max_length=200)),
                ('education_Level', models.CharField(choices=[('M', 'Master'), ('H', 'High School'), ('P', 'Phd'), ('D', 'Degree'), ('T', 'Tecnical'), ('F', 'Fundamental')], max_length=1)),
                ('year', models.CharField(choices=[('21', '2021'), ('20', '2020'), ('19', '2019'), ('18', '2018'), ('17', '2017'), ('16', '2016'), ('15', '2015'), ('14', '2014'), ('13', '2013'), ('12', '2012'), ('11', '2011'), ('10', '2010'), ('9', '2009'), ('8', '2008'), ('7', '2007'), ('6', '2006'), ('5', '2005'), ('4', '2004'), ('3', '2003'), ('2', '2002'), ('1', '2001'), ('0', '2000')], max_length=2)),
                ('answear', models.CharField(blank=True, max_length=5000, null=True)),
                ('is_public', models.BooleanField(blank=True, default=True)),
                ('wrong_answears_count', models.IntegerField(blank=True, default=0)),
                ('difficult', models.CharField(blank=True, choices=[('E', 'Very Easy'), ('e', 'Easy'), ('m', 'Middle Level'), ('h', 'Hard'), ('H', 'Very Hard')], default='E', max_length=1)),
                ('pic_1', models.ImageField(blank=True, null=True, upload_to='')),
                ('pic_2', models.ImageField(blank=True, null=True, upload_to='')),
                ('answears', models.ManyToManyField(blank=True, to='base.Answear')),
                ('books', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='base.book')),
                ('exams', models.ManyToManyField(blank=True, to='base.Exam')),
            ],
        ),
        migrations.CreateModel(
            name='Report',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_created', models.DateTimeField(auto_now_add=True, null=True)),
                ('note', models.CharField(max_length=2000)),
            ],
        ),
        migrations.CreateModel(
            name='StandardUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_created', models.DateTimeField(auto_now_add=True, null=True)),
                ('profile_pic', models.ImageField(blank=True, default='profile1.png', null=True, upload_to='')),
                ('nickname', models.CharField(blank=True, max_length=200, null=True)),
                ('firstname', models.CharField(blank=True, max_length=100, null=True)),
                ('lastname', models.CharField(blank=True, max_length=200, null=True)),
                ('birth', models.CharField(blank=True, max_length=8, null=True)),
                ('phone', models.CharField(blank=True, max_length=11, null=True)),
                ('sex', models.CharField(blank=True, max_length=1, null=True)),
                ('education', models.CharField(blank=True, max_length=100, null=True)),
                ('color', models.CharField(blank=True, choices=[('W', 'White'), ('B', 'Black'), ('G', 'Grey')], default='W', max_length=1)),
                ('addresses', models.ManyToManyField(blank=True, to='base.Address')),
                ('notifications', models.ManyToManyField(blank=True, to='base.Notification')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='State',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('initials', models.CharField(max_length=2)),
            ],
        ),
        migrations.CreateModel(
            name='TeacherStudents',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_created', models.DateTimeField(auto_now_add=True, null=True)),
                ('title', models.CharField(blank=True, max_length=200, null=True)),
                ('note', models.CharField(max_length=2000)),
            ],
        ),
        migrations.CreateModel(
            name='University',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('profile_pic', models.ImageField(blank=True, default='profile1.png', null=True, upload_to='')),
                ('date_created', models.DateTimeField(auto_now_add=True, null=True)),
                ('name', models.CharField(max_length=200)),
                ('initials', models.CharField(max_length=10)),
                ('addresses', models.ManyToManyField(blank=True, to='base.Address')),
                ('reports', models.ManyToManyField(blank=True, to='base.Report')),
            ],
        ),
        migrations.CreateModel(
            name='UserPermissionUniversity',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('permission', models.CharField(choices=[('S', 'Student'), ('T', 'Teacher'), ('P', 'Poster'), ('O', 'Owner')], max_length=1)),
                ('standarduser', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='base.standarduser')),
                ('university', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='base.university')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='UserPermissionTeacher',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('permission', models.CharField(choices=[('S', 'Student'), ('T', 'Teacher'), ('P', 'Poster'), ('O', 'Owner')], max_length=1)),
                ('standarduser', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='base.standarduser')),
                ('teacher_students', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='base.teacherstudents')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='UserPermissionStudents',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('permission', models.CharField(choices=[('S', 'Student'), ('T', 'Teacher'), ('P', 'Poster'), ('O', 'Owner')], max_length=1)),
                ('standarduser', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='base.standarduser')),
                ('teacher_students', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='base.teacherstudents')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='UserPermissionQuestion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('permission', models.CharField(choices=[('S', 'Student'), ('T', 'Teacher'), ('P', 'Poster'), ('O', 'Owner')], max_length=1)),
                ('question', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='base.question')),
                ('standarduser', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='base.standarduser')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='UserPermissionExam',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('permission', models.CharField(choices=[('S', 'Student'), ('T', 'Teacher'), ('P', 'Poster'), ('O', 'Owner')], max_length=1)),
                ('exam', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='base.exam')),
                ('standarduser', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='base.standarduser')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='UserPermissionBook',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('permission', models.CharField(choices=[('S', 'Student'), ('T', 'Teacher'), ('P', 'Poster'), ('O', 'Owner')], max_length=1)),
                ('book', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='base.book')),
                ('standarduser', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='base.standarduser')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='UserPermissionAnswear',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('permission', models.CharField(choices=[('S', 'Student'), ('T', 'Teacher'), ('P', 'Poster'), ('O', 'Owner')], max_length=1)),
                ('answear', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='base.answear')),
                ('standarduser', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='base.standarduser')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='TimeToApplyExam',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_created', models.DateTimeField(auto_now_add=True, null=True)),
                ('date_to_apply', models.DateTimeField(blank=True, null=True)),
                ('date_to_finish', models.DateTimeField(blank=True, null=True)),
                ('exam', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='base.exam')),
                ('standarduser', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='base.standarduser')),
            ],
        ),
        migrations.CreateModel(
            name='Subject',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('discipline_name', models.CharField(max_length=100)),
                ('reports', models.ManyToManyField(blank=True, to='base.Report')),
            ],
        ),
        migrations.CreateModel(
            name='Requisition',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_created', models.DateTimeField(auto_now_add=True, null=True)),
                ('about', models.CharField(blank=True, max_length=200, null=True)),
                ('standarduser', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='base.standarduser')),
            ],
        ),
        migrations.AddField(
            model_name='report',
            name='standarduser',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='base.standarduser'),
        ),
        migrations.AddField(
            model_name='question',
            name='reports',
            field=models.ManyToManyField(blank=True, to='base.Report'),
        ),
        migrations.AddField(
            model_name='question',
            name='standarduser',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='base.standarduser'),
        ),
        migrations.AddField(
            model_name='question',
            name='subject',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='base.subject'),
        ),
        migrations.AddField(
            model_name='question',
            name='university',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='base.university'),
        ),
        migrations.AddField(
            model_name='notification',
            name='question',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='base.question'),
        ),
        migrations.AddField(
            model_name='notification',
            name='reports',
            field=models.ManyToManyField(blank=True, to='base.Report'),
        ),
        migrations.AddField(
            model_name='notification',
            name='university',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='base.university'),
        ),
        migrations.CreateModel(
            name='LikeUniversity',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_created', models.DateTimeField(auto_now_add=True, null=True)),
                ('standarduser', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='base.standarduser')),
                ('university', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='base.university')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='LikeNotification',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_created', models.DateTimeField(auto_now_add=True, null=True)),
                ('notification', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='base.notification')),
                ('standarduser', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='base.standarduser')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='LikeCommentaryUniversity',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_created', models.DateTimeField(auto_now_add=True, null=True)),
                ('commentary', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='base.commentaryuniversity')),
                ('standarduser', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='base.standarduser')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='LikeCommentaryQuestion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_created', models.DateTimeField(auto_now_add=True, null=True)),
                ('commentary', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='base.commentaryquestion')),
                ('standarduser', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='base.standarduser')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='LikeCommentaryBook',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_created', models.DateTimeField(auto_now_add=True, null=True)),
                ('commentary', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='base.commentarybook')),
                ('standarduser', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='base.standarduser')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='LikeCommentaryAnswear',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_created', models.DateTimeField(auto_now_add=True, null=True)),
                ('commentary', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='base.commentaryanswear')),
                ('standarduser', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='base.standarduser')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='LikeBook',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_created', models.DateTimeField(auto_now_add=True, null=True)),
                ('book', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='base.book')),
                ('standarduser', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='base.standarduser')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='LikeAnswear',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_created', models.DateTimeField(auto_now_add=True, null=True)),
                ('answear', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='base.answear')),
                ('standarduser', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='base.standarduser')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='exam',
            name='reports',
            field=models.ManyToManyField(blank=True, to='base.Report'),
        ),
        migrations.AddField(
            model_name='exam',
            name='standarduser',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='base.standarduser'),
        ),
        migrations.AddField(
            model_name='exam',
            name='subjects',
            field=models.ManyToManyField(blank=True, to='base.Subject'),
        ),
        migrations.CreateModel(
            name='Discipline',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('subjects', models.ManyToManyField(blank=True, to='base.Subject')),
            ],
        ),
        migrations.CreateModel(
            name='DeslikeUniversity',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_created', models.DateTimeField(auto_now_add=True, null=True)),
                ('standarduser', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='base.standarduser')),
                ('university', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='base.university')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='DeslikeNotification',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_created', models.DateTimeField(auto_now_add=True, null=True)),
                ('notification', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='base.notification')),
                ('standarduser', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='base.standarduser')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='DeslikeCommentaryUniversity',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_created', models.DateTimeField(auto_now_add=True, null=True)),
                ('commentary', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='base.commentaryuniversity')),
                ('standarduser', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='base.standarduser')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='DeslikeCommentaryQuestion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_created', models.DateTimeField(auto_now_add=True, null=True)),
                ('commentary', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='base.commentaryquestion')),
                ('standarduser', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='base.standarduser')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='DeslikeCommentaryBook',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_created', models.DateTimeField(auto_now_add=True, null=True)),
                ('commentary', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='base.commentarybook')),
                ('standarduser', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='base.standarduser')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='DeslikeCommentaryAnswear',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_created', models.DateTimeField(auto_now_add=True, null=True)),
                ('commentary', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='base.commentaryanswear')),
                ('standarduser', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='base.standarduser')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='DeslikeBook',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_created', models.DateTimeField(auto_now_add=True, null=True)),
                ('book', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='base.book')),
                ('standarduser', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='base.standarduser')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='DeslikeAnswear',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_created', models.DateTimeField(auto_now_add=True, null=True)),
                ('answear', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='base.answear')),
                ('standarduser', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='base.standarduser')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='commentaryuniversity',
            name='reports',
            field=models.ManyToManyField(blank=True, to='base.Report'),
        ),
        migrations.AddField(
            model_name='commentaryuniversity',
            name='standarduser',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='base.standarduser'),
        ),
        migrations.AddField(
            model_name='commentaryuniversity',
            name='university',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='base.university'),
        ),
        migrations.AddField(
            model_name='commentaryquestion',
            name='question',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='base.question'),
        ),
        migrations.AddField(
            model_name='commentaryquestion',
            name='reports',
            field=models.ManyToManyField(blank=True, to='base.Report'),
        ),
        migrations.AddField(
            model_name='commentaryquestion',
            name='standarduser',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='base.standarduser'),
        ),
        migrations.AddField(
            model_name='commentarybook',
            name='reports',
            field=models.ManyToManyField(blank=True, to='base.Report'),
        ),
        migrations.AddField(
            model_name='commentarybook',
            name='standarduser',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='base.standarduser'),
        ),
        migrations.AddField(
            model_name='commentaryanswear',
            name='reports',
            field=models.ManyToManyField(blank=True, to='base.Report'),
        ),
        migrations.AddField(
            model_name='commentaryanswear',
            name='standarduser',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='base.standarduser'),
        ),
        migrations.CreateModel(
            name='City',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('state', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='base.state')),
            ],
        ),
        migrations.AddField(
            model_name='book',
            name='reports',
            field=models.ManyToManyField(blank=True, to='base.Report'),
        ),
        migrations.AddField(
            model_name='book',
            name='standarduser',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='base.standarduser'),
        ),
        migrations.AddField(
            model_name='book',
            name='subject',
            field=models.ManyToManyField(blank=True, to='base.Subject'),
        ),
        migrations.AddField(
            model_name='answear',
            name='reports',
            field=models.ManyToManyField(blank=True, to='base.Report'),
        ),
        migrations.AddField(
            model_name='answear',
            name='standarduser',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='base.standarduser'),
        ),
        migrations.AddField(
            model_name='address',
            name='city',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='base.city'),
        ),
    ]
