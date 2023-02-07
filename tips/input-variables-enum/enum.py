import enum
import random


# class TrafficLightState(enum.Enum):
#     RED = enum.auto()
#     YELLOW = enum.auto()
#     GREEN = enum.auto()
#     OFF = enum.auto()
#
#
# choice = int(input("Enter numbers [1-4]"))
# state = 0
# print(choice)
# if choice == TrafficLightState.RED:
#     state = TrafficLightState.RED
# elif choice == 2:
#     state = TrafficLightState.YELLOW
# elif choice == 3:
#     state = TrafficLightState.GREEN
# elif choice == 4:
#     state = TrafficLightState.OFF
# else:
#     print("You did not select the state so, it will remain ")
#
# # print the state
# print(state)


class SeasonClass(enum.Enum):
    SPRING = enum.auto()
    SUMMER = enum.auto()
    FALL = enum.auto()
    WINTER = enum.auto()


def get_randon_season():
    """
    Retorna randomicamente as estacoes do ano
    """
    return random.choice(list(SeasonClass))


print(get_randon_season())