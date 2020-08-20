  
import sqlite3

def connect_db():
    return sqlite3.connect('betmyway.db')

def create_odds_table():
    connect = connect_db()
    connect.execute('''
        CREATE TABLE IF NOT EXISTS ODDS
        (ID INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
        LEAGUE TEXT NOT NULL,
        HOME_TEAM TEXT NOT NULL,
        AWAY_TEAM TEXT NOT NULL,
        HOME_TEAM_WIN_ODDS TEXT NOT NULL,
        AWAY_TEAM_WIN_ODDS TEXT NOT NULL,
        DRAW_ODDS TEXT NOT NULL,
        GAME_DATE TEXT NULL);
        ''')

def get_db_odds():
    connect = connect_db()
    results = connect.execute('''
        SELECT 
        ID,
        LEAGUE,
        HOME_TEAM,
        AWAY_TEAM,
        HOME_TEAM_WIN_ODDS,
        AWAY_TEAM_WIN_ODDS,
        DRAW_ODDS,
        GAME_DATE
        FROM ODDS;
        ''')
    data = []
    for row in results:
        data_object = {}
        data_object["id"] = row[0]
        data_object["league"] = row[1]
        data_object["home_team"] = row[2]
        data_object["home_team_win_odds"] = row[3]
        data_object["away_team_win_odds"] = row[4]
        data_object["draw_odds"] = row[5]
        data_object["game_date"] = row[6]
        data.append(data_object)
    return data

def add_db_odds(data):
    connect = connect_db()
    """add odds"""
    query = "INSERT INTO ODDS(LEAGUE, HOME_TEAM, AWAY_TEAM, HOME_TEAM_WIN_ODDS, AWAY_TEAM_WIN_ODDS, DRAW_ODDS, GAME_DATE) VALUES('{0}', '{1}', '{2}', '{3}', '{4}','{5}', '{6}')".format(
        data['league'],
        data['home_team'],
        data['away_team'],
        data['home_team_win_odds'],
        data['away_team_win_odds'],
        data['draw_odds'],
        data['game_date']
        )
    connect.execute(query)
    connect.commit()
    connect.close()


def update_db_odds(data, ids):
    """update odds"""
    connect = connect_db()
    query = "UPDATE ODDS set LEAGUE = ? , HOME_TEAM = ?, AWAY_TEAM = ?, HOME_TEAM_WIN_ODDS = ? , AWAY_TEAM_WIN_ODDS = ?, DRAW_ODDS = ?, GAME_DATE = ? where ID = ? "


    connect.execute(query, (data['league'],data['home_team'],data['away_team'],
        data['home_team_win_odds'],data['away_team_win_odds'], 
        data['draw_odds'], data['game_date'], ids))
    connect.commit()
    connect.close()

def delete_from_odds(ids):
    """ delete odds"""
    connect = connect_db()

    query = " DELETE from ODDS where ID = ? "
    
    connect.execute(query, (ids,))
    connect.commit()
    connect.close()

