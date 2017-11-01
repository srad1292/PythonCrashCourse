# ** in front of user_info turns it into an empty dictionary


def build_profile(first, last, **user_info):
	"""Build a dictionary with everything we know about a user"""
	profile = {}
	profile['first_name'] = first
	profile['last_name'] = last
	for key, value in user_info.items():
		profile[key] = value
	return profile

user_profile = build_profile('albert', 'einstein',
							location='princeton',
							field='physics')
print(user_profile)