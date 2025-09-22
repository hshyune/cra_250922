from src.player import Player, PlayerFactory, GoldPlayer, SilverPlayer, NormalPlayer
from src.player_manager import PlayerManager

players = {}


def insert_player_data(name, attendance_weekday):
    # if player not be inserted on memory, insert into memory
    player = Player(name)
    if name not in players:
        player_number = PlayerManager().get_number()
        player.number = player_number
        players[name] = player

    players[name].attend(attendance_weekday)


def input_file():
    try:
        with open("attendance_weekday_500.txt", encoding="utf-8") as f:
            for _ in range(500):
                line = f.readline()
                if not line:
                    break
                parts = line.strip().split()
                if len(parts) == 2:
                    insert_player_data(parts[0], parts[1])

        for name, player in players.items():
            # scoring
            player.score = PlayerManager().scoring(player.attended)
            # grading
            player_factory = PlayerFactory()
            graded_player = player_factory.classifyPlayer(player)
            players[name] = graded_player
            print(
                f"NAME : {name}, POINT : {player.score}, GRADE : {player.grade}"
            )

        print("\nRemoved player")
        print("==============")
        for name, player in players.items():
            # is_falling
            if PlayerManager().is_falling(player.grade, player.attended):
                print(name)

    except FileNotFoundError:
        print("파일을 찾을 수 없습니다.")


if __name__ == "__main__":
    input_file()
