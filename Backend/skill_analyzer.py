def extract_skills(text):

    skills = [
        "python",
        "java",
        "sql",
        "machine learning",
        "deep learning",
        "data analysis",
        "pandas",
        "numpy",
        "react",
        "node",
        "aws",
        "docker",
        "git"
    ]

    found_skills = []

    text = text.lower()

    for skill in skills:
        if skill in text:
            found_skills.append(skill)

    return list(set(found_skills))