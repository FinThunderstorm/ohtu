from urllib import request
import toml
from project import Project


class ProjectReader:
    def __init__(self, url):
        self._url = url

    def get_project(self):
        # tiedoston merkkijonomuotoinen sisältö
        content = request.urlopen(self._url).read().decode("utf-8")
        # print(content)

        content = toml.loads(content)
        # print(content)

        # deserialisoi TOML-formaatissa oleva merkkijono ja muodosta Project-olio sen tietojen perusteella
        return Project(content['tool']['poetry']['name'], content['tool']['poetry']['description'], list(content['tool']['poetry']['dependencies'].keys()), list(content['tool']['poetry']['dev-dependencies'].keys()))
