#functions to be saved here
#Function 1
def dictionary_of_metrics(list):         #
   mean=round(np.mean(list),2)
    median=round(np.percentile(list,50),2)
    var=round(np.var(list,ddof=1),2)
    std=round(np.std(list,ddof=1),2)     #calculates the standard deviation
    mini=round(min(list),2)
    maxi=round(max(list),2)

    keys=['mean','median','var','std','min','max']
    values=[mean,median,var,std,mini,maxi]

    dict ={} #created a dictionary
    for l in range(len(keys)):
        dict[keys[l]]=values[l]
        
    return (dict)
    
#Function 3
    def date_parser(dates):
    parsed_dates=[i.split()[0] for i in dates]
    return(parsed_dates)