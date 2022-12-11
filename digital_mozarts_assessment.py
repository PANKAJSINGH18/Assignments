import pandas as pd

def main():
    df = pd.read_csv('data.csv', parse_dates=['reporting_start', 'reporting_end'])
    impression = df[df['age']=='30-34']['impressions'].sum()
    total_clicks = df[ (df['reporting_start']>='19/08/2017') & (df['reporting_start']<='22/08/2017')]['clicks'].sum()
    campaign_dict = dict()
    for col in df['campaign_id'].unique():
        campaign_dict[col] = df[df['campaign_id']==col]['ad_id'].reset_index()['ad_id']
    campaign_df = pd.DataFrame(campaign_dict)

    print('Total Impression whose age group is 30-34 -> ', impression)
    print('Total clicks with reporting start between 19/08/2017 to 22/08/2017 -> ', total_clicks)

    print('\n Ad_id table for unique Campaign id : ')
    print(campaign_df)

if __name__=='__main__':
    main()