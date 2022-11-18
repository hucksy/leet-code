import statistics as stats

filename = "./data/techcrunch.csv"

lines = (line for line in open(filename))
list_line = (s.rstrip().split(",") for s in lines)
cols = next(list_line)
company_dicts = (dict(zip(cols, data)) for data in list_line)
funding = (
        int(company_dict['raisedAmt']) 
        for company_dict in company_dicts 
        if company_dict['round'] == 'a'
        )
round_a_funding = stats.mean(funding)
print(round_a_funding)