import argparse
import sys

import pandas as pd

def argumentParsing():
    parser = argparse.ArgumentParser(description="Mutation recomendation", formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument("-d", "--dominant", action=argparse.BooleanOptionalAction, default=True, help="Dominant states algorithms (True/False)")
    parser.add_argument("-g", "--group", type=str, help="The group of algorithms you want, if you select a specific group it will ignore the dominant or not value")
    parser.add_argument("-a", "--algorithm", type=str, help="The specific algorithm you want, if you choose a specific algorithm it will ignore the group value")
    parser.add_argument("-sr", "--sr", default=1, type=float, help="Max survival rate for mutants, value between 0 and 1 (Float)")
    parser.add_argument("-n", "--number", default=5, type=int, help="Number of mutants")
    args = parser.parse_args()
    config = vars(args)
    if config['dominant']==True:
        config['dominant'] = 'yes'
    else:
        config['dominant'] = 'no'

    return config

def get_recomendations(dominant,group,algorithm,sr,number):
    df_total = pd.read_csv('merged_data_001.csv')
    if algorithm:
        df_selected = df_total[df_total['algorithm_group'] == algorithm]
        df1 = df_selected.groupby(['Operator', 'Position', 'Gate'])['Killed'].value_counts(normalize=True)
        df1 = df1.rename('SR').reset_index()
        df_surv = df1[df1['Killed'] == 'Survivor']
        df_surv_below = df_surv[df_surv['SR'] <= sr]
        df_top = df_surv_below.sort_values(by=['SR'], ascending=False)[
            ['Operator', 'Position', 'Gate', 'SR']].head(number)
    elif group:
        df_selected = df_total[df_total['algorithm_group'] == group]
        df1 = df_selected.groupby(['Operator', 'Position', 'Gate'])['Killed'].value_counts(normalize=True)
        df1 = df1.rename('SR').reset_index()
        df_surv = df1[df1['Killed'] == 'Survivor']
        df_surv_below = df_surv[df_surv['SR'] <= sr]
        df_top = df_surv_below.sort_values(by=['SR'], ascending=False)[
            ['Operator', 'Position', 'Gate', 'SR']].head(number)
    else:
        df_selected = df_total[df_total['dominant_state'] == dominant]
        df1 = df_selected.groupby(['Operator', 'Position', 'Gate'])['Killed'].value_counts(normalize=True)
        df1 = df1.rename('SR').reset_index()
        df_surv = df1[df1['Killed'] == 'Survivor']
        df_surv_below = df_surv[df_surv['SR'] <= sr]
        df_top = df_surv_below.sort_values(by=['SR'], ascending=False)[
            ['Operator', 'Position', 'Gate', 'SR']].head(number)



    return df_top


if __name__ == "__main__":
    config = argumentParsing()
    recomendations = get_recomendations(config['dominant'], config['group'], config['algorithm'], config['sr'],
                                        config['number'])
    print(recomendations.to_string(index=False))