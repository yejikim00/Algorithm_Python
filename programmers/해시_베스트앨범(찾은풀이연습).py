def solution(genres, plays):
    answer = []
    dic = {}
    # dic 딕셔너리에 { "장르1": [[재생 횟수, 고유 번호], [재생 횟수, 고유 번호]] } 형식으로 담자!
    for i in range(len(genres)):
        if genres[i] in dic:
            dic[genres[i]].append([plays[i], i])
        else:
            dic[genres[i]] = [[plays[i], i]]

    # genre_rank에 각 장르의 총 재생 횟수를 담음.
    genre_rank = {}
    for genre in dic.keys():
        songs = dic[genre]
        plays_sum = 0
        for song in songs:
            plays_sum += song[0]
        genre_rank[genre] = [plays_sum]

    # genre_rank를 재생 횟수가 큰 순으로 정렬한다.
    genre_rank = sorted(genre_rank.items(), key=lambda x: x[1], reverse=True)

    # genre_rank에 저장된 장르 순으로 dic의 장르를 Key로 가진 value 확인.
    for genre in genre_rank:
        # 2차원 배열인 value를 다중 조건으로 정렬(첫 번째 조건: 첫 번째 인자인 곡 재생 수를 기준으로 내림차순 정렬(-x[0])
        #                                            두 번째 인자인 고유 번호를 기준으로 오름차순 정렬
        song_rank = sorted(dic[genre[0]], key=lambda x: -x[0])
        best_two = 0
        # song_rank를 돌면서 앞에서 두 번째로 큰 노래까지의 노래의 고유 번호를 best_two에 담는다. 순서대로!
        # 만약 한 장르의 곡이 두 곡이 저장되면 그 장르의 반복을 중지한다.
        for song in song_rank:
            answer.append(song[1])
            best_two += 1
            if best_two == 2:
                break

    return answer


genres = ["classic", "pop", "classic", "classic", "pop"]
plays = [500, 600, 150, 800, 2500]
print(solution(genres, plays))