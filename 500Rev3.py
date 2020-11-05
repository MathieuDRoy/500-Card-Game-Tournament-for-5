import tkinter as tk
from tkinter import messagebox
from tkinter.ttk import *
import time

class App(tk.Frame):
    def __init__(self, parent):
        tk.Frame.__init__(self, parent)
        self.parent = parent
    #current hand and bidder
        self.weight = 0
        self.suit = 0
        self.bidder = ""
        self.undone = 0 
        self.ftd = 0     
    #Partners
        self.local_team1 = []
        self.total_team1 = []
        self.local_team2 = []
        self.total_team2 = []
        self.name_team1 = []
        self.name_team2 = []
    #local_contestent: game score - equal to partner
        self.local_contestant1 = 0
        self.local_contestant2 = 0
        self.local_contestant3 = 0
        self.local_contestant4 = 0
        self.local_contestant5 = 0
    #total_contestent: tournement score
        self.total_contestant1 = 0
        self.total_contestant2 = 0
        self.total_contestant3 = 0
        self.total_contestant4 = 0
        self.total_contestant5 = 0
    ##        Stats        ##
    #checkbox stats
        self.check_undone = False
        self.check_ftd = False 
    #total_count: hands taken in total
        self.total_count1 = 0
        self.total_count2 = 0
        self.total_count3 = 0
        self.total_count4 = 0
        self.total_count5 = 0
    #*suit*_score: amount of times we took that suit
        self.blood_score = 0
        self.heart_score = 0
        self.diamond_score = 0
        self.club_score = 0
        self.spade_score = 0
    #All possible games 
        self.games_played = [None]*15
        
        self.start_up()
        
    def start_up(self):
        self.parent.geometry("1100x300")
        self.parent.title("500")
        
    #Names of players
        self.label1 = tk.Label(self.parent, text="Player 1")
        self.entry1 = tk.Entry(self.parent)
        self.label2 = tk.Label(self.parent, text="Player 2")
        self.entry2 = tk.Entry(self.parent)
        self.label3 = tk.Label(self.parent, text="Player 3")
        self.entry3 = tk.Entry(self.parent)
        self.label4 = tk.Label(self.parent, text="Player 4")
        self.entry4 = tk.Entry(self.parent)
        self.label5 = tk.Label(self.parent, text="Player 5")
        self.entry5 = tk.Entry(self.parent)

    ##      Buttons           ##
    #misc
        self.button = tk.Button(self.parent, text = "Continue", command = self.SecondPage)
        self.submit = tk.Button(self.parent, text = "Submit", state = "disable", command = self.tabulate)
        self.stats = tk.Button(self.parent, text = "Stats", command = self.stats)
        var1 = tk.IntVar()
        var2 = tk.IntVar()
        self.FTD = tk.Checkbutton(self.parent, variable = var1, text = "Force the Dealer", command = self.set_ftd)
        self.makeIt = tk.Checkbutton(self.parent, variable = var2, text = "Undone", command = self.set_made)


    #All Posible games
        self.game1234 = tk.Button(self.parent, text="Player1 & Player2 VS Player3 & Player4", bg="#16DFD8", state="disabled", command = self.g1234)
        self.game1235 = tk.Button(self.parent, text="Player1 & Player2 VS Player3 & Player5", bg="#16DFD8", state="disabled", command = self.g1235)
        self.game1245 = tk.Button(self.parent, text="Player1 & Player2 VS Player4 & Player5", bg="#16DFD8", state="disabled", command = self.g1245)
        
        self.game1324 = tk.Button(self.parent, text="Player1 & Player3 VS Player2 & Player4", bg="#2C8AC9", state="disabled", command = self.g1324)
        self.game1325 = tk.Button(self.parent, text="Player1 & Player3 VS Player2 & Player5", bg="#2C8AC9", state="disabled", command = self.g1325)
        self.game1345 = tk.Button(self.parent, text="Player1 & Player3 VS Player4 & Player5", bg="#2C8AC9", state="disabled", command = self.g1345)
        
        self.game1423 = tk.Button(self.parent, text="Player1 & Player4 VS Player2 & Player3", bg="#E3721C", state="disabled", command = self.g1423)
        self.game1425 = tk.Button(self.parent, text="Player1 & Player4 VS Player2 & Player5", bg="#E3721C", state="disabled", command = self.g1425)
        self.game1435 = tk.Button(self.parent, text="Player1 & Player4 VS Player3 & Player5", bg="#E3721C", state="disabled", command = self.g1435)
        
        self.game1523 = tk.Button(self.parent, text="Player1 & Player5 VS Player2 & Player3", bg="#F882F8", state="disabled", command = self.g1523)
        self.game1524 = tk.Button(self.parent, text="Player1 & Player5 VS Player2 & Player4", bg="#F882F8", state="disabled", command = self.g1524)
        self.game1534 = tk.Button(self.parent, text="Player1 & Player5 VS Player3 & Player4", bg="#F882F8", state="disabled", command = self.g1534)
        
        self.game2345 = tk.Button(self.parent, text="Player2 & Player3 VS Player4 & Player5", bg="#F50000", state="disabled", command = self.g2345)
        self.game2435 = tk.Button(self.parent, text="Player2 & Player4 VS Player3 & Player5", bg="#F50000", state="disabled", command = self.g2435)
        self.game2534 = tk.Button(self.parent, text="Player2 & Player5 VS Player3 & Player4", bg="#F50000", state="disabled", command = self.g2534)

        self.P1 = tk.Label(self.parent, text = "Player 1 doesn't play")        
        self.P2 = tk.Label(self.parent, text = "Player 2 doesn't play")        
        self.P3 = tk.Label(self.parent, text = "Player 3 doesn't play")
        self.P4 = tk.Label(self.parent, text = "Player 4 doesn't play")
        self.P5 = tk.Label(self.parent, text = "Player 5 doesn't play")        

    ##      Radio Buttons       ##
    #Used for different radiobutton groups
        t = tk.StringVar(self, "3")
        v = tk.StringVar(self, "1")
        u = tk.StringVar(self, "2")
        
    #Weight
        self.ten = tk.Radiobutton(self.parent, text = "10", variable = v, value = 400,  indicator = 0, state = "disabled", command = self.ten)
        self.nine = tk.Radiobutton(self.parent, text = "9", variable = v, value = 300,  indicator = 0, state = "disabled", command = self.nine)        
        self.eight = tk.Radiobutton(self.parent, text = "8", variable = v, value = 200,  indicator = 0, state = "disabled", command = self.eight)        

    #Suit
        self.blood = tk.Radiobutton(self.parent, text = "Sans",    variable = u, value = 120,  indicator = 0, state = "disabled", command = self.blood)
        self.heart = tk.Radiobutton(self.parent, text = u"\u2764", variable = u, value = 100,  indicator = 0, state = "disabled", command = self.heart)
        self.diamond = tk.Radiobutton(self.parent, text = u"\u2666", variable = u, value = 80,   indicator = 0, state = "disabled", command = self.diamond)
        self.club = tk.Radiobutton(self.parent, text = u"\u2663", variable = u, value = 60,   indicator = 0, state = "disabled", command = self.club)
        self.spade = tk.Radiobutton(self.parent, text = u"\u2660", variable = u, value = 40,   indicator = 0, state = "disabled", command = self.spade)

    #Player Placing Bid
        self.bidder1 = tk.Radiobutton(self.parent, text = "Player 1", variable = t, value = 1, indicator = 0, state = "disabled", command = self.first_bid)
        self.bidder2 = tk.Radiobutton(self.parent, text = "Player 2", variable = t, value = 2, indicator = 0, state = "disabled", command = self.second_bid)
        self.bidder3 = tk.Radiobutton(self.parent, text = "Player 3", variable = t, value = 3, indicator = 0, state = "disabled", command = self.third_bid)
        self.bidder4 = tk.Radiobutton(self.parent, text = "Player 4", variable = t, value = 4, indicator = 0, state = "disabled", command = self.fourth_bid)
        self.bidder5 = tk.Radiobutton(self.parent, text = "Player 5", variable = t, value = 5, indicator = 0, state = "disabled", command = self.fifth_bid)

    #score board
        self.score_board_title = tk.Label(self.parent, text = "Game Score")
        self.score_team1_name = tk.Label(self.parent, text = "Team 1")
        self.score_team1_value = tk.Label(self.parent, text = "0")
        self.score_team2_name = tk.Label(self.parent, text = "Team 2")
        self.score_team2_value = tk.Label(self.parent, text = "0")

    ##     Grid Palcement     ##
        self.label1.grid(row = 0, column = 0)
        self.entry1.grid(row = 1, column = 0)
        self.label2.grid(row = 2, column = 0)
        self.entry2.grid(row = 3, column = 0)
        self.label3.grid(row = 4, column = 0)
        self.entry3.grid(row = 5, column = 0)
        self.label4.grid(row = 6, column = 0)
        self.entry4.grid(row = 7, column = 0)
        self.label5.grid(row = 8, column = 0)
        self.entry5.grid(row = 9, column = 0)

        self.button.grid(row = 10, column = 0)
        self.submit.grid(row = 8, column = 5)
        self.stats.grid(row = 10, column = 5)

        self.FTD.grid(row = 6, column = 5)
        self.makeIt.grid(row = 7, column = 5)

        self.game1234.grid(row = 0, column = 2)
        self.game1235.grid(row = 1, column = 2) 
        self.game1245.grid(row = 2, column = 2)

        self.game1324.grid(row = 0, column = 3)
        self.game1325.grid(row = 1, column = 3)
        self.game1345.grid(row = 3, column = 3)
        
        self.game1423.grid(row = 0, column = 4)
        self.game1425.grid(row = 2, column = 4)
        self.game1435.grid(row = 3, column = 4)
        
        self.game1523.grid(row = 1, column = 5)
        self.game1524.grid(row = 2, column = 5)
        self.game1534.grid(row = 3, column = 5)
        
        self.game2345.grid(row = 4, column = 3)
        self.game2435.grid(row = 4, column = 4)
        self.game2534.grid(row = 4, column = 5)

        self.P1.grid(row = 4, column = 6)
        self.P2.grid(row = 3, column = 6)
        self.P3.grid(row = 2, column = 6)
        self.P4.grid(row = 1, column = 6)
        self.P5.grid(row = 0, column = 6)

        self.ten.grid(row = 6, column =2)
        self.nine.grid(row = 7, column =2)
        self.eight.grid(row = 8, column =2)
        
        self.blood.grid(row = 6, column =3)
        self.heart.grid(row = 7, column =3)
        self.diamond.grid(row = 8, column =3)
        self.club.grid(row = 9, column =3)
        self.spade.grid(row = 10, column =3)        

        self.bidder1.grid(row = 6, column = 4)
        self.bidder2.grid(row = 7, column = 4)
        self.bidder3.grid(row = 8, column = 4)
        self.bidder4.grid(row = 9, column = 4)
        self.bidder5.grid(row = 10, column = 4)

        self.score_board_title.grid(row = 6, column = 6)
        self.score_team1_name.grid(row = 7, column = 6)
        self.score_team1_value.grid(row = 8, column = 6)
        self.score_team2_name.grid(row = 9, column = 6)
        self.score_team2_value.grid(row = 10, column = 6)
        

    def SecondPage(self):
        self.button.config(state = "disabled")
        for H in (self.game1234, self.game1235, self.game1245, self.game1324, self.game1325, self.game1345, self.game1423, self.game1425, self.game1435, self.game1523, self.game1524,
                  self.game1534, self.game2345, self.game2435, self.game2534):
            H.config(state = "normal")
        
        for F in (self.entry1, self.entry2, self.entry3, self.entry4, self.entry5):
            F.config(state = "disabled")
            
        player1 = self.entry1.get()
        player2 = self.entry2.get()
        player3 = self.entry3.get()
        player4 = self.entry4.get()
        player5 = self.entry5.get()
        self.game1234.config(text = player1 + " & " + player2 + " VS " + player3 + " & " + player4)
        self.game1235.config(text = player1 + " & " + player2 + " VS " + player3 + " & " + player5)
        self.game1245.config(text = player1 + " & " + player2 + " VS " + player4 + " & " + player5)
        
        self.game1324.config(text = player1 + " & " + player3 + " VS " + player2 + " & " + player4)
        self.game1325.config(text = player1 + " & " + player3 + " VS " + player2 + " & " + player5)
        self.game1345.config(text = player1 + " & " + player3 + " VS " + player4 + " & " + player5)
        
        self.game1423.config(text = player1 + " & " + player4 + " VS " + player2 + " & " + player3)
        self.game1425.config(text = player1 + " & " + player4 + " VS " + player2 + " & " + player5)
        self.game1435.config(text = player1 + " & " + player4 + " VS " + player3 + " & " + player5)
        
        self.game1523.config(text = player1 + " & " + player5 + " VS " + player2 + " & " + player3)
        self.game1524.config(text = player1 + " & " + player5 + " VS " + player2 + " & " + player4)
        self.game1534.config(text = player1 + " & " + player5 + " VS " + player3 + " & " + player4)
        
        self.game2345.config(text = player2 + " & " + player3 + " VS " + player4 + " & " + player5)
        self.game2435.config(text = player2 + " & " + player4 + " VS " + player3 + " & " + player5)
        self.game2534.config(text = player2 + " & " + player5 + " VS " + player3 + " & " + player4)

        self.bidder1.config(text = player1)
        self.bidder2.config(text = player2)
        self.bidder3.config(text = player3)
        self.bidder4.config(text = player4)
        self.bidder5.config(text = player5)

        self.P1.config(text = player1 + " doesn't play")
        self.P2.config(text = player2 + " doesn't play")
        self.P3.config(text = player3 + " doesn't play")
        self.P4.config(text = player4 + " doesn't play")
        self.P5.config(text = player5 + " doesn't play")

    def g1234(self):
        self.local_team1 = [self.local_contestant1, self.local_contestant2]
        self.local_team2 = [self.local_contestant3, self.local_contestant4]
        self.total_team1 = [self.total_contestant1, self.total_contestant2]
        self.total_team2 = [self.total_contestant3, self.total_contestant4]
        self.name_team1 = [self.entry1.get(), self.entry2.get()]
        self.name_team2 = [self.entry3.get(), self.entry4.get()]
        self.score_team1_name.config(text = self.name_team1[0] + " & " + self.name_team1[1])
        self.score_team2_name.config(text = self.name_team2[0] + " & " + self.name_team2[1])
        self.games_played[0] = self.game1234
        self.five_not_playing()#1

    def g1235(self):
        self.local_team1 = [self.local_contestant1, self.local_contestant2]
        self.local_team2 = [self.local_contestant3, self.local_contestant5]
        self.total_team1 = [self.total_contestant1, self.total_contestant2]
        self.total_team2 = [self.total_contestant3, self.total_contestant5]
        self.name_team1 = [self.entry1.get(), self.entry2.get()]
        self.name_team2 = [self.entry3.get(), self.entry5.get()]
        self.score_team1_name.config(text = self.name_team1[0] + " & " + self.name_team1[1])
        self.score_team2_name.config(text = self.name_team2[0] + " & " + self.name_team2[1])
        self.games_played[1] = self.game1235
        self.four_not_playing()#2

    def g1245(self):
        self.local_team1 = [self.local_contestant1, self.local_contestant2]
        self.local_team2 = [self.local_contestant4, self.local_contestant5]
        self.total_team1 = [self.total_contestant1, self.total_contestant2]
        self.total_team2 = [self.total_contestant4, self.total_contestant5]
        self.name_team1 = [self.entry1.get(), self.entry2.get()]
        self.name_team2 = [self.entry4.get(), self.entry5.get()]
        self.score_team1_name.config(text = self.name_team1[0] + " & " + self.name_team1[1])
        self.score_team2_name.config(text = self.name_team2[0] + " & " + self.name_team2[1])
        self.games_played[2] = self.game1245
        self.three_not_playing()#3

    def g1324(self):
        self.local_team1 = [self.local_contestant1, self.local_contestant3]
        self.local_team2 = [self.local_contestant2, self.local_contestant4]
        self.total_team1 = [self.total_contestant1, self.total_contestant3]
        self.total_team2 = [self.total_contestant2, self.total_contestant4]
        self.name_team1 = [self.entry1.get(), self.entry3.get()]
        self.name_team2 = [self.entry2.get(), self.entry4.get()]
        self.score_team1_name.config(text = self.name_team1[0] + " & " + self.name_team1[1])
        self.score_team2_name.config(text = self.name_team2[0] + " & " + self.name_team2[1])
        self.games_played[3] = self.game1324
        self.five_not_playing()#4

    def g1325(self):
        self.local_team1 = [self.local_contestant1, self.local_contestant3]
        self.local_team2 = [self.local_contestant2, self.local_contestant5]
        self.total_team1 = [self.total_contestant1, self.total_contestant3]
        self.total_team2 = [self.total_contestant2, self.total_contestant5]
        self.name_team1 = [self.entry1.get(), self.entry3.get()]
        self.name_team2 = [self.entry2.get(), self.entry5.get()]
        self.score_team1_name.config(text = self.name_team1[0] + " & " + self.name_team1[1])
        self.score_team2_name.config(text = self.name_team2[0] + " & " + self.name_team2[1])
        self.games_played[4] = self.game1325
        self.four_not_playing()#5

    def g1345(self):
        self.local_team1 = [self.local_contestant1, self.local_contestant3]
        self.local_team2 = [self.local_contestant4, self.local_contestant5]
        self.total_team1 = [self.total_contestant1, self.total_contestant3]
        self.total_team2 = [self.total_contestant4, self.total_contestant5]
        self.name_team1 = [self.entry1.get(), self.entry3.get()]
        self.name_team2 = [self.entry4.get(), self.entry5.get()]
        self.score_team1_name.config(text = self.name_team1[0] + " & " + self.name_team1[1])
        self.score_team2_name.config(text = self.name_team2[0] + " & " + self.name_team2[1])
        self.games_played[5] = self.game1345
        self.two_not_playing()#6

    def g1423(self):
        self.local_team1 = [self.local_contestant1, self.local_contestant4]
        self.local_team2 = [self.local_contestant2, self.local_contestant3]
        self.total_team1 = [self.total_contestant1, self.total_contestant4]
        self.total_team2 = [self.total_contestant2, self.total_contestant3]
        self.name_team1 = [self.entry1.get(), self.entry4.get()]
        self.name_team2 = [self.entry2.get(), self.entry3.get()]
        self.score_team1_name.config(text = self.name_team1[0] + " & " + self.name_team1[1])
        self.score_team2_name.config(text = self.name_team2[0] + " & " + self.name_team2[1])
        self.games_played[6] = self.game1423
        self.five_not_playing()#7

    def g1425(self):
        self.local_team1 = [self.local_contestant1, self.local_contestant4]
        self.local_team2 = [self.local_contestant2, self.local_contestant5]
        self.total_team1 = [self.total_contestant1, self.total_contestant4]
        self.total_team2 = [self.total_contestant2, self.total_contestant5]
        self.name_team1 = [self.entry1.get(), self.entry4.get()]
        self.name_team2 = [self.entry2.get(), self.entry5.get()]
        self.score_team1_name.config(text = self.name_team1[0] + " & " + self.name_team1[1])
        self.score_team2_name.config(text = self.name_team2[0] + " & " + self.name_team2[1])
        self.games_played[7] = self.game1425
        self.three_not_playing()#8

    def g1435(self):
        self.local_team1 = [self.local_contestant1, self.local_contestant4]
        self.local_team2 = [self.local_contestant3, self.local_contestant5]
        self.total_team1 = [self.total_contestant1, self.total_contestant4]
        self.total_team2 = [self.total_contestant3, self.total_contestant5]
        self.name_team1 = [self.entry1.get(), self.entry4.get()]
        self.name_team2 = [self.entry3.get(), self.entry5.get()]
        self.score_team1_name.config(text = self.name_team1[0] + " & " + self.name_team1[1])
        self.score_team2_name.config(text = self.name_team2[0] + " & " + self.name_team2[1])
        self.games_played[8] = self.game1435
        self.two_not_playing()#9

    def g1523(self):
        self.local_team1 = [self.local_contestant1, self.local_contestant5]
        self.local_team2 = [self.local_contestant2, self.local_contestant3]
        self.total_team1 = [self.total_contestant1, self.total_contestant5]
        self.total_team2 = [self.total_contestant2, self.total_contestant3]
        self.name_team1 = [self.entry1.get(), self.entry5.get()]
        self.name_team2 = [self.entry2.get(), self.entry3.get()]
        self.score_team1_name.config(text = self.name_team1[0] + " & " + self.name_team1[1])
        self.score_team2_name.config(text = self.name_team2[0] + " & " + self.name_team2[1])
        self.games_played[9] = self.game1523
        self.four_not_playing()#10

    def g1524(self):
        self.local_team1 = [self.local_contestant1, self.local_contestant5]
        self.local_team2 = [self.local_contestant2, self.local_contestant4]
        self.total_team1 = [self.total_contestant1, self.total_contestant5]
        self.total_team2 = [self.total_contestant2, self.total_contestant4]
        self.name_team1 = [self.entry1.get(), self.entry5.get()]
        self.name_team2 = [self.entry2.get(), self.entry4.get()]
        self.score_team1_name.config(text = self.name_team1[0] + " & " + self.name_team1[1])
        self.score_team2_name.config(text = self.name_team2[0] + " & " + self.name_team2[1])
        self.games_played[10] = self.game1524
        self.three_not_playing()#11

    def g1534(self):
        self.local_team1 = [self.local_contestant1, self.local_contestant5]
        self.local_team2 = [self.local_contestant3, self.local_contestant4]
        self.total_team1 = [self.total_contestant1, self.total_contestant5]
        self.total_team2 = [self.total_contestant3, self.total_contestant4]
        self.name_team1 = [self.entry1.get(), self.entry5.get()]
        self.name_team2 = [self.entry3.get(), self.entry4.get()]
        self.score_team1_name.config(text = self.name_team1[0] + " & " + self.name_team1[1])
        self.score_team2_name.config(text = self.name_team2[0] + " & " + self.name_team2[1])
        self.games_played[11] = self.game1534
        self.two_not_playing()#12

    def g2345(self):
        self.local_team1 = [self.local_contestant2, self.local_contestant3]
        self.local_team2 = [self.local_contestant4, self.local_contestant5]
        self.total_team1 = [self.total_contestant2, self.total_contestant3]
        self.total_team2 = [self.total_contestant4, self.total_contestant5]
        self.name_team1 = [self.entry2.get(), self.entry3.get()]
        self.name_team2 = [self.entry4.get(), self.entry5.get()]
        self.score_team1_name.config(text = self.name_team1[0] + " & " + self.name_team1[1])
        self.score_team2_name.config(text = self.name_team2[0] + " & " + self.name_team2[1])
        self.games_played[12] = self.game2345
        self.one_not_playing()#13

    def g2435(self):
        self.local_team1 = [self.local_contestant2, self.local_contestant4]
        self.local_team2 = [self.local_contestant3, self.local_contestant5]
        self.total_team1 = [self.total_contestant2, self.total_contestant4]
        self.total_team2 = [self.total_contestant3, self.total_contestant5]
        self.name_team1 = [self.entry2.get(), self.entry4.get()]
        self.name_team2 = [self.entry3.get(), self.entry5.get()]
        self.score_team1_name.config(text = self.name_team1[0] + " & " + self.name_team1[1])
        self.score_team2_name.config(text = self.name_team2[0] + " & " + self.name_team2[1])
        self.games_played[13] = self.game2435
        self.one_not_playing()#14

    def g2534(self):
        self.local_team1 = [self.local_contestant2, self.local_contestant5]
        self.local_team2 = [self.local_contestant3, self.local_contestant4]
        self.total_team1 = [self.total_contestant2, self.total_contestant5]
        self.total_team2 = [self.total_contestant3, self.total_contestant4]
        self.name_team1 = [self.entry2.get(), self.entry5.get()]
        self.name_team2 = [self.entry3.get(), self.entry4.get()]
        self.score_team1_name.config(text = self.name_team1[0] + " & " + self.name_team1[1])
        self.score_team2_name.config(text = self.name_team2[0] + " & " + self.name_team2[1])
        self.games_played[14] = self.game2534
        self.one_not_playing()#15

    def one_not_playing(self):
        for H in (self.bidder2, self.bidder3, self.bidder4, self.bidder5):
            H.config(state = "normal")
        self.bidder1.config(state = "disabled")
        self.ThirdPage()
            
    def two_not_playing(self):
        for H in (self.bidder1, self.bidder3, self.bidder4, self.bidder5):
            H.config(state = "normal")
        self.bidder2.config(state = "disabled")
        self.ThirdPage()

    def three_not_playing(self):
        for H in (self.bidder2, self.bidder1, self.bidder4, self.bidder5):
            H.config(state = "normal")
        self.bidder3.config(state = "disabled")
        self.ThirdPage()

    def four_not_playing(self):
        for H in (self.bidder2, self.bidder3, self.bidder1, self.bidder5):
            H.config(state = "normal")
        self.bidder4.config(state = "disabled")
        self.ThirdPage()

    def five_not_playing(self):
        for H in (self.bidder2, self.bidder3, self.bidder4, self.bidder1):
            H.config(state = "normal")
        self.bidder5.config(state = "disabled")
        self.ThirdPage()

    def ThirdPage(self):
        for H in (self.game1234, self.game1235, self.game1245, self.game1324, self.game1325, self.game1345, self.game1423, self.game1425, self.game1435, self.game1523, self.game1524,
                  self.game1534, self.game2345, self.game2435, self.game2534):
            H.config(state = "disabled")
        for G in (self.ten, self.nine, self.eight, self.blood, self.heart, self.diamond, self.club, self.spade, self.submit):
            G.config(state = "normal")
    
    def ten(self):
        self.weight = 400

    def nine(self):
        self.weight = 300

    def eight(self):
        self.weight = 200
        
    def blood(self):
        self.suit = 120
        
    def heart(self):
        self.suit = 100

    def diamond(self):
        self.suit = 80
        
    def club(self):
        self.suit = 60
       
    def spade(self):
        self.suit = 40

    def first_bid(self):
        self.bidder = self.entry1.get()

    def second_bid(self):
        self.bidder = self.entry2.get()

    def third_bid(self):
        self.bidder = self.entry3.get()

    def fourth_bid(self):
        self.bidder = self.entry4.get()
        
    def fifth_bid(self):
        self.bidder = self.entry5.get()

    def set_made(self):
        if self.check_undone == False:
            self.check_undone = True
        else:
            self.check_undone = False 

    def set_ftd(self):
        if self.check_ftd == False:
            self.check_ftd = True
        else:
            self.check_ftd = False

    def stats(self):
        tk.messagebox.showinfo(title = "Stats", message = self.entry1.get() + "'s total score is: " + str(self.total_contestant1) + " and took " + str(self.total_count1) + " times" + "\n"
                               + self.entry2.get() + "'s total score is: " + str(self.total_contestant2) + " and took " + str(self.total_count2) + " times" + "\n"
                               + self.entry3.get() + "'s total score is: " + str(self.total_contestant3) + " and took " + str(self.total_count3) + " times" + "\n"
                               + self.entry4.get() + "'s total score is: " + str(self.total_contestant4) + " and took " + str(self.total_count4) + " times" + "\n"
                               + self.entry5.get() + "'s total score is: " + str(self.total_contestant5) + " and took " + str(self.total_count5) + " times" + "\n"
                               + str(self.undone) + " Undone Hands\n"
                               + str(self.ftd) +" Force The Dealers\n"
                               + str(self.blood_score) + " Sans\n"
                               + str(self.heart_score) + " Hearts\n"
                               + str(self.diamond_score) + " Diamond\n"
                               + str(self.club_score) + " Club\n"
                               + str(self.spade_score) + " Spade\n")
        
    def tabulate(self):
        games_possible = [self.game1234, self.game1235, self.game1245, self.game1324, self.game1325, self.game1345, self.game1423, self.game1425, self.game1435, self.game1523, self.game1524,
                  self.game1534, self.game2345, self.game2435, self.game2534]

        score = self.suit+self.weight
    #undone 
        if self.check_undone == True:
            self.undone += 1
    #ftd
        if self.check_ftd == True:
            self.ftd += 1
    #bidders
        if self.bidder == self.entry1.get():
            self.total_count1 += 1
        elif self.bidder == self.entry2.get():
            self.total_count2 += 1        
        elif self.bidder == self.entry3.get():
            self.total_count3 += 1
        elif self.bidder == self.entry4.get():
            self.total_count4 += 1
        else:
            self.total_count5 += 1
            
    #suit of the hand
        if self.suit == 120:
            self.blood_score += 1
        elif self.suit == 100:
            self.heart_score += 1
        elif self.suit == 80:
            self.diamond_score += 1
        elif self.suit == 60:
            self.club_score += 1
        elif self.suit == 40:
            self.spade_score +=1   

        if self.bidder == self.name_team1[0] or self.bidder == self.name_team1[1]:
            
            if self.check_undone == True:
                self.local_team2[1] += score
                self.local_team2[0] += score
                self.total_team2[1] += score
                self.total_team2[0] += score
                self.score_team2_value.config(text = self.local_team2[1])
                for i in range(2):
                    if self.name_team2[i] == self.entry1.get():
                        self.total_contestant1 += score
                    elif self.name_team2[i] == self.entry2.get():
                        self.total_contestant2 += score
                    elif self.name_team2[i] == self.entry3.get():
                        self.total_contestant3 += score
                    elif self.name_team2[i] == self.entry4.get():
                        self.total_contestant4 += score
                    else:
                        self.total_contestant5 += score
                
                
            else:
                self.local_team1[1] += score
                self.local_team1[0] += score
                self.total_team1[1] += score
                self.total_team1[0] += score
                self.score_team1_value.config(text = self.local_team1[1])

                for i in range(2):
                    if self.name_team1[i] == self.entry1.get():
                        self.total_contestant1 += score
                    elif self.name_team1[i] == self.entry2.get():
                        self.total_contestant2 += score
                    elif self.name_team1[i] == self.entry3.get():
                        self.total_contestant3 += score
                    elif self.name_team1[i] == self.entry4.get():
                        self.total_contestant4 += score
                    else:
                        self.total_contestant5 += score
                
                
        elif self.bidder == self.name_team2[0] or self.bidder == self.name_team2[1]:
            if self.check_undone == True:
                self.local_team1[1] += score
                self.local_team1[0] += score
                self.total_team1[1] += score
                self.total_team1[0] += score
                self.score_team1_value.config(text = self.local_team1[1])

                for i in range(2):
                    if self.name_team1[i] == self.entry1.get():
                        self.total_contestant1 += score
                    elif self.name_team1[i] == self.entry2.get():
                        self.total_contestant2 += score
                    elif self.name_team1[i] == self.entry3.get():
                        self.total_contestant3 += score
                    elif self.name_team1[i] == self.entry4.get():
                        self.total_contestant4 += score
                    else:
                        self.total_contestant5 += score
                
            else:
                self.local_team2[1] += score
                self.local_team2[0] += score
                self.total_team2[1] += score
                self.total_team2[0] += score
                self.score_team2_value.config(text = self.local_team2[1])

                for i in range(2):
                    if self.name_team2[i] == self.entry1.get():
                        self.total_contestant1 += score
                    elif self.name_team2[i] == self.entry2.get():
                        self.total_contestant2 += score
                    elif self.name_team2[i] == self.entry3.get():
                        self.total_contestant3 += score
                    elif self.name_team2[i] == self.entry4.get():
                        self.total_contestant4 += score
                    else:
                        self.total_contestant5 += score
                
                
        print(score, "for ", self.bidder)
        print(self.name_team1, " ", self.name_team2)
        print(self.local_team1[0], " ", self.local_team1[1], self.local_team2[0], " ", self.local_team2[1])
        if self.local_team1[0] >= 1000 or self.local_team2[0] >=1000:
            print("Game over")
            self.local_team1[0] = 0
            self.local_team1[1] = 0
            self.local_team2[0] = 0
            self.local_team2[1] = 0
            self.score_team1_value.config(text = "0")
            self.score_team2_value.config(text = "0")
            self.score_team1_name.config(text = "Team 1")
            self.score_team2_name.config(text = "Team 2")

            for i in range(15):
                if self.games_played[i] != games_possible[i]:
                    games_possible[i].config(state = "normal")
        score = 0            
        self.weight = 0
        self.suit = 0
        self.bidder = ""
        self.check_undone = False
        self.check_ftd = False
        self.FTD.deselect()
        self.makeIt.deselect()
        for H in (self.bidder1, self.bidder2, self.bidder3, self.bidder4, self.bidder5, self.ten, self.nine, self.eight, self.blood, self.heart, self.diamond, self.club, self.spade):
            H.deselect()

if __name__ == '__main__':
   root = tk.Tk()
   run = App(root)
   root.mainloop()

