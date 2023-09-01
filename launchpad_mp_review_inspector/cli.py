"""Console script for launchpad_mp_review_inspector."""
import os
import sys
import click

import launchpadagent
from launchpad_mp_review_inspector import get_mp_summary

@click.command()
@click.option('--reviewer-launchpad-username', envvar='REVIEWER_LAUNCHPAD_USERNAME', required=False,
              help="Your launchpad username of the merge proposal review."
                   "You can also set REVIEWER_LAUNCHPAD_USERNAME as an environment "
                   "variable.", default=None)
@click.option('--proposer-launchpad-username', envvar='PROPOSER_LAUNCHPAD_USERNAME', required=False,
              help="Your launchpad username of the merge proposal proposer."
                   "You can also set PROPOSER_LAUNCHPAD_USERNAME as an environment "
                   "variable.", default=None)
@click.option('--launchpad-git-repo', 'launchpad_git_repos',  envvar='LAUNCHPAD_GIT_REPOS', required=True,
              help="Your launchpad git repo."
                   "You can also set LAUNCHPAD_GIT_REPO as an environment "
                   "variable.", default=None, multiple=True)
@click.option('--lp-credentials-store', envvar='LP_CREDENTIALS_STORE',
              required=False,
              help="An optional path to an already configured launchpad "
                   "credentials store.", default=None)
def main(reviewer_launchpad_username, proposer_launchpad_username, launchpad_git_repos, lp_credentials_store):
    """Console script for launchpad_mp_review_inspector."""
    click.echo("Retrieving merge proposals in {}".format(launchpad_git_repos))
    if reviewer_launchpad_username:
        click.echo("Filtered by merge proposal reviewer {}".format(reviewer_launchpad_username))
    if proposer_launchpad_username:
        click.echo("Filtered by merge proposal proposer {}".format(proposer_launchpad_username))
    launchpad_cachedir = os.path.join('/tmp/launchpad_mp_review_inspector/.launchpadlib')
    lp = launchpadagent.get_launchpad(
        launchpadlib_dir=launchpad_cachedir,
        lp_credentials_store=lp_credentials_store)

    for source_repo in launchpad_git_repos:
        repo = lp.git_repositories.getByPath(path=source_repo.replace('lp:', ''))
        merge_proposals = repo.getMergeProposals(status=['Needs review', 'Merged', 'Approved', 'Rejected', 'Work in progress', 'Superseded', 'Queued'])
        for merge_proposal in merge_proposals:
            _, merge_proposal_owner = merge_proposal.registrant_link.split('~')
            if not proposer_launchpad_username or (proposer_launchpad_username and merge_proposal_owner.lower() == proposer_launchpad_username.lower()):
                if reviewer_launchpad_username:
                    for vote in merge_proposal.votes:
                        owner = vote.reviewer.name
                        if owner.lower() == reviewer_launchpad_username.lower() and hasattr(vote.comment, 'vote'):
                            target_source, summary = get_mp_summary(merge_proposal)
                            print(merge_proposal.web_link)
                            print("\t[{}] - {}".format(merge_proposal.date_created, target_source))
                            print("\t\t{}".format(summary))
                            print("\t\t{}".format(merge_proposal.queue_status))
                            print("\t\t{} {}".format(owner, vote.comment.vote))
                else:
                    # we're not filtering on the reviewer so just print all MPs in list
                    target_source, summary = get_mp_summary(merge_proposal)
                    print(merge_proposal.web_link)
                    print("\t[{}] - {}".format(merge_proposal.date_created, target_source))
                    print("\t\t{}".format(summary))
                    print("\t\t{}".format(merge_proposal.queue_status))
    return 0


if __name__ == "__main__":
    sys.exit(main())  # pragma: no cover
