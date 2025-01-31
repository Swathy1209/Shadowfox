import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


file_path = "c:/Users/swathiga/Downloads/IPL_sample_data_updated.xlsx"  
df = pd.read_excel(file_path)  



df.columns = df.columns.str.strip()


players = ["Rilee Russouw", "Phil Salt", "Yash Dhull", "Axar Patel", "Lalit Yadav", "Aman Khan", "Kuldeep Yadav"]


df["Player Name"] = players * (len(df) // len(players)) + players[:len(df) % len(players)]



print(df.head())


df.columns = df.columns.str.strip()

print("Column Names:", df.columns.tolist())

if "Player Name" not in df.columns:
    print("Error: 'Player Name' column not found. Please check the column names.")
else:
    print("Success: 'Player Name' column exists.")
selected_players = ["Rilee Russouw", "Phil Salt", "Yash Dhull"]  


df_selected = df[df["Player Name"].isin(selected_players)]  


weights = {
    "CP": 1,    # Clean Picks
    "GT": 1,    # Good Throws
    "C": 3,     # Catches
    "DC": -3,   # Dropped Catches
    "ST": 3,    # Stumpings
    "RO": 3,    # Run Outs
    "MRO": -2,  # Missed Run Outs
    "DH": 2,    # Direct Hits
}


performance_data = df_selected.groupby("Player Name").agg(
    CP=("Catch", lambda x: (x == "Y").sum()),
    GT=("Dropped Catch", lambda x: (x == "Y").sum()),
    C=("Catch", lambda x: (x == "C").sum()),
    DC=("Catch", lambda x: (x == "DC").sum()),
    ST=("Dropped Catch", lambda x: (x == "ST").sum()),
    RO=("Dropped Catch", lambda x: (x == "RO").sum()),
    MRO=("Dropped Catch", lambda x: (x == "MRO").sum()),
    DH=("Dropped Catch", lambda x: (x == "DH").sum()),
     RS=("Clean Pick", lambda x: pd.to_numeric(x, errors='coerce').sum())   # Runs saved/conceded
).reset_index()


performance_data["PS"] = (
    performance_data["CP"] * weights["CP"] +
    performance_data["GT"] * weights["GT"] +
    performance_data["C"] * weights["C"] +
    performance_data["DC"] * weights["DC"] +
    performance_data["ST"] * weights["ST"] +
    performance_data["RO"] * weights["RO"] +
    performance_data["MRO"] * weights["MRO"] +
    performance_data["DH"] * weights["DH"] +
    performance_data["RS"]
)


print(performance_data)


plt.figure(figsize=(8, 5))
sns.barplot(x="Player Name", y="PS", data=performance_data, palette="viridis")
plt.xlabel("Player")
plt.ylabel("Performance Score (PS)")
plt.title("Fielding Performance Score of Selected Players")
plt.show()
