import re

# -------------------------------
# 1. FILE HANDLING (with Error Handling)
# -------------------------------

def read_file(filename):
    try:
        with open(filename, "r") as file:
            content = file.read()
            if not content.strip():
                print(f"Error: {filename} is empty.")
                return None
            return content
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")
        return None


# -------------------------------
# 2. STRING HANDLING FUNCTIONS
# -------------------------------

def clean_text(text):
    text = text.lower()  # Convert to lowercase
    text = re.sub(r'[^a-zA-Z0-9\s]', '', text)  # Remove special characters
    words = text.split()  # Split into words
    return words


# -------------------------------
# 3. SKILL EXTRACTION FUNCTION
# -------------------------------

def extract_skills(word_list):
    skills = list(set(word_list))  # Remove duplicates
    skills.sort()  # Sort alphabetically
    return skills


# -------------------------------
# 4. MATCHING LOGIC
# -------------------------------

def match_skills(resume_skills, job_skills):
    matched = list(set(resume_skills) & set(job_skills))
    missing = list(set(job_skills) - set(resume_skills))
    extra = list(set(resume_skills) - set(job_skills))

    return matched, missing, extra


# -------------------------------
# 5. PERCENTAGE CALCULATION
# -------------------------------

def calculate_match_percentage(matched, job_skills):
    if len(job_skills) == 0:
        return 0
    return (len(matched) / len(job_skills)) * 100


# -------------------------------
# 6. DICTIONARY (Frequency Count)
# -------------------------------

def skill_frequency(word_list):
    freq = {}
    for word in word_list:
        freq[word] = freq.get(word, 0) + 1
    return freq


# -------------------------------
# 7. DISPLAY FUNCTION
# -------------------------------

def display_results(matched, missing, extra, percentage):
    print("\n------ MATCH RESULTS ------")
    print("Matched Skills:", matched)
    print("Missing Skills:", missing)
    print("Extra Skills:", extra)

    print(f"\nMatch Percentage: {percentage:.2f}%")

    if percentage < 50:
        print("Match Level: LOW")
        print("Suggestion: Improve your skills based on missing skills.")
    elif percentage < 75:
        print("Match Level: MEDIUM")
    else:
        print("Match Level: HIGH")

    if percentage < 50:
        print("Recommendation: Consider enhancing your skills before applying.")


# -------------------------------
# 8. SAVE RESULTS TO FILE
# -------------------------------

def save_to_file(filename, data):
    with open(filename, "w") as file:
        for item in data:
            file.write(item + "\n")


# -------------------------------
# MAIN PROGRAM
# -------------------------------

def main():
    print("=== Resume Match & Skill Suggester ===")

    # Read Files
    resume_text = read_file("resume.txt")
    job_text = read_file("job_description.txt")

    if resume_text is None or job_text is None:
        print("Program stopped due to errors.")
        return

    # Display Inputs
    print("\n--- Resume Content ---")
    print(resume_text)

    print("\n--- Job Description Content ---")
    print(job_text)

    # Clean Text
    resume_words = clean_text(resume_text)
    job_words = clean_text(job_text)

    # Word Counts
    print("\nTotal words in Resume:", len(resume_words))
    print("Total words in Job Description:", len(job_words))

    # Extract Skills
    resume_skills = extract_skills(resume_words)
    job_skills = extract_skills(job_words)

    print("\nTotal unique skills in Resume:", len(resume_skills))
    print("Total unique skills in Job Description:", len(job_skills))

    # Match Skills
    matched, missing, extra = match_skills(resume_skills, job_skills)

    # Calculate Percentage
    percentage = calculate_match_percentage(matched, job_skills)

    # Frequency Dictionary
    resume_freq = skill_frequency(resume_words)
    job_freq = skill_frequency(job_words)

    # Display most frequent skill
    most_resume_skill = max(resume_freq, key=resume_freq.get)
    most_job_skill = max(job_freq, key=job_freq.get)

    print("\nMost repeated skill in Resume:", most_resume_skill)
    print("Most required skill in Job Description:", most_job_skill)

    # Display Results
    display_results(matched, missing, extra, percentage)

    # Save Results
    save_to_file("matched_skills.txt", matched)
    save_to_file("missing_skills.txt", missing)

    print("\nResults saved to files successfully!")


# Run program
main()