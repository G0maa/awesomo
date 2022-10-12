import json

# Deleting & Creating Language folder ?maybe? in github actions itself.

def intro(language):
    return [f'## Alphabetical index of projects in {language} :\n\n',
"""|       |       |       |       |       |       |       |
|---    |---    |---    |---    |---    |---    |    ---|
|[A](#a)|[B](#b)|[C](#c)|[D](#d)|[E](#e)|[F](#f)|[G](#g)|
|[H](#h)|[I](#i)|[J](#j)|[K](#k)|[L](#l)|[M](#m)|[N](#n)|
|[O](#o)|[P](#p)|[Q](#q)|[R](#r)|[S](#s)|[T](#t)|[U](#u)|
|[V](#v)|[W](#w)|[X](#x)|[Y](#y)|[Z](#z)|       |       |
|       |       |       |       |       |       |       |\n\n"""
    ,'<br>\n\n']


def sort_based_on_name(obj):
    return obj['name']

def main():
    json_file = open('./data.json')

    data = json.load(json_file)
    for language in data:
        name = language['language']
        projects = language['projects']

        # Creating language file
        language_file = open(f"./languages/{name}.md", 'w')
        language_file.writelines(intro(name))

        # Sorting projects alphabitcally
        projects.sort(key=sort_based_on_name)

        # Dummy value, will fail if there exists a project starting with '^'
        cur_letter = '^'

        for project in projects:
            lines = []

            # If starting character changes, add ## that character
            if cur_letter != project['name'][0]:
                cur_letter = project['name'][0]
                lines.append(f'## {cur_letter}\n\n')

            # note the added space...
            lines.extend([f"[**{project['name']}**]({project['url']}) ",
                          f"{project['description']}\n\n"])

            if "image_url" in project:
                lines.append(f"![{project['name']}]({project['image_url']})\n\n")

            lines.append('---\n\n')

            language_file.writelines(lines)
        language_file.close()

    json_file.close()

if __name__ == "__main__":
    main()
