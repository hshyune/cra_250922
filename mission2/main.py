MONDAY = 0
TUESDAY = 1
WEDNESDAY = 2
THURSDAY = 3
FRIDAY = 4
SATURDAY = 5
SUNDAY = 6

PLAYER_NUMBER = 0

GOLD = "Gold"
SILVER = "Silver"
NORMAL = "Normal"

players = {}
# player
"""
{
    "Tina": {
        "number" : 16,
        "attended" : [],
        "score": 24,
        "grade": "Normal"
    },
    "Will": {
        "number" : 17,
        "attended" : [],
        "score": 46,
        "grade": "Silver"
    },
    ...
}
"""

def get_player_number():
    # get player number from 1
    global PLAYER_NUMBER
    PLAYER_NUMBER += 1
    return PLAYER_NUMBER

def get_score(attended_weekday: str):
    # get score by weekday
    ## wednesday 3
    ## weekend: saturday, sunday 2
    ## others 1
    index = 0
    score = 0
    if attended_weekday == "monday":
        index = MONDAY
        score = 1
    elif attended_weekday == "tuesday":
        index = TUESDAY
        score = 1
    elif attended_weekday == "wednesday":
        index = WEDNESDAY
        score = 3
    elif attended_weekday == "thursday":
        index = THURSDAY
        score = 1
    elif attended_weekday == "friday":
        index = FRIDAY
        score = 1
    elif attended_weekday == "saturday":
        index = SATURDAY
        score = 2
    elif attended_weekday == "sunday":
        index = SUNDAY
        score = 2
    else:
        index = -1
        score = 0
    return index, score

def get_grade(player: dict):
    # grading players by score
    ## if player attended weekend and Wednesday more than or equal 10 days, player can receive bonus score. 
    if player["attended"][WEDNESDAY] >= 10:
        player["score"] += 10
    if (player["attended"][SATURDAY] + player["attended"][SUNDAY]) >= 10:
        player["score"] += 10
        
    # define grade
    score = player["score"]
    if score >= 50:
        player["grade"] = GOLD
    elif score >= 30:
        player["grade"] = SILVER
    else:
        player["grade"] = NORMAL
    return player["grade"]

def is_falling(player: dict):
    attended = player["attended"]
    if (player["grade"] == NORMAL) and (
        (attended[WEDNESDAY] + attended[SATURDAY] + attended[SUNDAY]) == 0
    ):
        return True
    return False

def insert_player_data(name, attendance_weekday):
    # if player not be inserted on memory, insert into memory
    if name not in players:
        player_number = get_player_number()
        players[name] = {
            "number": player_number,
            "attended": [0, 0, 0, 0, 0, 0, 0],
            "score": 0,
            "grade": None,
        }
        

    # scoring and grading
    index, score = get_score(attendance_weekday)
    try:
        player = players.get(name)
        player["attended"][index] += score
        player["score"] += score
    except IndexError as ie:
        pass

    return score

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
            get_grade(player)
            print(
                f"NAME : {name}, POINT : {player['score']}, GRADE : {player['grade']}"
            )

        print("\nRemoved player")
        print("==============")
        for name, player in players.items():
            if is_falling(player):
                print(name)

    except FileNotFoundError:
        print("파일을 찾을 수 없습니다.")

if __name__ == "__main__":
    input_file()