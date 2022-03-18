import streamlit as st
from data_cleaning import *
import plotly.graph_objects as go
import plotly.express as px
# Import subprocess
from subprocess import call

#@st.cache(suppress_st_warning=True)
def get_basic_stats():
    #player_name = ""
    # Get the payer your looking for
    player_name = st.text_input("Search for a particular player here <Player full name>", value=" ")
    #st.write(player_name)


    # Get the player currstreamlitent season stats.
    # Button
    p_id = 0
    #if st.button('Get Data'):
    if player_name:
        # Run the code to get the player id and if player is still active or not.
        st.write(player_name.upper(), "'s profile.")
        #call(['python', 'app.py', player_name])
        p_id, active = get_palyer_id(player_name)
        #call(['python', 'app.py', player_name])
        #st.write(p_id)
        #st.write( active)
        if active:
            # if the player is still active then get his current season stats
            player_stats, shooting_avg = get_current_season(p_id)

            player_stats = formatage_pct(player_stats)
            shooting_avg = formatage_pct(shooting_avg)

            st.write(player_name, "'s current season stats")
            #st.write(player_stats.style.format("{:.}"))
            st.dataframe(player_stats.style.format(subset=['Player_ID', 'OREB', 'DREB', 'REB', 'AST', 'STL', 'BLK', 'TOV', 'PF', 'PTS', 'PLUS_MINUS'], formatter="{:.2f}"))
            #st.write(player_stats)
            st.write(player_name, "'s Shooting stats")
            st.dataframe(shooting_avg.style.format(
                subset=['Player_ID', 'FGM', 'FGA', 'FG3M', 'FG3A', 'FTM', 'FTA'], formatter="{:.2f}"))
            pie_chart(p_id, player_name)
            #st.write(shooting_avg)
        else:
            st.write("Player Not active or not find.")






    return p_id, player_name


# Get a pie chart of a player points.
def pie_chart(p_id, player_name):
        p_d = playerdashboardbyshootingsplits.PlayerDashboardByShootingSplits(player_id=p_id)
        df_p = p_d.get_data_frames()

        shot_area = df_p[3][['GROUP_VALUE', 'FGM', 'FGA', 'FG_PCT']]
        shot_area = pd.DataFrame(shot_area)

        # left_col, right_col = st.columns(2)

        fig2 = go.Figure(data=[
            go.Pie(labels=shot_area['GROUP_VALUE'], values=shot_area['FGM'], textinfo='label+percent',
                   insidetextorientation='radial')])

        fig2.update_layout(title_text=f"{player_name}'s Current season Shots made repartition.")
        # left_col.plotly_chart(fig2, use_container_width=True)
        st.plotly_chart(fig2, use_container_width=True)

        fig3 = go.Figure(data=[
            go.Pie(labels=shot_area['GROUP_VALUE'], values=shot_area['FGA'], textinfo='label+percent',
                   insidetextorientation='radial')])

        fig3.update_layout(title_text=f"{player_name}'s Current season Shots attempted repartition.")
        fig3.update_traces(hoverinfo='label+percent', textinfo='percent', textfont_size=15,
                           marker=dict(colors=shot_area['GROUP_VALUE']))
        st.plotly_chart(fig3, use_container_width=True)
        # right_col.plotly_chart(fig3, use_container_width=True)


# Get plot chart with a player avg stats(pts, ast, reb)
def bar_chart(p_id, player_name):
        p = playerprofilev2.PlayerProfileV2(player_id=p_id)
        df_p = p.get_data_frames()
        # df_r_s = get_career_stats(p_id)
        # st.write(df_r_s[0])

        avg_s = df_p[0].copy()
        # st.write(avg_s)
        avg_s = avg_s.drop(['PLAYER_ID', 'LEAGUE_ID', 'TEAM_ID'], axis=1)
        avg_s = pd.DataFrame(avg_s)
        avg_s = avg_s[::-1]
        avg_s = avg_s.iloc[np.unique(avg_s['SEASON_ID'], return_index=True)[1]]
        #st.dataframe(avg_s)
        columns_with_avg = ['MIN', 'FGM', 'FGA', 'FG3M', 'FG3A', 'FTM', 'FTA', 'OREB', 'DREB', 'REB', 'AST', 'STL',
                            'BLK', 'TOV', 'PF',
                            'PTS']
        df_avg = pd.DataFrame(columns=['SEASON_ID', 'TEAM_ABBREVIATION', 'PLAYER_AGE', 'GP', 'GS', 'MIN',
                                       'FGM', 'FGA', 'FG_PCT', 'FG3M', 'FG3A', 'FG3_PCT', 'FTM', 'FTA',
                                       'FT_PCT', 'OREB', 'DREB', 'REB', 'AST', 'STL', 'BLK', 'TOV', 'PF',
                                       'PTS'])
        for i in range(len(avg_s)):
            for col in df_avg.columns:
                if col in columns_with_avg:
                    nun = avg_s.iloc[i][col] / avg_s.iloc[i]['GP']
                    df_avg.loc[i, col] = nun


                else:
                    df_avg.loc[i, col] = avg_s.iloc[i][col]

        # Get the age and number of game played as integer
        df_avg['PLAYER_AGE'] = df_avg['PLAYER_AGE'].astype(int)
        df_avg['GP'] = df_avg['GP'].astype(int)
        df_avg['GS'] = df_avg['GS'].astype(int)

        df_chart = df_avg[['SEASON_ID', 'REB', 'AST', 'PTS']]
        df_chart['SEASON'] = df_avg.SEASON_ID.str.split('-').str[1]
        df_chart



        # Formate the columns to have 1 0r 2 after ther decimal.
        df_chart['PTS'] = df_chart['PTS'].astype(float).round(1)
        df_chart['AST'] = df_chart['AST'].astype(float).round(1)
        df_chart['REB'] = df_chart['REB'].astype(float).round(1)

        fig = go.Figure(data=[
            go.Bar(name='POINTS', x=df_chart['SEASON'], y=df_chart['PTS'], marker_color='indianred'),
            go.Bar(name='REBONDS', x=df_chart['SEASON'], y=df_chart['REB'], marker_color='lightsalmon'),
            go.Bar(name='AST', x=df_chart['SEASON'], y=df_chart['AST'])])
        # Change the bar mode
        fig.update_layout(barmode='group', height=500)
        fig.update_layout(title_text=f"{player_name}'s CAREER PTS, AST AND REB by years.")
        st.plotly_chart(fig, use_container_width=True)


