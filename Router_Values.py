import pandas as pd
from glob import glob


def GetRouteValues(df_path, dir_path, prod1, prod2):
    """
    Input: 
        df_path => path of the csv containing id and matched values
        dir_path => path of the fodler containing html
        prod1 => name of 1 mission (e.g. CSK, SAO, SEN)
        prod2 => name of 1 mission (e.g. CSK, SAO, SEN)

    Output:
        idx, prod1: names, prod2:names, links: hrefs to htmls
    """
    df = pd.read_csv(df_path)

    Prod1 = df[f'{prod1}'].to_list() 
    Prod2 = df[f'{prod2}'].to_list()
    idx = df['Unnamed: 0'].to_list()


    hrefs = glob(dir_path+'\\*.html')
    hrefs = sorted(hrefs, key=lambda x: int(x.split('_')[1].split('__')[0]))
    hrefs = [x.split('\\')[-1] for x in hrefs]

    out = {'idx':idx, f'{prod1}':Prod1, f'{prod2}':Prod2, 'links':hrefs}
    return out


if __name__ == "main":
    pass