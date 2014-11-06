redis_url = environ.get('REDISTOGO_URL')
if redis_url: 
    url = urlparse(redis_url)
    app.config.setdefault('REDIS_HOST', url.hostname)
	app.config.setdefault('REDIS_PORT', url.port)
    app.config.setdefault('REDIS_PASSWORD', url.password)