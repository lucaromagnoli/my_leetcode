""""This script fetches the problem statement and the code snippet from leetcode and writes them to a file"""
from pathlib import Path

import requests
from bs4 import BeautifulSoup


def fetch_operation(data):
    url = "https://leetcode.com/graphql/"
    r = requests.post(url, json=data)
    return r.json()


def fetch_question_content(title):
    data = {
        "query": "query questionContent($titleSlug: String!) "
        "{question(titleSlug: $titleSlug) {content    mysqlSchemas    dataSchemas  }}",
        "variables": {"titleSlug": f"{title}"},
        "operationName": "questionContent",
    }
    return fetch_operation(data)


def fetch_question_editor_data():
    data = {
        "query": "query questionEditorData($titleSlug: String!) "
                 "{question(titleSlug: $titleSlug) "
                 "{questionId    questionFrontendId    "
                 "codeSnippets {lang      langSlug      code}"
                 "envInfo    enableRunCode    hasFrontendPreview    frontendPreviews}}",
        "variables": {"titleSlug": "regular-expression-matching"},
        "operationName": "questionEditorData",
    }

    return fetch_operation(data)


def parse_problem(content):
    soup = BeautifulSoup(content, "html.parser")
    text = soup.get_text().replace("\xa0", " ")
    return f"""\n{text}"""


def get_snippet(editor_data):
    for snippet in editor_data["data"]["question"]["codeSnippets"]:
        if snippet["lang"] == "Python":
            return snippet["code"]


def write_file(content, filepath, mode="w"):
    with open(filepath, mode) as f:
        f.write(content)


def main(title):

    sol_fpath = Path.cwd().parent / f"solutions/{title.replace("-", "_")}.py"
    test_fpath = Path.cwd().parent / f"tests/test_{title.replace("-", "_")}.py"
    question_content = fetch_question_content(title)
    content = parse_problem(question_content["data"]["question"]["content"])
    editor_data = fetch_question_editor_data()
    snippet = get_snippet(editor_data)
    write_file(content, sol_fpath)
    write_file(snippet, sol_fpath, mode="a")
    write_file("", test_fpath)


if __name__ == "__main__":
    main("letter-combinations-of-a-phone-number")
