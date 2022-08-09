from leboncoin_api_wrapper import Leboncoin

def request_leboncoin(search,limit):
    lbc = Leboncoin()
    lbc.searchFor(search)
    lbc.setLimit(limit)
    lbc.maxPrice(2000)
    lbc.setDepartement("tarn")
    results = lbc.execute()

    return results.ads(), results.shippable_ads()
    
