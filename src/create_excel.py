import pandas as pd
from datetime import datetime
import os

def crearte_excel(df:pd.DataFrame, name:str):
    file_name = f"{datetime.today().strftime('%Y-%m-%d')}_{name}_sitemap-report.xlsx"
    user = os.getlogin()
    path = rf"C:\Users\{user}\Sekuenz\SKZ - T - Team\02.CUENTAS\{name}\02.PRO\05.SEO\05.ROBOTS & SITEMAP\{file_name}"

    with pd.ExcelWriter(path, engine='xlsxwriter') as writer:
        workbook=writer.book
        df.to_excel(writer,sheet_name='raw',index=False)
        summary = workbook.add_worksheet('summary')
        errors = workbook.add_worksheet('errors')

        title_format = workbook.add_format({'bold': True, 'font_size': 14, 'align': 'center'})

        lan_num=0

        for language in df['language'].unique():
            df_lan = df[df['language']==language].drop('language', axis=1)
            
            status_counts = df_lan['status_code'].value_counts().reset_index(name='num. url')
            summary.write(0,lan_num, f'{language.upper()} Sitemap',title_format)
            status_counts.to_excel(writer, sheet_name='summary', startrow=1, startcol=lan_num,index=False)

            error_urls= df_lan[~df_lan['indexable']][['url', 'status_code']]
            errors.write(0,lan_num, f'{language.upper()} URLs',title_format)
            error_urls.to_excel(writer, sheet_name='errors', startrow=1, startcol=lan_num,index=False)

            df_lan = df_lan[df_lan.columns[1:].tolist() + [df_lan.columns[0]]]
            df_lan.to_excel(writer, sheet_name=f'{language}_folders',index=False)
            lan_num=lan_num+3
            

