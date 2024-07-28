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


def main(solutions_path: str = "solutions", tests_path: str = "tests") -> None:
    urls = [
        "https://leetcode.com/problems/two-sum",
        "https://leetcode.com/problems/add-two-numbers",
        "https://leetcode.com/problems/longest-substring-without-repeating-characters",
        "https://leetcode.com/problems/longest-palindromic-substring",
        "https://leetcode.com/problems/zigzag-conversion",
        "https://leetcode.com/problems/reverse-integer",
        "https://leetcode.com/problems/palindrome-number",
        "https://leetcode.com/problems/container-with-most-water",
        "https://leetcode.com/problems/integer-to-roman",
        "https://leetcode.com/problems/roman-to-integer",
        "https://leetcode.com/problems/longest-common-prefix",
        "https://leetcode.com/problems/3sum",
        "https://leetcode.com/problems/3sum-closest",
        "https://leetcode.com/problems/letter-combinations-of-a-phone-number",
        "https://leetcode.com/problems/4sum",
        "https://leetcode.com/problems/remove-nth-node-from-end-of-list",
        "https://leetcode.com/problems/valid-parentheses",
        "https://leetcode.com/problems/merge-two-sorted-lists",
        "https://leetcode.com/problems/swap-nodes-in-pairs",
        "https://leetcode.com/problems/remove-duplicates-from-sorted-array",
        "https://leetcode.com/problems/find-the-index-of-the-first-occurrence-in-a-string",
        "https://leetcode.com/problems/search-in-rotated-sorted-array",
        "https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array",
        "https://leetcode.com/problems/search-insert-position",
        "https://leetcode.com/problems/valid-sudoku",
        "https://leetcode.com/problems/sudoku-solver",
        "https://leetcode.com/problems/count-and-say",
        "https://leetcode.com/problems/combination-sum",
        "https://leetcode.com/problems/multiply-strings",
        "https://leetcode.com/problems/permutations",
        "https://leetcode.com/problems/n-queens",
        "https://leetcode.com/problems/jump-game",
        "https://leetcode.com/problems/length-of-last-word",
        "https://leetcode.com/problems/climbing-stairs",
        "https://leetcode.com/problems/word-break",
        "https://leetcode.com/problems/lucky-numbers-in-a-matrix",
        "https://leetcode.com/problems/finding-pairs-with-a-certain-sum",
        "https://leetcode.com/problems/sort-the-people",
    ]
    for url in urls:
        get_problem(url.split("/")[-1], solutions_path, tests_path)


if __name__ == "__main__":
    main("new_solutions", "new_tests")
