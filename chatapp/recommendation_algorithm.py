import json

def load_user_data():
    with open('users.json', 'r') as json_file:
        return json.load(json_file)

def recommend_friends(user_id, user_data):
    user = user_data.get(user_id)

    if user is None:
        return []

    # Implement your recommendation algorithm here
    # For example, you can recommend friends with similar interests
    recommended_friends = []

    for other_user_id, other_user in user_data.items():
        if other_user_id != user_id:
            common_interests = set(user['interests']) & set(other_user['interests'])
            if len(common_interests) >= 2:  # Recommend if they have at least 2 common interests
                recommended_friends.append({
                    'id': other_user_id,
                    'name': other_user['name'],
                    'common_interests': list(common_interests)
                })

    # Sort recommended friends by the number of common interests (optional)
    recommended_friends.sort(key=lambda x: len(x['common_interests']), reverse=True)

    return recommended_friends[:5]  # Return the top 5 recommended friends
