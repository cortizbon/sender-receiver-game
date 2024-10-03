from otree.api import *

class Constants(BaseConstants):
    name_in_url = 'survey'
    players_per_group = None
    num_rounds = 1


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):

    # Demographics
    age = models.IntegerField(label='Age', min=13, max=125)

    gender = models.IntegerField(
        label='Gender',
        choices=[[0, 'Male'], [1, 'Female'], [2, 'Rather not say'], [3, 'Other']]
    )
    gender_add = models.StringField(blank=True, label='')
    education = models.IntegerField(
        choices=[[0, 'Less than High School'],
                 [1, 'High School'],
                 [2, 'Some College'],
                 [3, 'Associate Degree'],
                 [4, 'Bachelor\'s Degree'],
                 [5, 'Advanced or Professional Degree']
                 ],
        label='What is your highest level of education?'
    )
    student = models.IntegerField(
        label='Are you currently enrolled in college?',
        choices=[[0, 'No'], [1, 'Yes']]
    )
    experiments = models.IntegerField(
        label='Please give a rough estimate about the number of experiments you have participated in before',
        blank=True
    )

    reasoning = models.LongStringField(
        label='Please give a concise explanation of how you took your decisions in the experiment',
        blank=True
    )

    chosen_role = models.IntegerField(
        choices=[[1, 'Participant A'],
                 [2, 'Participant B'],
                 [0, 'Indifferent'],
                 ],
        label='Imagine you were to play the same game again and had a choice, would you rather be Participant A  or Participant B'
    )

    religion = models.IntegerField(
        choices=[[1, 'Baha\'i'],
                 [2, 'Buddhism'],
                 [3, 'Candomble'],
                 [4, 'Christianity (e.g. Baptist, Church of England, Roman Catholic, Methodist, Jehovah Witness, etc.)'],
                 [5, 'Hinduism'],
                 [6, 'Islam'],
                 [7, 'Jainism'],
                 [8, 'Judaism'],
                 [9, 'Non Religious (e.g. Agnostic, Atheist, No Religion)'],
                 [10, 'Paganism'],
                 [11, 'Rastafari'],
                 [12, 'Santeria'],
                 [13, 'Shinto'],
                 [14, 'Sikhism'],
                 [15, 'Spiritualism'],
                 [16, 'Taoism'],
                 [17, 'Unitarianism'],
                 [18, 'Zorastrianism'],
                 [19, 'Other'],
                 [0, 'Do Not Wish to Answer'],
                 ],
        label='What is your religious affiliation?'
    )

class Demographics(Page):
    form_model = 'player'
    form_fields = ['age', 'gender',  'education', 'student', 'experiments', 'reasoning', 'chosen_role', 'religion']


page_sequence = [Demographics]