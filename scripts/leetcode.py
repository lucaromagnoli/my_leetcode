from pathlib import Path
import argparse
import requests
from bs4 import BeautifulSoup


def fetch_operation(data: dict) -> dict:
    """
    Sends a POST request to the LeetCode GraphQL endpoint with the provided data.
    """
    url = "https://leetcode.com/graphql/"
    return requests.post(url, json=data).json()


def fetch_question_content(title: str) -> dict:
    """
    Fetches the content of a LeetCode question based on its title.
    """
    data = {
        "query": "query questionContent($titleSlug: String!) {question(titleSlug: $titleSlug) {content}}",
        "variables": {"titleSlug": title},
        "operationName": "questionContent",
    }
    return fetch_operation(data)


def fetch_question_title(title: str) -> dict:
    """
    Fetches the title of a LeetCode question based on its title.
    """
    data = {
        "query": """
            query questionTitle($titleSlug: String!) {
                question(titleSlug: $titleSlug) {
                    questionId
                    title
                    difficulty
                    categoryTitle
                }
            }
        """,
        "variables": {"titleSlug": title},
        "operationName": "questionTitle",
    }
    return fetch_operation(data)


def fetch_question_editor_data(title: str) -> dict:
    """
    Fetches the editor data of a LeetCode question based on its title.
    """
    data = {
        "query": "query questionEditorData($titleSlug: String!) {question(titleSlug: $titleSlug) {codeSnippets {lang code}}}",
        "variables": {"titleSlug": title},
        "operationName": "questionEditorData",
    }
    return fetch_operation(data)


def get_snippet(editor_data: dict) -> str:
    """
    Extracts the Python code snippet from the editor data.
    """
    for snippet in editor_data["data"]["question"]["codeSnippets"]:
        if snippet["lang"] == "Python":
            return snippet["code"]


def write_file(content: str, filepath: Path, mode: str = "w") -> None:
    """
    Writes content to a file.
    """
    with open(filepath, mode) as f:
        f.write(content)


def write_solution_file(title, base_path="solutions") -> Path:
    sol_fpath = Path.cwd().parent / base_path / f"{title.replace('-', '_')}.py"
    sol_fpath.parent.mkdir(parents=True, exist_ok=True)
    question_content = fetch_question_content(title)["data"]["question"]["content"]
    content = (
        BeautifulSoup(question_content, "html.parser").get_text().replace("\xa0", " ")
    )
    question_title = fetch_question_title(title)["data"]["question"]
    metadata = {
        "title": question_title["title"],
        "no": question_title["questionId"],
        "difficulty": question_title["difficulty"],
        "category": question_title["categoryTitle"],
    }
    editor_data = fetch_question_editor_data(title)
    snippet = get_snippet(editor_data)
    file_content = '"""\n'
    file_content += f"https://leetcode.com/problems/{title}/\n"
    file_content += f"Title: {metadata['title']}\n"
    file_content += f"No: {metadata['no']}\n"
    file_content += f"Difficulty: {metadata['difficulty']}\n"
    file_content += f"Category: {metadata['category']}\n"
    file_content += f"Problem:\n{content}\n"
    file_content += '"""\n'
    file_content += snippet
    write_file(file_content, sol_fpath)
    return sol_fpath


def write_test_file(title, base_path="tests") -> Path:
    test_fpath = Path.cwd().parent / base_path / f"test_{title.replace('-', '_')}.py"
    test_fpath.parent.mkdir(parents=True, exist_ok=True)
    write_file("", test_fpath)
    return test_fpath


def get_problem(
    title: str, solutions_path: str = "solutions", tests_path: str = "tests"
) -> None:
    """
    Main function to fetch and write the LeetCode question content and code snippet to files.
    """
    sol_fpath = write_solution_file(title, solutions_path)
    test_fpath = write_test_file(title, tests_path)
    print(f"Files created: {sol_fpath}, {test_fpath}")


def main(
    title: str, solutions_path: str = "solutions", tests_path: str = "tests"
) -> None:
    get_problem(title, solutions_path, tests_path)


if __name__ == "__main__":
    argparse = argparse.ArgumentParser()
    argparse.add_argument(
        "title", type=str, help="Title of the LeetCode problem", nargs="?"
    )
    argparse.add_argument(
        "--solutions", type=str, default="solutions", help="Path to solutions"
    )
    argparse.add_argument("--tests", type=str, default="tests", help="Path to tests")
    args = argparse.parse_args()
    main(args.title, args.solutions, args.tests)
