"""This function will left join two hash maps into one."""


def left_join(HM1, HM2):
    """Left join 2 hash maps."""
    final = dict()
    for key in HM1:
        final[key] = [HM1.get(key), None]
    for key in HM2:
        if key in final:
            final[key][1] = HM2.get(key)

    return final
