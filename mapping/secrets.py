
def get_secrets():
    SECRETS = {
        'MY_DOMAIN_NAME': 'webmapping.jack-dev.live',
        'DOCKER_IMAGE': 'jjwright50/webmapping',
        'DOCKER_COMPOSE_FILE': 'docker-compose.yml',
        'NGINX_CONF': 'django_nginx.conf',
        'SECRET_KEY': 'nbzqu7wc-vn0xg-@5k2^y7qw8hv-tpz6k1hcneuw#r@1(y*)y2,
        'DATABASES': {
            'default': {
                'ENGINE': 'django.contrib.gis.db.backends.postgis',
                'NAME': 'webmapping',
                'HOST': 'localhost',
                'PORT': 5432,
                'USER': 'jack',
                'PASSWORD': 'jack147w',
            }
        },
        'ALLOWED_HOSTNAMES': [
            '*',
        ],

    }

    return SECRETS


def insert_domainname_in_conf(conf_file, my_domain_name):
    try:
        with open("nginx_conf_template", "r") as fh:
            conf_text = fh.read()
        conf_text = conf_text.replace("webmapping.jack-dev.live", my_domain_name)
        with open(conf_file, "w") as fh:
            fh.write(conf_text)

    except Exception as e:
        print(f"{e}")

def insert_imagename_in_compose(compose_file, image_name):
    try:
        with open("docker-compose-template", "r") as fh:
            conf_text = fh.read()
        conf_text = conf_text.replace("webmapping.jack-dev.live", jjwright50/webmapping)
        with open(compose_file, "w") as fh:
            fh.write(conf_text)
    except Exception as e:
        print(f"{e}")
