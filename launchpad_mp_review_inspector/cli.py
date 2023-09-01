"""Console script for launchpad_mp_review_inspector."""
import os
import sys
import click

import launchpadagent
from launchpad_mp_review_inspector import get_mp_summary

@click.command()
@click.option('--launchpad-username', envvar='LAUNCHPAD_USERNAME', required=True,
              help="Your launchpad username."
                   "You can also set LAUNCHPAD_USERNAME as an environment "
                   "variable.", default=None)
@click.option('--launchpad-git-repo', 'launchpad_git_repos',  envvar='LAUNCHPAD_GIT_REPOS', required=True,
              help="Your launchpad git repo."
                   "You can also set LAUNCHPAD_GIT_REPO as an environment "
                   "variable.", default=None, multiple=True)
@click.option('--lp-credentials-store', envvar='LP_CREDENTIALS_STORE',
              required=False,
              help="An optional path to an already configured launchpad "
                   "credentials store.", default=None)
def main(launchpad_username, launchpad_git_repos, lp_credentials_store):
    """Console script for launchpad_mp_review_inspector."""
    click.echo("Retrieving merge proposals for {0} in {1}".format(launchpad_username, launchpad_git_repos))
    launchpad_cachedir = os.path.join('/tmp/launchpad_mp_review_inspector/.launchpadlib')
    lp = launchpadagent.get_launchpad(
        launchpadlib_dir=launchpad_cachedir,
        lp_credentials_store=lp_credentials_store)

    for source_repo in launchpad_git_repos:
        repo = lp.git_repositories.getByPath(path=source_repo.replace('lp:', ''))
        merge_proposals = repo.getMergeProposals(status=['Needs review', 'Merged', 'Approved', 'Rejected', 'Work in progress', 'Superseded', 'Queued'])
        for merge_proposal in merge_proposals:
            for vote in merge_proposal.votes:
                owner = vote.reviewer.name
                if owner == launchpad_username and hasattr(vote.comment, 'vote'):
                    target_source, summary = get_mp_summary(merge_proposal)
                    print(merge_proposal.web_link)
                    print("\t[{}] - {}".format(merge_proposal.date_created, target_source))
                    print("\t\t{}".format(summary))
                    print("\t\t{}".format(merge_proposal.queue_status))
                    print("\t\t{} {}".format(owner, vote.comment.vote))
    return 0


if __name__ == "__main__":
    sys.exit(main())  # pragma: no cover
