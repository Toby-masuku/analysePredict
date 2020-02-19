import numpy as np
import pandas as pd

#Function 1
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
    median=np.percentile(list,50)
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

def date_parser(dates):
    """
    removes time from the date
    eg input: dates[:3] == [
    '2019-11-29 12:50:54',
    '2019-11-29 12:46:53',
    '2019-11-29 12:46:10']

    output: ['2019-11-29', '2019-11-29', '2019-11-29']

    """

#Create a new list with a list comprehension that split time from the date
    parsed_dates=[i.split()[0] for i in dates]
    return(parsed_dates)


#function 2
def five_num_summary(list):
    """
    This functions give the maximum, minimum, median, 1st quartile of a given list as a dictionary:

    input:
    fn([1,2,3])
    ___________________

    Output:
    [1,2,3]

    {max:3.0, min: 1.0, median:2.0, q1: 1.5, q3: 2.5}
    """
    # create dictionary for five number summary
    dict={'max':round(np.max(list),2),
    'min':round(np.min(list),2),
    'median':round(np.percentile(list,50),2),
    'q1':round(np.percentile(list,25),2),
    'q3':round(np.percentile(list,75),2)}
    
    return (dict)
    
#function 6
def word_splitter(df):
    """
    This function splits the sentences in dataframe's column into list of separate words
    """
    df['Split Tweets']=df['Tweets'].str.lower().str.split(" ")
    return (df)

#Function 5

def number_of_tweets_per_day(df):
    '''
    This function takes a pandas dataframe as input.
    It then returns a new dataframe, grouped by day, with the number of tweets for that day.
    '''
    #Function removes time values from the dates' column
    def fn (row):
        row.Date=row.Date.split()[0]
        return(row)
    #Slices column's dates and tweets
    df_sliced=df.loc[:,['Date','Tweets']].apply(fn,axis=1)
    #Use pd.datetime to change date into datetime object
    df_sliced.Date=pd.to_datetime(df_sliced.Date,format='%Y-%m-%d')
    df_count=df_sliced.groupby('Date').count()
    return (df_count)
    
#Function 4:
def extract_municipality_hashtags(df):
    """ This is a function which extracts Tweets and Municipality names from a tweet.
     ---------------------------------------------------------------------------
     1. It  take a pandas dataframe as input.
     2. The function extracts the municipality twitter usernames and maps them to the municipal dictionary keys.
     3. The function then extracts all hashtags in the 'Tweets Column' and stores the result as a list in Hashtags column.
     4. Function modifies the DataFrame
     5. Finally the Function will return the modified Data Frame
     --------------------------------------------------------------------------- 
     """

    df['municipality']=np.nan
    df['hashtags']=df.Tweets.str.split(' ')
    def fn(row):
        row.municipality=[mun_dict[i] for i in row.hashtags if i in mun_dict.keys()] #Municipality @ extracted to 'Municipality' column
        row.hashtags=[i.lower() for i in row.hashtags if '#' in i]                   #Extraction of hashtags
        if len(row.hashtags)==0:
            row.hashtags=np.nan  
        if len(row.municipality)==0:
            row.municipality=np.nan
        return(row)
    df=df.apply(fn,axis=1)
    return (df)

# Function 7

def stop_words_remover(df):
    """ This is a function which removes english stop words from a tweet.
     ---------------------------------------------------------------------------
     1. It  take a pandas dataframe as input.
     2. It  tokenise the sentences according to the definition in function 6.
     3. uses the stop_words_dict and remove all stop words in the tokenised list.
     4. "Without Stop Words" stores the localized column.
     5. Function modifies the DataFrame
     6. Finally the Function will return the modified Data Frame
     --------------------------------------------------------------------------- 
     """

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