class DocumentInfos:

    title = u'Les Failles zéro day'
    first_name = 'Noah'
    last_name = 'Guaico Tapia'
    author = f'{first_name} {last_name}'
    year = u'2023'
    month = u'Février'
    seminary_title = u'Travail personnel OCI'
    tutor = u"Cédric Donner"
    release = "version finale"
    repository_url = "https://github.com/<username>/<reponame>"

    @classmethod
    def date(cls):
        return cls.month + " " + cls.year

infos = DocumentInfos()