
def get_user_from_request(requests):
    return requests.user if not requests.user.is_anonymous else None
