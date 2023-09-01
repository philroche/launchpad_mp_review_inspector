"""Main module."""
MAX_DESCRIPTION_LENGTH = 80


def get_mp_summary(mp):
    '''Format a sensible MP title from git branches and the description.'''
    title = ''
    git_source = mp.source_git_path
    if git_source is not None:

        source = mp.source_git_repository_link.replace(
            'https://api.launchpad.net/devel/', '')
        source += ':' + git_source.replace('refs/heads/', '') + \
                  '-> '
        title += source
    else:
        source = mp.source_branch_link.replace(
            'https://api.launchpad.net/devel/', '')
        source += '-> '
        title += source
    git_target = mp.target_git_path
    if git_target is not None:
        target = mp.target_git_repository_link.replace(
            'https://api.launchpad.net/devel/', '')
        target += ':' + git_target.replace('refs/heads/', '')
        title += target
    else:
        target = mp.target_branch_link.replace(
            'https://api.launchpad.net/devel/', '')
        title += target

    if mp.description is None:
        summary = mp.commit_message
    else:
        summary = mp.description
    if summary is not None:
        summary = summary.split('\n')[0]
        if len(summary) > MAX_DESCRIPTION_LENGTH:
            summary = summary[:MAX_DESCRIPTION_LENGTH] + '...'

    return title, summary
