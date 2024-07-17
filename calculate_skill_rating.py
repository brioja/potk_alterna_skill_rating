import json
import re

def remove_comments(json_str):
    """
    Remove comments from a JSON string.
    """
    json_str = re.sub(r'\/\/.*', '', json_str)  # Remove // comments
    json_str = re.sub(r'\/\*[\s\S]*?\*\/', '', json_str)  # Remove /* */ comments
    return json_str

def calculate_skill_rating(skill):
    targets = skill.get("Targets", 1)
    regular_damage = skill.get("Regular Damage", 0)
    fixed_damage = skill.get("Fixed Damage", 0)

    # Calculate the total damage as a sum of regular and fixed damage
    total_damage = (regular_damage + fixed_damage) * targets

    # Simple rating based on total damage
    rating = total_damage
    return rating

def rate_skills(input_file):
    with open(input_file, 'r') as file:
        raw_data = file.read()
    
    json_str = remove_comments(raw_data)
    skills = json.loads(json_str)
    
    rated_skills = []
    for skill in skills:
        rating = calculate_skill_rating(skill)
        skill_info = {
            "Skill": skill["Skill"],
            "Units": skill["Units"],
            "Rating": rating
        }
        rated_skills.append(skill_info)
    
    # Sort skills by rating in descending order
    rated_skills.sort(key=lambda x: x["Rating"], reverse=True)
    return rated_skills

def main():
    input_file = 'input_skills.json'
    rated_skills = rate_skills(input_file)
    
    for skill in rated_skills:
        print(f"Skill: {skill['Skill']}, Units: {', '.join(skill['Units'])}, Rating: {skill['Rating']:.2f}")

if __name__ == "__main__":
    main()

