def artist_track(artist, track):
    return 'This is {0} by {1}'.format(track, artist)

def sum(*args):
    total = 0
    for arg in args:
        total+=arg
    return total

def form_submission(**kwargs):
    return 'Hello, {0}.'.format(kwargs['name'])

print(form_submission(name='Carl', email='this@gmail.com', address='haha Lane'))

print(sum(1, 2, 3, 5532, 2287, 10056))

print(artist_track('Kanye West', 'Through the Wire'))

print(artist_track(track = 'I am a God', artist = 'Yeezus'))