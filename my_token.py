def read_token(donor: str) -> str:
    with open(donor, "r", encoding = "utf-8") as file_data_donor:
        data = file_data_donor.read()
    return data