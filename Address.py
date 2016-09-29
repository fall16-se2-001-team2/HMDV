#address contains the "throwaway" part of the Provider class.
class Address:
    name = ""
    address = ""
    address2 = ""
    city = ""
    state = ""
    zip = ""
    eligibility = ""

    def __init__(self,name, address, address2, city, state,zip, eligibility):
        name = name
        address = address
        address2 = address2
        city = city
        state = state
        zip = zip
        eligibility = eligibility