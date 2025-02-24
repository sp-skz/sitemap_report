import pandas as pd

def get_folders(df:pd.DataFrame, domain:str, root_language=None):
    df['language']=df['url'].str.extract(domain + r"([a-zA-Z]{2})(?:/|$)").fillna(root_language)
    df['path'] = df['url'].str.replace(domain + r"([a-zA-Z]{2})(?:/|$)", '/', regex=True)
    df['path'] = df['path'].str.replace(domain, '/')
    df_split = df['path'].str.split('/', expand=True)
    df_split.columns = [f'folder_{i}' for i in range(df_split.shape[1])]
    df_split = df_split
    df = df.join(df_split)
    return df.drop(['folder_0','path'], axis=1)