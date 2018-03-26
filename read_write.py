# Purpose:
#   - easy acces to scores and unlocked characters

import shelve


# given content and type (0 for highscore), writes the content with shelve
def write(content, type):
    with shelve.open("score.txt") as file:
        # check if the highscore should be written
        if type is 0:
            if file["Score"] < content:
                file["Score"] = content
        else:
            file[type] = content


def write_highscore(score):
    write(score, 0)


def get_highscore():
    with shelve.open("score.txt") as file:
        score = file["Score"]
    return score


def reset_highscore():
    with shelve.open("score.txt") as file:
        file["Score"] = 0
