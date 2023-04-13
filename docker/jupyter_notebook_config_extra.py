c.ServerProxy.servers = {
    'test-server': {
        'command': ['python3', '-m', 'SimpleHTTPServer', '{port}'],
        'absolute_url': False
    }
}
