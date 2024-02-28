from behave import given, when, then
from logic import init_game 

@given("есть запущенное приложение")
def step_given_app_is_running(context):
    pass

@when("игрок выбирает \"Новая игра\"")
def step_when_player_starts_new_game(context):
    context.player, context.croupier, context.cards, context.player_tot, context.croupier_tot = init_game()  # Имплементируйте эту функцию

@then("на столе должны быть 2 карты у игрока")
def step_then_two_cards_on_player_table(context):
    player_hand = context.player  # Получите текущую руку игрока (например, из глобальной переменной)
    assert len(player_hand) == 2

@then("на столе должна быть 2 карты у крупье")
def step_then_two_cards_on_dealer_table(context):
    dealer_hand = context.croupier  # Получите текущую руку крупье (например, из глобальной переменной)
    assert len(dealer_hand) == 2

@then("сумма очков у игрока должна быть меньше или равна 21")
def step_then_player_score_should_be_equal_or_less_than_21(context):
    player_score = context.player_tot  # Получите текущий счёт игрока (например, из глобальной переменной)
    assert player_score <= 21

@then("сумма очков крупье также меньше или равна 21")
def step_then_croupier_score_is_also_equal_or_less_then_21(context):
    croupier_score = context.croupier_tot
    assert croupier_score <= 21