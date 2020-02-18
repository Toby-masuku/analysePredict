#functions to be saved here
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
