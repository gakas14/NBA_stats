import pandas as pd
from nba_api.stats.static import *
import numpy as np
import streamlit as st


def get_player_id(player_list, name):

    #player_list = players.get_players()
    #player_list = pd.DataFrame(player_list)

    #st.dataframe(player_list)
    p_id = 0
    active = False
    for p in range(len(player_list)):
        #st.write(p)
        #print(all_players_list.iloc[p])
        if player_list.iloc[p]['full_name'].lower() == name.lower():
            p_id = player_list.iloc[p]['id']
            active = player_list.iloc[p]['is_active']
            break
    return p_id, active

def avg_data(data_set):
    # Get the regular sesson avg
    return_df = {}
    for i in data_set:
        if i not in ['GP', 'FT_PCT', 'FG3_PCT', 'FG_PCT']:
            return_df[i] = data_set[1][i] / data_set[1]['GP']
        else:
            return_df[i] = data_set[1][i]
    return_df = pd.DataFrame(return_df, index=[0])


def formatage_pct(data_set):
    #pd.options.display.float_format = '{:,.2f}'.format
    for i in data_set:
        # print(i)`
        if 'PCT' in i:
            data_set[i] = data_set[i].map('{:,.2f}%'.format)

    return data_set

def formatage_data_set(data_set):
    for i in data_set:
        # print(i)`
        if 'PCT' in i:
            data_set[i] = data_set[i].map('{:,.2f}%'.format)




def get_current_season(player_id):
    #player_info = commonplayerinfo.CommonPlayerInfo(player_id=player_id)
    #df_player_info = player_info.get_data_frames()

    df_player_info = pd.read_csv('df_player_info.csv')
    #df_player_info[1]
    #player_bio = df_player_info[0]
    player_season_stats = df_player_info


    #a_player_gamelog = playergamelog.PlayerGameLog(player_id=player_id)
    #df_player_gamelog = a_player_gamelog.get_data_frames()
    #player_gamelog = df_player_gamelog[0]

    player_gamelog = pd.read_csv('player_gamelog.csv')

    shooting_data = pd.DataFrame(
        columns=['Player_ID', 'PLAYER_NAME', 'FGM', 'FGA', 'FG_PCT', 'FG3M', 'FG3A', 'FG3_PCT', 'FTM', 'FTA',
                 'FT_PCT'])
    current_stats = pd.DataFrame(
        columns=['Player_ID', 'PLAYER_NAME', 'OREB', 'DREB', 'REB', 'AST', 'STL', 'BLK', 'TOV', 'PF',
                 'PTS', 'PLUS_MINUS'])

    # Get the player points, assist....
    player_stats = {}
    for i in current_stats:
        if i == 'PLAYER_NAME':
            player_stats[i] = player_season_stats['PLAYER_NAME']
        else:

            player_stats[i] = player_gamelog[i].mean()
    player_stats = pd.DataFrame(player_stats, index=[0])

    # Get the shooting percentage
    shooting_avg = {}
    for i in shooting_data:
        if i == 'PLAYER_NAME':
            shooting_avg[i] = player_season_stats['PLAYER_NAME']
        else:
            shooting_avg[i] = player_gamelog[i].mean()
    shooting_avg = pd.DataFrame(shooting_avg, index=[0])

    return player_stats, shooting_avg


def get_career_stats(player_id):
    #pd.options.display.float_format = '{:,.2f}'.format
    #p = playerprofilev2.PlayerProfileV2(player_id=player_id)
    #df_p = p.get_data_frames()

    df_p0 = pd.read_csv('regular_s.csv')
    df_p1 = pd.read_csv('total_reg_s.csv')
    df_p2 = pd.read_csv('playoff.csv')
    df_p3 = pd.read_csv('total_playoff.csv')
    df_p4 = pd.read_csv('all_star.csv')
    df_p5 = pd.read_csv('total_all_star.csv')

    regular_season = df_p0

    regular_season['PLAYER_AGE'] = regular_season['PLAYER_AGE'].astype(str)
    #regular_season.set_index('SEASON_ID', inplace=True)
    #regular_season = regular_season.drop(['PLAYER_ID', 'LEAGUE_ID','TEAM_ID'], axis=1)

    regular_season_tot = regular_season.append(df_p1)
    regular_season_tot = regular_season_tot.reset_index(drop=True)
    #regular_season_tot.set_index('SEASON_ID', inplace=True)
    regular_season_tot = regular_season_tot.drop(['PLAYER_ID', 'LEAGUE_ID', 'TEAM_ID'], axis=1)
    #regular_season_tot = regular_season_tot.reset_index(drop=True)
    #regular_season_tot = regular_season_tot.fillna('-')




    playoff_stats = df_p2
    playoff_stats['PLAYER_AGE'] = playoff_stats['PLAYER_AGE'].astype(str)
    #playoff_stats.set_index('SEASON_ID', inplace=True)
    #playoff_stats = playoff_stats.drop(['PLAYER_ID', 'LEAGUE_ID', 'TEAM_ID'], axis=1)
    playoff_stats_tot = playoff_stats.append(df_p3)
    playoff_stats_tot = playoff_stats_tot.drop(['PLAYER_ID', 'LEAGUE_ID', 'TEAM_ID'], axis=1)

    allstar_stats = df_p4
    allstar_stats['PLAYER_AGE'] = allstar_stats['PLAYER_AGE'].astype(str)
    #allstar_stats.set_index('SEASON_ID', inplace=True)
    #allstar_stats = playoff_stats.drop(['PLAYER_ID', 'LEAGUE_ID', 'TEAM_ID'], axis=1)
    allstar_stats_tot = allstar_stats.append(df_p5)
    allstar_stats_tot = allstar_stats_tot.drop(['PLAYER_ID', 'LEAGUE_ID', 'TEAM_ID'], axis=1)

    return regular_season, regular_season_tot, playoff_stats, playoff_stats_tot, allstar_stats, allstar_stats_tot


