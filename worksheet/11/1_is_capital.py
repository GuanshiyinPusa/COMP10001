def is_capital(state, city):
    capitals = {'Victoria': 'Melbourne',
                'New South Wales': 'Sydney',
                'Queensland': 'Brisbane',
                'Tasmania': 'Hobart',
                'South Australia': 'Adelaide',
                'Western Australia': 'Perth'}
    return capitals.get(state, '') == city
