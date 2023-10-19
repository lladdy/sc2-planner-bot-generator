import os
import sys

sys.path.insert(1, "sharpy-sc2")
sys.path.insert(1, os.path.join("sharpy-sc2", "python-sc2"))

from bot import SC2PlannerBot
from json_build import calculate_race_and_build_str


from sc2 import maps
from sc2.data import Race, Difficulty
from sc2.main import run_game
from ladder import run_ladder_game
from sc2.player import Bot, Computer


def get_build_order_filename():
    return sys.argv[1]


build_order_filename = get_build_order_filename()

race, build_str = calculate_race_and_build_str(build_order_filename)

bot = Bot(race, SC2PlannerBot('[' + build_str + ']'))


def main():
    if "--LadderServer" in sys.argv:
        # Ladder game started by LadderManager
        print("Starting ladder game...")
        run_ladder_game(bot)
    else:
        # Local game
        print("Starting local game...")

        run_game(maps.get("RoyalBloodAIE"), [
            bot,
            Computer(Race.Random, Difficulty.VeryHard),
        ], save_replay_as=f'replays/replay.SC2Replay', realtime=False)



if __name__ == "__main__":
    main()


