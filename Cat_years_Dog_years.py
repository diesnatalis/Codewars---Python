def human_years_cat_years_dog_years(human_years):
    if human_years == 1:
        return [1,15,15]
    elif human_years == 2:
        return [2,24,24]
    else:
        catYears = 24
        for x in range(human_years - 2):
            catYears = catYears + 4
        dogYears = 24
        for y in range(human_years - 2):
            dogYears = dogYears + 5
        return [human_years,catYears,dogYears]
