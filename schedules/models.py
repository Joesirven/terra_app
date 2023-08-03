from django.db import models

# Create your models here.


# Period Model:
# 		- period_num: PositiveIntegerFreld (max_length=2,)
# 		- is_free_period: BooleanField (default=False,)
# 		- duration: DurationField

class Period(models.Model):
    period_num = models.PositiveSmallIntegerField(max_length=2,)
    free_period = models.BooleanField(default=False,)
    duration = models.DurationField()



# Schedule Model:
# 		- order of periods per week

class Schedule(models.Model):




# 	- Elective Choice Model
# 		- ForeignKey: Student (related_name='elective_choices')
# 		- ForeignKey: Course (related_name='elective_choices')
# 	- ScheduleConstraint Model:
# 		- Session: ForeignKey to the `Section` model to represent the session to which the constraint applies. (related_name='constraints')
# 		- max_courses_per_semester: PositiveIntegerField to specify the maximum number of courses per semester for the given session.
# 		- recommended_progression: ManyToManyField to the `Section` model to represent the recommended progression of curriculum (related_name='recommended_progressions')
# 	- Schedule Optimization:
# 		- Student: ForeignKey (related_name='schedule_optimizations')
# 		- Fitness_function: CharField to store the name or identifier of the fitness function used for optimization.
# 		- weights: JSONField to store a dictionary of weights for each factor in the fitness function.
# 	- Enrollment Model:
# 		- Student: ForeginKey (related_name='schedules')
# 		- Section: ForeignKey (related_name='schedules')
# 		- Final_grade: IntegerField()
# 		- Attendance: 