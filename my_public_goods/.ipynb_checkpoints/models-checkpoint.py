from otree.api import (
    models,
    widgets,
    BaseConstants,
    BaseSubsession,
    BaseGroup,
    BasePlayer,
    Currency as c,
    currency_range,
)


author = 'Your name here'

doc = """
Your app description
"""


class Constants(BaseConstants):
    name_in_url = 'my_public_goods'
    players_per_group = 3
    num_rounds = 2
    endowment = c(1000)
    multiplier = 2


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    total_contribution = models.CurrencyField()
    individual_share = models.CurrencyField()
    
    def set_payoffs(self):
        players = self.get_players()
        contributions = [p.contribution for p in players]
        self.total_contribution = sum(contributions)
        self.individual_share = self.total_contribution * Constants.multiplier / Constants.players_per_group
        for player in players:
            player.payoff = Constants.endowment - player.contribution + self.individual_share
        


class Player(BasePlayer):
    contribution = models.CurrencyField(
        min=0,
        max=Constants.endowment,
        label="How much will you contribute?"
    )
    
