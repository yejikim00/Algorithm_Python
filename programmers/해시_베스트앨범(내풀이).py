def solution(genres, plays):
    play = {}
    play_sum = {}
    sum = 0
    for g, p in zip(genres, plays):
        if g in play.keys():
            play[g].append(p)
        else:
            play[g] = [p]

    for g in play:
        if g in play_sum.keys():
            for p in play[g]:
                sum += p
                play_sum[g].append(sum)
        else:
            for p in play[g]:
                sum += p
                play_sum[g] = [sum]
        sum = 0

    print(play_sum.values())


genres = ["classic", "pop", "classic", "classic", "pop"]
plays = [500, 600, 150, 800, 2500]
solution(genres, plays)