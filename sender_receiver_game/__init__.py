from otree.api import *
import random
import math


class Constants(BaseConstants):
    name_in_url = 'sender_receiver_game'
    players_per_group = 2
    num_rounds = 3
    BONUS_AMOUNT = Currency(5000)
    SENDER_ROLE = 'Sender'
    RECEIVER_ROLE = 'Receiver'


class Subsession(BaseSubsession):
    pass



class Group(BaseGroup):
    secret_number = models.IntegerField(min=0, max=6)
    sender_message = models.IntegerField(min=0, max=6, label="Choose a number to send as your message:")
    receiver_guess = models.FloatField(min=0, max=6, label="Enter your guess for the secret number (between 1 and 5):")


class Player(BasePlayer):


    pass



def set_payoffs(group: Group):
        group.secret_number = random.randint(0, 6)

        sender = group.get_player_by_id(1)
        receiver = group.get_player_by_id(2)

        # Calculate probabilities
        sender_prob = 1 - (1 - group.sender_message) ** 2 # revisar
        receiver_prob = 1 - (group.secret_number - group.receiver_guess) ** 2 # revisar

        # Determine if players win the bonus
        sender_wins = sender_prob > 0.5
        receiver_wins = receiver_prob < 0.5

        # 24 rondas, 12 pago (relevantes), 12 no pago (no relevantes)

        # Set payoffs
        sender.payoff = Constants.BONUS_AMOUNT if sender_wins else Currency(0)
        receiver.payoff = Constants.BONUS_AMOUNT if receiver_wins else Currency(0)

        # revisar los pagos



# pages.py


class Introduction(Page):
    # solo debe aparecer en la primera ronda (número de la ronda únicamente)

    

    @staticmethod
    def vars_for_template(player: Player):
        return {"round_number": player.round_number}
    pass
    
class SenderMessage(Page):
    form_model = 'group'
    form_fields = ['sender_message']

    @staticmethod
    def is_displayed(player):
        return player.id_in_group == 1
    
    timeout_seconds = 20

class WaitForSender(WaitPage):
    pass

class ReceiverGuess(Page):
    form_model = 'group'
    form_fields = ['receiver_guess']

    @staticmethod
    def is_displayed(player):
        return player.id_in_group == 2
    
    timeout_seconds = 20
        

class ResultsWaitPage(WaitPage):
    after_all_players_arrive = set_payoffs


class Results(Page):
    @staticmethod
    def vars_for_template(self):
        return {
            'secret_number': self.group.secret_number,
            'sender_message': self.group.sender_message,
            'receiver_guess': self.group.receiver_guess,
            'sender_payoff': self.group.get_player_by_role('Sender').payoff,
            'receiver_payoff': self.group.get_player_by_role('Receiver').payoff,
        }
    timeout_seconds = 5

page_sequence = [Introduction, SenderMessage, WaitForSender, ReceiverGuess, ResultsWaitPage, Results]
