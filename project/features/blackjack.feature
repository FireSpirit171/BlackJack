Feature: Новая игра в блэкджек

  Scenario: Запуск новой игры
    Given есть запущенное приложение
    When игрок выбирает "Новая игра"
    Then на столе должны быть 2 карты у игрока
    And на столе должна быть 2 карты у крупье
    And сумма очков у игрока должна быть меньше или равна 21
    And сумма очков крупье также меньше или равна 21