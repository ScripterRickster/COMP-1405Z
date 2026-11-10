def sort_cities_by_rainfall(observations):
    """Return unique city names in increasing order of total rainfall.

    observations is a nonempty list of [city_name, rainfall_amount] lists.
    Equal totals may appear in either order. Do not modify any input lists.
    Do not use sorted() or list.sort().
    """

    # Write your solution here.

    total_dict = {}
    ordered_list = []

    for i in observations:
        if i[0] not in total_dict:
            total_dict[i[0]] = float(i[1])
            ordered_list.append(i[0])
        else:
            total_dict[i[0]] += float(i[1])

    while True:
        sorted = True
        for i in range(len(ordered_list)-1):
            if total_dict[ordered_list[i]] > total_dict[ordered_list[i+1]]:
                ordered_list[i],ordered_list[i+1] = ordered_list[i+1],ordered_list[i]
                sorted = False
        if sorted: break

    return ordered_list

