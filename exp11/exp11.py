from pathlib import Path
import pandas as pd

base_dir = Path(__file__).resolve().parent
csv_path = base_dir / "experiment_11_prompting_techniques.csv"
if not csv_path.exists():
    from google.colab import files
    files.upload()
    csv_path = Path("experiment_11_prompting_techniques.csv")

df = pd.read_csv(csv_path)

positive_words = {"quick", "perfectly", "excellent", "helpful", "love", "early", "great"}
negative_words = {"poor", "dull", "stopped", "broken", "slow", "unavailable"}


def sentiment_demo(sentence):
    words = set(sentence.lower().replace(".", "").replace(",", "").split())
    score = len(words & positive_words) - len(words & negative_words)
    return "Positive" if score > 0 else "Negative" if score < 0 else "Neutral"


def construct_prompt(row):
    role = row["Role"]
    task = row["Task"]
    text = row["Input_Text"]
    technique = row["Technique"]
    if technique == "Zero-Shot":
        return f"You are a {role}. {task}: {text}"
    if technique == "One-Shot":
        return (f"You are a {role}. {task}. Example: "
                f"{row['Example_Input']} -> {row['Example_Output']}. New input: {text}")
    if technique == "Few-Shot":
        return (f"You are a {role}. {task}. Examples: "
                "Excellent service -> Positive; Poor quality -> Negative. "
                f"New input: {text}")
    return f"Act as a {role}. {task}: {text}"


print("----- ROLE-BASED AND EXAMPLE-BASED PROMPTING -----")
for _, row in df.iterrows():
    prompt = construct_prompt(row)
    if "sentiment" in row["Task"].lower():
        response = sentiment_demo(row["Input_Text"])
    elif "priority" in row["Task"].lower():
        response = "High" if "unavailable" in row["Input_Text"].lower() else "Low"
    else:
        response = "Suggested rewrite: Please share the project file at your earliest convenience."
    print(f"\nID: {row['Example_ID']} | Technique: {row['Technique']}")
    print("Constructed prompt:", prompt)
    print("Python demonstration response:", response)

print("\nDemonstration completed. Responses use predefined Python rules, not a live LLM.")
