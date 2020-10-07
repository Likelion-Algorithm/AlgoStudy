def solution(genres, plays):
    order = []
    all_songs = sorted(list(zip(genres, plays)), reverse=True)
    print(all_songs,'\n')
    tot_genre = {}.fromkeys([g for g in set(genres)], 0)
    for (genre, plays) in all_songs:
        tot_genre[genre] += plays
    for i in sorted(tot_genre, key=lambda x: x[1], reverse=True):
        print(i)
        for pair in all_songs:
            print(pair[0])
            stop=False
            while stop==False:
                if i == pair[0]:
                    index = all_songs.index(pair)
                    order.append([index, int(index+1)])
                    stop==True
    print(order)
