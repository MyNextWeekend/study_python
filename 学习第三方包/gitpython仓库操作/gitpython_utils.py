import git


def git_clone(git_url, repo_dir):
    # 克隆 Git 仓库
    try:
        git.Repo.clone_from(git_url, repo_dir)
    except git.exc.GitError as e:
        raise Exception(f"git clone err: {e}")
    print("git clone success")


if __name__ == '__main__':
    url = "git@github.com:MyNextWeekend/study_rust.git"
    repo_path = "/Users/weekend/workSpaces/vsCodeProjects/hello"
    git_clone(url, repo_path)
