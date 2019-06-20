import time

import datetime
import git
from django.conf import settings
from django.http import JsonResponse


def get_repo_info(request):
    repo = git.Repo(settings.BASE_DIR)
    try:
        branch = repo.active_branch
    except ValueError:
        return JsonResponse({
            "error": "uninitialized repo"
        })

    def tag_on_commit(tag):
        try:
            return tag.commit == branch.commit
        except ValueError:
            return False

    try:
        tag_name = list(filter(tag_on_commit, repo.tags))[-1].name
    except IndexError:
        tag_name = ""

    return JsonResponse({
        "commit": branch.commit.hexsha,  # хеш хед-коммита текущей ветки
        "commit_date": branch.commit.committed_datetime.astimezone(datetime.timezone.utc),  # дата хед-коммита
        "branch": branch.name,  # текущая ветка
        "version": tag_name,  # максимальный тег хед-коммита
        "started": settings.INIT_TIME,
        "uptime_seconds": time.time() - settings.INIT_TIME.timestamp()
    })
