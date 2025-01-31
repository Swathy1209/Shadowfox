import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
# Load the dataset
file_path = "c:/Users/swathiga/Downloads/X data (1).csv"
df = pd.read_csv(file_path)


df.info(), df.head()

df = df.dropna().reset_index(drop=True)


sentiment_distribution = df['category'].value_counts(normalize=True) * 100
sentiment_distribution


sns.set_style("whitegrid")


plt.figure(figsize=(8, 5))
sns.barplot(x=sentiment_distribution.index, y=sentiment_distribution.values, palette=['green', 'gray', 'red'])
plt.xlabel("Sentiment Category")
plt.ylabel("Percentage")
plt.title("Sentiment Distribution of Tweets on X")
plt.xticks(ticks=[0, 1, 2], labels=["Positive", "Neutral", "Negative"])
plt.show()
df.columns
