def make_pizza(*toppings):
    print("\n which toping do you want to make pizza : ")
    for topping in toppings:
        print("-"+topping)

make_pizza('peproni')
make_pizza('tomato','cheese','butter','chocklate')


def build_profile(first, last, **user_info):
    profile = {}
    profile['first_name'] = first
    profile['last_name'] = last
    for key, value in user_info.items():
        profile[key] = value
        return profile


user_profile = build_profile('amol', 'gawade', location='baramati', at='pragati nagar')
print(user_profile)