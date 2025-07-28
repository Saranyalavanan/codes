import pandas as pd
import numpy as np
from sklearn.preprocessing import LabelEncoder, MinMaxScaler
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
import matplotlib.pyplot as plt
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score


data = pd.read_csv("datasets\\IPL.csv", encoding='ISO-8859-1') 
print(data.head(100))


grouped = data.groupby("batting_team").size()
print(grouped)

grouped = data.groupby("match_won_by").size()
print(grouped)


data["date"] = pd.to_datetime(data["date"])
print(data["date"])


cat = [
    "match_type", "event_name", "batting_team", "bowling_team", "batter",
    "bowler", "runs_not_boundary",  "non_striker", "umpires_call",
    "player_of_match", "match_won_by", "win_outcome", "toss_winner",
    "toss_decision", "venue", "city", "gender", "team_type", "superover_winner",
    "result_type", "method", "batting_partners",
    "next_batter", "striker_out"
]

label_encode = LabelEncoder()
for c in cat:
    data[c] = label_encode.fit_transform(data[c])
    print(data[c])

