#functions to be saved here
#Function 1
def dictionary_of_metrics(list):
    mean=round(np.mean(list),2)
    median=round(np.percentile(list,50),2)
    var=round(np.var(list,ddof=1),2)
    std=round(np.std(list,ddof=1),2)
    mini=round(min(list),2)
    maxi=round(max(list),2)

    keys=['mean','median','var','std','min','max']
    values=[mean,median,var,std,mini,maxi]

    dict ={} #created a dictionary
    for l in range(len(keys)):
        dict[keys[l]]=values[l]

    return (dict)
#function 2
def five_num_summary(items):
   
    return{'max':max(items),
          'median':np.median(items),
          'min':min(items),
          'qi':np.quantile(items,q=0.25),
          'q3':np.quantile(items,q=0.75)}
#function 6

def word_splitter(df):
    df['Split Tweets']=df['Tweets'].str.lower().str.split(" ")
    return (df)

#Function 4:
def extract_municipality_hashtags(df):
    df['municipality']=np.nan
    df['hashtags']=df.Tweets.str.split(' ')
    def fn(row):
        row.municipality=[mun_dict[i] for i in row.hashtags if i in mun_dict.keys()] #list of the words with @ in them
        row.hashtags=[i.lower() for i in row.hashtags if '#' in i]
        if len(row.hashtags)==0:
            row.hashtags=np.nan  
        if len(row.municipality)==0:
            row.municipality=np.nan
        return(row)
    df=df.apply(fn,axis=1)
    return (df)

    ## Function 7

def stop_words_remover(df):
    # copy df into a new data frame: df_new
    df_new = df.copy()

    # empty list to store tokens
    tokens = []

    # get tweets in list format
    tweets = list(df['Tweets'])

    # loop over tweets, tokenizing and removing stopwords
    for item in tweets:
      tok = item.lower().split()
      tokens.append([i for i in tok if i not in stop_words_dict['stopwords']])

    # add tokens to new_df in a new column: 'Split Tweets'
    df_new['Without Stop Words'] = tokens

    return df_new
#Function 3
def date_parser(dates):
    parsed_dates=[i.split()[0] for i in dates]
    return(parsed_dates)