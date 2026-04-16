def main():
    trainer_levels = {}

    all_species = set()

    with open("contest.txt", "r") as f:
        for line in f:
            line = line.strip()
            if not line:
                continue

            parts = line.split(',')
            trainer_name = parts[0]
            pakuri_list = parts[1:]

            levels = []
            for pakuri in pakuri_list:
                pieces = pakuri.split("-")
                species = pieces[0]
                level = int(pieces[1])

                levels.append(level)

                all_species.add(species)
            trainer_levels[trainer_name] = levels


    # find winner (single highest level pakuri)
    winner = ""
    MAX_lvl = -1
    for trainer in trainer_levels:
        for level in trainer_levels[trainer]:
            if level > MAX_lvl:
                MAX_lvl = level
                winner = trainer

    with open("winner.txt", "w") as f:
        f.write(winner)

    # write sorted distinct species to pakuri.txt
    all_species = sorted(all_species)

    with open("pakuri.txt", "w") as f:
        for species in all_species:
            f.write(species + "\n")

main()