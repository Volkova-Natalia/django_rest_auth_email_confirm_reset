import os
import json


base_dir = os.path.dirname(os.path.abspath(__file__))
app_name = r'django_rest_auth_email_confirm_reset'
base_url = r'/'


with open(os.path.join(base_dir, 'static', app_name, 'swagger.json'), 'r') as swagger_file:
    swagger_paths = json.load(swagger_file)['paths']
end_point = {
    name: {
        'url': path[1:],
        'name': name,
    }
    for name in ('registration',
                 'login',
                 'logout',
                 'auth_info',
                 )
    for path in swagger_paths
    if name == swagger_paths[path]['x-name']
}


def select_parameter(*, url):
    """
    Select one parameter (start from the begin) from url from swagger.json
    For example:
    url in swagger = r"confirmation/{uidb64}/{token}/"
    parameter = uidb64
    pos_opened_curly_bracket = 13
    pos_closed_curly_bracket = 20
    """
    parameter = None
    pos_opened_curly_bracket = -1
    pos_closed_curly_bracket = -1

    pos_opened_curly_bracket = url.find('{')
    if pos_opened_curly_bracket >= 0:
        pos_closed_curly_bracket = url.find('}')
        if pos_closed_curly_bracket >= 0:
            parameter = url[pos_opened_curly_bracket+1:pos_closed_curly_bracket]
    return parameter, pos_opened_curly_bracket, pos_closed_curly_bracket


def change_parameters(*, url):
    """
    Change all parameters from url in format swagger.json to  format django.urlconf
    For example:
    r"confirmation/{uidb64}/{token}/" -> r"confirmation/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z\-]+)/"
    """
    re_types_default = r'[0-9A-Za-z]+'
    re_types = re_types_default

    parameter, pos_opened_curly_bracket, pos_closed_curly_bracket = select_parameter(url=url)

    while parameter:
        if parameter == 'uidb64':
            re_types = r'[0-9A-Za-z_\-]+'
        elif parameter == 'token':
            re_types = r'[0-9A-Za-z\-]+'
        else:
            re_types = re_types_default

        re_path_parameter = r'(?P<' + parameter + r'>' + re_types + r')'
        url = (url[:pos_opened_curly_bracket] +
               re_path_parameter +
               url[pos_closed_curly_bracket+1:])
        parameter, pos_opened_curly_bracket, pos_closed_curly_bracket = select_parameter(url=url)

    return url


name = 'confirmation'
end_point[name] = {}
for path in swagger_paths:
    if name == swagger_paths[path]['x-name']:
        url = r'^' + change_parameters(url=path[1:]) + r'$'
        end_point[name]['url'] = url
        end_point[name]['name'] = name


end_point['swagger_expected'] = {
    'url': 'swagger/expected/',
    'name': 'swagger-expected',
}
