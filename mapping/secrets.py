
def get_secrets():
    SECRETS = {
        'MY_DOMAIN_NAME': 'webmapping.jack-dev.live',
        'DOCKER_IMAGE': 'nginx_image6',
        'DOCKER_COMPOSE_FILE': 'docker-compose.yml',
        'NGINX_CONF': 'nginx_conf.yml',
        'SECRET_KEY': 'nbzqu7wc-vn0xg-@5k2^y7qw8hv-tpz6k1hcneuw#r@1(y*)y2,
        'DATABASES': {
            'default': {
                'ENGINE': 'django.contrib.gis.db.backends.postgis',
                'NAME': 'mappingDB',
                'HOST': '178.128.167.4',
                'PORT': 5432,
                'USER': 'docker',
                'PASSWORD': 'docker',
            }
        },
        'ALLOWED_HOSTNAMES': [
            'webmapping.jack-dev.live',
	    'LAPTOP-1AHNF5CO',
        ],

    }

    return SECRETS


def insert_domainname_in_conf(conf_file, my_domain_name):
    try:
        with open("nginx_conf.yml", "r") as fh:
            conf_text = fh.read()
        conf_text = conf_text.replace("webmapping.jack-dev.live", my_domain_name)
        with open(conf_file, "w") as fh:
            fh.write(conf_text)

    except Exception as e:
        print(f"{e}")

def insert_imagename_in_compose(compose_file, image_name):
    try:
        with open("docker-compose.yml", "r") as fh:
            conf_text = fh.read()
        conf_text = conf_text.replace("webmapping.jack-dev.live", image_name)
        with open(compose_file, "w") as fh:
            fh.write(conf_text)
    except Exception as e:
        print(f"{e}")
