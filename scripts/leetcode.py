import argparse
import re
import subprocess
from pathlib import Path
from urllib.parse import urlparse

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
        if snippet["lang"] in ["Python", "Pandas"]:
            return snippet["code"]

def remove_object_from_class(code):
    """Removes object inheritance from new-style Python classes."""
    pattern = r'(class\s+\w+)\(object\)(\s*:)'
    replacement = r'\1\2'
    return re.sub(pattern, replacement, code)

def convert_docstring_to_type_hints(code):
    """Converts type hints in docstrings to actual Python 3 type hints."""
    # Regex to match a function signature and the associated docstring
    function_pattern = re.compile(r"def\s+(\w+)\((.*?)\):\s*\n\s*\"\"\"(.*?)\"\"\"", re.DOTALL)

    # Regex to extract parameter types (including complex types like List[int])
    param_type_pattern = re.compile(r"(\w+)\s*:\s*([\w\[\], ]+)")
    return_type_pattern = re.compile(r":rtype:\s*([\w\[\], ]+)")

    def convert_type(type_):
        """Converts types like List[int] to list[int]."""
        return type_.replace('List', 'list').replace('Dict', 'dict').replace('Tuple', 'tuple')

    def replace_function_signature(match):
        func_name = match.group(1)
        params = match.group(2)
        docstring = match.group(3)

        # Extract types from docstring
        param_types = param_type_pattern.findall(docstring)
        return_type = return_type_pattern.search(docstring)

        # Build new parameter list with type hints
        param_list = params.split(", ")
        for i, param in enumerate(param_list):
            for name, type_ in param_types:
                if name == param:
                    param_list[i] = f"{param}: {convert_type(type_)}"

        new_param_list = ", ".join(param_list)

        # Add return type hint if available
        return_hint = ""
        if return_type:
            return_hint = f" -> {convert_type(return_type.group(1))}"

        # Reconstruct the function signature with type hints
        new_function = f"def {func_name}({new_param_list}){return_hint}:"

        return f"{new_function}\n{' ' * 8}\"\"\"{docstring}\"\"\""  # Add indentation

    # Apply transformation to all functions in the code
    new_code = function_pattern.sub(replace_function_signature, code)
    return new_code

def convert_python2_to_python3(code):
    """Converts Python 2 code to Python 3 without object inheritance."""
    # Step 1: Remove (object) from class definitions
    code = remove_object_from_class(code)

    # Step 2: Convert docstring types into type hints
    return convert_docstring_to_type_hints(code)

def write_file(content: str, filepath: Path, mode: str = "w") -> None:
    """
    Writes content to a file.
    """
    with open(filepath, mode) as f:
        f.write(content)
    print(f"File written: {filepath}")


def write_solution_file(title, base_path="solutions") -> Path:
    sol_fpath = Path.cwd().parent / base_path / f"{title.replace('-', '_')}.py"
    sol_fpath.parent.mkdir(parents=True, exist_ok=True)
    if sol_fpath.exists():
        print(f"File already exists: {sol_fpath}")
        return sol_fpath
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
    snippet = convert_python2_to_python3(snippet)
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
    if test_fpath.exists():
        print(f"File already exists: {test_fpath}")
        return test_fpath
    write_file("", test_fpath)
    return test_fpath


def get_problem(
    title: str, solutions_path: str = "solutions", tests_path: str = "tests"
) -> tuple[Path, Path]:
    """
    Main function to fetch and write the LeetCode question content and code snippet to files.
    """

    sol_fpath = write_solution_file(title, solutions_path)
    test_fpath = write_test_file(title, tests_path)
    return sol_fpath, test_fpath


def parse_title(title):
    parts = urlparse(title)
    if not parts.netloc:
        return title
    elif parts.netloc == "leetcode.com":
        return [p for p in parts.path.split("/") if p][1]
    else:
        raise ValueError(f"Unexpected title: {title}")


def main(
    title: str, solutions_path: str, tests_path: str, ide: str
) -> None:
    title = parse_title(title)
    sol_path, test_path = get_problem(title, solutions_path, tests_path)
    subprocess.run([ide, str(sol_path), str(test_path)])


if __name__ == "__main__":
    argparse = argparse.ArgumentParser()
    argparse.add_argument(
        "title", type=str, help="Title or full URL of the LeetCode problem", nargs="?"
    )
    argparse.add_argument(
        "--solutions", type=str, default="solutions", help="Path to solutions"
    )
    argparse.add_argument("--tests", type=str, default="tests", help="Path to tests")
    argparse.add_argument("--ide", type=str, default="pycharm", help="IDE to open files")
    args = argparse.parse_args()
    main(args.title, args.solutions, args.tests, args.ide)
