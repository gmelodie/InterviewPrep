# O(nlogn) solution

def can_watch_two_movies(flight_length, movie_lengths):
    movie_lengths = sorted(movie_lengths)

    if movie_lengths[0] <= 0:
        raise ValueError("Invalid movie length " + str(movie_lengths[0]) + \
                         " at index 0")

    i = 0
    j = len(movie_lengths) - 1

    while i < j:
        total_length = movie_lengths[i] + movie_lengths[j]
        if total_length > flight_length:
            j -= 1
        elif total_length < flight_length:
            i += 1
        else:
            return True

    return False


if __name__ == "__main__":
    flight_length = int(input())
    movie_lengths = [int(a) for a in input().split()]
    print(can_watch_two_movies(flight_length, movie_lengths))
