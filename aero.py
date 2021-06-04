from aerofiles.igc import Reader


with open('igcdata/demo.igc', 'r', encoding='cp1251') as f:
    parsed_igc_file = Reader().read(f)


def get_igc_header():
    header = parsed_igc_file["header"][1]
    return header
