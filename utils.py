import requests


def load_candidates_from_json(path):
    return requests.get('https://www.jsonkeeper.com/b/RQR9').json()


def get_candidate(candidate_id, candidates):
    for candidate in candidates:
        if candidate_id == candidate['id']:
            return candidate


def get_candidates_by_name(candidate_name, candidates):
    result = []
    for candidate in candidates:
        if candidate_name in candidate['name'].split():
            result.append(candidate)
    return result


def get_candidates_by_skill(skill_name, candidates):
    result = []
    for candidate in candidates:
        if skill_name.lower() in candidate['skills'].lower().split(', '):
            result.append(candidate)
    return result
