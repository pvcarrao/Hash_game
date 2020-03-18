import os
import random


class Velha:
    def __init__(self):
        self.positions = ["-", "-", "-", "-", "-", "-", "-", "-", "-"]
        self.avaible_pos = [0, 1, 2, 3, 4, 5, 6, 7, 8]
        self.winning_pos = [[0, 1, 2], [3, 4, 5], [6, 7, 8], [0, 3, 6], [1, 4, 7], [2, 5, 8], [2, 4, 6], [0, 4, 8]]
        self.corner = [0, 2, 6, 8]

    def create_tab(self):
        for i in range(0, 9):
            xerem = (i + 1)/3
            if xerem.is_integer():
                print(self.positions[i])
            else:
                print(self.positions[i], "|", end=" ")

    def play_human(self):
        play = input("Jogue:")
        pos = int(play)
        if pos in self.avaible_pos:
            self.positions[pos] = "X"
            self.avaible_pos.remove(pos)
        else:
            print ("Posição indisponível")
            self.play_human()

    def play_ai(self):
        winning_play_ai = self.check_winning_play("O")
        winning_play_human = self.check_winning_play("X")
        avaible_corner_plays = []
        for i in self.corner:
            if i in self.avaible_pos:
                avaible_corner_plays.append(i)     
        if winning_play_ai:
            pos = winning_play_ai
        elif winning_play_human:
            pos = winning_play_human
        elif 4 in self.avaible_pos:
            pos = 4
        elif avaible_corner_plays:
            pos = random.choice(avaible_corner_plays)
        else:
            pos = random.choice(self.avaible_pos)
        self.positions[pos] = "O"
        self.avaible_pos.remove(pos)

    def has_won(self, player):
        for pos in self.winning_pos:
            if self.positions[pos[0]] == player and self.positions[pos[1]] == player and self.positions[pos[2]] == player:
                return True
        return False

    def check_winning_play(self, player):
        for pos in self.winning_pos:
            if self.positions[pos[0]] == player and self.positions[pos[1]] == player:
                if pos[2] in self.avaible_pos:
                    return pos[2]
            if self.positions[pos[0]] == player and self.positions[pos[2]] == player:
                if pos[1] in self.avaible_pos:
                    return pos[1]
            if self.positions[pos[1]] == player and self.positions[pos[2]] == player:
                if pos[0] in self.avaible_pos:
                    return pos[0]
        return False

    def start_game(self, player):
        for i in range(0,9):
            os.system("clear") or None
            self.create_tab()
            if player == "X":
                self.play_human()
                if self.has_won(player):
                    os.system("clear") or None
                    print("Ganhou! :)")
                    self.create_tab()
                    break
                player = "O"
            else:
                self.play_ai()
                if self.has_won(player):
                    os.system("clear") or None
                    print("Perdeu. :(")
                    self.create_tab()
                    break
                player = "X"

        if not self.has_won("X") and not self.has_won("O"):
            os.system("clear") or None
            self.create_tab()
            print("Velha.")


Velha().start_game("X")