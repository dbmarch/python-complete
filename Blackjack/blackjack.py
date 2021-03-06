import random

try:
    import tkinter
except ImportError:
    import Tkinter as tkinter


def _load_images(card_images):
    suits = ['heart', 'club', 'diamond', 'spade']
    face_cards = ['jack', 'queen', 'king']
    if tkinter.TkVersion >= 8.6:
        extension = "png"
    else:
        extension = "ppm"
    for suit in suits:
        for card in range(1, 11):
            name = 'cards/{}_{}.{}'.format(card, suit, extension)
            image = tkinter.PhotoImage(file=name)
            card_images.append((card, image,))
        for card in face_cards:
            name = 'cards/{}_{}.{}'.format(card, suit, extension)
            image = tkinter.PhotoImage(file=name)
            card_images.append((10, image,))


def _deal_card(frame):
    next_card = deck.pop(0)
    tkinter.Label(frame, image=next_card[1], relief='raised').pack(side='left')
    return next_card


def _score_hand(hand):
    score = 0
    ace = False
    for next_card in hand:
        card_value = next_card[0]
        if card_value == 1 and not ace:
            ace = True
            card_value = 11
        score += card_value
        if score > 21 and ace:
            score -= 10
            ace = False
    return score


def _deal_dealer():
    dealer_score = _score_hand(dealer)
    while 0 < dealer_score < 17:
        dealer_score = _score_hand(dealer)
        dealer.append(_deal_card(dealer_card_frame))
        dealer_score_label.set(dealer_score)
    player_score = _score_hand(player)
    if player_score > 21:
        result_text.set("Dealer wins!")
    elif dealer_score > 21 or dealer_score < player_score:
        result_text.set("Player wins!")
    elif dealer_score > player_score:
        result_text.set("Dealer wins!")
    else:
        result_text.set("Draw!")


def _deal_player():
    player.append(_deal_card(player_card_frame))
    player_score = _score_hand(player)

    player_score_label.set(player_score)
    if player_score > 21:
        result_text.set("Dealer Wins!")


def _setup_game():
    global dealer_card_frame
    global player_card_frame
    global dealer
    global player
    global deck

    deck = list(cards) + list(cards) + list(cards)
    random.shuffle(deck)

    dealer_card_frame = tkinter.Frame(card_frame, background='green')
    dealer_card_frame.grid(row=0, column=1, sticky="ew", rowspan=2)

    player_card_frame = tkinter.Frame(card_frame, background='green')
    player_card_frame.grid(row=2, column=1, sticky="ew", rowspan=2)

    dealer = []
    player = []

    result_text.set("")


def _initial_deal():
    _deal_player()
    dealer.append(_deal_card(dealer_card_frame))
    dealer_score_label.set(_score_hand(dealer))
    _deal_player()


def _new_game():
    global dealer_card_frame
    global player_card_frame
    dealer_card_frame.destroy()
    player_card_frame.destroy()
    _setup_game()
    _initial_deal()


def play():
    _initial_deal()
    mainWindow.mainloop()


mainWindow = tkinter.Tk()

# Set up the screen and frames for the dealer and player.
mainWindow.title("Blackjack")
mainWindow.geometry("640x480")
mainWindow.configure(background="green")

result_text = tkinter.StringVar()
result = tkinter.Label(mainWindow, textvariable=result_text)
result.grid(row=0, column=0, columnspan=3)
result_text.set("")

card_frame = tkinter.Frame(mainWindow, relief="sunken", borderwidth=1, background="green")
card_frame.grid(row=1, column= 0, sticky="ew", columnspan=3, rowspan=2)

dealer_score_label = tkinter.IntVar()
tkinter.Label(card_frame, text="Dealer", background="green", fg="white").grid(row=0,column=0)
tkinter.Label(card_frame, textvariable=dealer_score_label, background="green", fg="white").grid(row=1,column=0)

player_score_label = tkinter.IntVar()
tkinter.Label(card_frame, text="Player", background="green", fg="white").grid(row=2,column=0)
tkinter.Label(card_frame, textvariable=player_score_label, background="green", fg="white").grid(row=3,column=0)

button_frame = tkinter.Frame(mainWindow)
button_frame.grid(row=3, column=0, columnspan=3, sticky="w")

dealer_button = tkinter.Button(button_frame, text="Dealer", command = _deal_dealer)
dealer_button.grid(row=0, column=0)

player_button = tkinter.Button(button_frame, text="Player", command=_deal_player)
player_button.grid(row=0, column=1)

restart_button = tkinter.Button(button_frame, text="New Game", command=_new_game)
restart_button.grid(row=0, column=3)

cards = []
_load_images(cards)

_setup_game()

if __name__ == "__main__":
    play()

