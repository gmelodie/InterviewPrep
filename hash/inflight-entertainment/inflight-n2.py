# O(n^2) solution

def can_watch_two_movies(flight_length, movie_lengths):
    for i, lenght in enumerate(movie_lengths):
        if lenght == 0:
            raise ValueError("Invalid movie lenght zero at index " + str(i))

    for i in range(len(movie_lengths) - 1):
        for j in range(i+1, len(movie_lengths)):
            if flight_length == movie_lengths[i] + movie_lengths[j]:
                return True
    return False


if __name__ == "__main__":
    flight_length = int(input())
    movie_lengths = [int(a) for a in input().split()]
    print(can_watch_two_movies(flight_length, movie_lengths))
