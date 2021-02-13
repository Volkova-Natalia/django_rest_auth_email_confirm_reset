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

end_point['swagger_expected'] = {
    'url': 'swagger/expected/',
    'name': 'swagger-expected',
}
