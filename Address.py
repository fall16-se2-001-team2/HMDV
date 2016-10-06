# --------------------------------------------------------------------------
# address contains the "throwaway" part of the Provider class
# --------------------------------------------------------------------------
class Address:
    name = ""
    address = ""
    address2 = ""
    city = ""
    state = ""
    zip = ""
    eligibility = ""
#Address(name:string, address:string, address2:string, city:string, state:string, zip:string, eligibility:string, isMobile:boolean):void
    def __init__(self,name, address, address2, city, state,zip, eligibility):
        name = name
        address = address
        address2 = address2
        city = city
        state = state
        zip = zip
        eligibility = eligibility
