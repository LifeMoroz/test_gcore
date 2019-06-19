import time

import git
from django.conf import settings
from django.http import JsonResponse


def get_repo_info(request):
    repo = git.Repo()
    try:
        branch = repo.active_branch
    except ValueError:
        return JsonResponse({
            "error": "uninitialized repo"
        })

    try:
        tag_name = repo.tags[-1].tag
    except IndexError:
        tag_name = ""

    return JsonResponse({
        "commit": branch.commit.hexsha,  # хеш хед-коммита текущей ветки
        "commit_date": branch.commit.committed_date,  # дата хед-коммита текущей ветки
        "branch": branch.name,  # текущая ветка
        "version": tag_name,  # максимальный тег хед-коммита
        "started": settings.INIT_TIME,
        "uptime_seconds": settings.INIT_TIME.timestamp() - time.time()
    })
