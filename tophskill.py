from trueskill import Rating, rate, rate_1vs1, setup
from pprint import pprint as pp
import glob
import os
import collections

# Results are of the format:
# 1: Toph (3)
# 2: Laudandus (2)
# ...

# 1. Keep a dictionary of player name to player rating
# 2. Parse in results from text file
# 3. Make new ratings for new players. Update ratings of all players that participated in each game


### FFA example
# tebls, sbelmont, sniparook, linosenpai, eppepen = Rating(), Rating(), Rating(), Rating(), Rating()
# print("Tebls: ", tebls)
# print("SBelmont: ", sbelmont)
# print("Sniparook: ", sniparook)
# print("LinoSenpai: ", linosenpai)
# print("Eppepen: ", eppepen)

# rating_groups = [(tebls,), (sbelmont,), (sniparook,), (linosenpai,), (eppepen,)]
# rated_rating_groups = rate(rating_groups, ranks=[0, 1, 2, 2, 4])
# print("Adjusting ratings...")
# (tebls,), (sbelmont,), (sniparook,), (linosenpai,), (eppepen,) = rated_rating_groups

# print("Tebls: ", tebls)
# print("SBelmont: ", sbelmont)
# print("Sniparook: ", sniparook)
# print("LinoSenpai: ", linosenpai)
# print("Eppepen: ", eppepen)


### 1vs1 example
# tebls, sbelmont = Rating(), Rating()
# print(tebls)
# print(sbelmont)
# print("Adjusting ratings...")
# tebls, sbelmont = rate_1vs1(tebls, sbelmont, drawn=True)
# print(tebls)
# print(sbelmont)


setup(draw_probability=0)
ratings = {}
os.chdir("C:\\Users\\Toph\\Dropbox\\TOPH_PACKAGE\\Ranked AMQ\Season 1")
for file in glob.glob("*.txt"):
    print("\nCalculating results from game %s..." % file.split(".")[0])
    with open(file, "r") as fp:
        ranks = []
        rating_groups = []
        line = fp.readline()
        while line:
            rank = int(line.split()[0].split(":")[0])
            name = line.split()[1]

            # Initialize a new rating for new players
            if not name in ratings:
                ratings[name] = Rating()

            # Parse results into rating groups
            ranks.append(rank)
            rating_groups.append({name: ratings[name]})

            line = fp.readline()
        updated_rating_groups = rate(rating_groups, ranks=ranks)

        # Save updated ratings
        for group in updated_rating_groups:
            for name, updated_rating in group.items():
                ratings[name] = updated_rating

    # pp(ratings)

final_rankings = collections.OrderedDict({name: rating for name, rating in sorted(ratings.items(), key=lambda item: -item[1].mu)})
print("\nFinal rankings:")
ranking = 0
for name, rating in final_rankings.items():
    ranking += 1
    print("%s: %s (Rating: %.3f, Uncertainty: %.3f)" % (ranking, name, rating.mu, rating.sigma))
