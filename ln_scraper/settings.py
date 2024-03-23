from ruamel.yaml import YAML

class SettingsParser:
    def __init__(self):
        pass

    def get_settings(self, settings_file):
        with open(settings_file, 'r') as stream:
            try:
                yaml = YAML(typ='safe')
                data = yaml.load(stream)
                # data = data['LoopNet']
                # settings = {}
                # settings['criteria'] = data['criteria']
                # settings['pageguid'] = data['pageguid']
                return data
            except Exception as exc:
                print(exc)