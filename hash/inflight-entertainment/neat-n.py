# O(n) solution
from collections import defaultdict

def can_watch_two_movies(flight_length, movie_lengths):
    lengths_map = defaultdict(int)

    for i, first_movie_len in enumerate(movie_lengths):
        if first_movie_len <= 0:
            raise ValueError("Invalid movie lenght zero at index " + str(i))

        second_movie_len = flight_length - first_movie_len

        if second_movie_len in lengths_map:
            return True

        lengths_map[first_movie_len] += 1

    return False


if __name__ == "__main__":
    flight_length = int(input())
    movie_lengths = [int(a) for a in input().split()]
    print(can_watch_two_movies(flight_length, movie_lengths))
