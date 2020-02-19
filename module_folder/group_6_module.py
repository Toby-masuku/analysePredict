import numpy as np
import pandas as pd

def dictionary_of_metrics(list):
    """
    This functions give the maximum, minimum, median, 1st quartile of a given list as a dictionary:

    input:
        fn([1,2,3])
    ___________________

    Output:
        [1,2,3]

    {max:3.0, median:2.0, min: 1.0, q1: 1.5, q2: 2.5}
    """
### creating values for the dictionary and rounding them up to 2 decimal places
    mean=round(np.mean(list),2)
    var=round(np.var(list,ddof=1),2)
    std=round(np.std(list,ddof=1),2)
    mini=round(min(list),2)
    maxi=round(max(list),2)

### setting values for dictionary

    keys=['mean','median','var','std','min','max']
    values=[mean,median,var,std,mini,maxi]

    dict ={} #created a dictionary
    for l in range(len(keys)):
        dict[keys[l]]=values[l]
    return (dict)
    
#Function 3
"""removes time from the date
    eg input: dates[:3] == [
    '2019-11-29 12:50:54',
    '2019-11-29 12:46:53',
    '2019-11-29 12:46:10']

    output: ['2019-11-29', '2019-11-29', '2019-11-29']
  
"""
def date_parser(dates):

### create a new list with a list comprehension that split time from the date
    parsed_dates=[i.split()[0] for i in dates]
    return(parsed_dates)

#function2
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

#Function 5
def number_of_tweets_per_day(df):
    def fn (row):
        row.Date=row.Date.split()[0]
        return(row)
    df_sliced=df.loc[:,['Date','Tweets']].apply(fn,axis=1)
    
    df_sliced.Date=pd.to_datetime(df_sliced.Date,format='%Y-%m-%d')
    df_count=df_sliced.groupby('Date').count()
    return (df_count)
    
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
    
"""" This is a function which removes english stop words from a tweet.
     ---------------------------------------------------------------------------
     1. It  take a pandas dataframe as input.
     2. It  tokenise the sentences according to the definition in function 6.
     3. uses the stop_words_dict and remove all stop words in the tokenised list.
     4. "Without Stop Words" stores the localized column.
     5. Function modifies the DataFrame
     6. Finally the Function will return the modified Data Frame
     --------------------------------------------------------------------------- """"

def stop_words_remover(df):
    # copy df into a new data frame: df_new
    df_new = df.copy()

    # empty the list to store tokens.
    tokens = []

    # get tweets in the list format.
    tweets = list(df['Tweets'])

    # looping over tweets, tokenizing and removing stopwords.
    for item in tweets:
      tok = item.lower().split()
      tokens.append([i for i in tok if i not in stop_words_dict['stopwords']])

    # add tokens to new_df in a new column: 'Split Tweets'
    df_new['Without Stop Words'] = tokens

    return df_new
