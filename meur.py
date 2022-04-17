#!/usr/bin/python3

# git branch --issue [issue key]
# Standardised git branch creator based on ticket/issue key and title.
#
# Branches are created using the standard format of
#       [type]-[issue key]-[issue_title]
#
# Flow:
#   checkout default branch
#   generate branch name
#   create that branch
#   checkout that branch
#
# Limitations:
#   Compatible git platforms:
#       GitHub
#   Compatible issue trackers:
#       GitHub Issues
# issue
# ticket
# Usage:
#   meur setup/help/version/[issue key] <command> [arg]
#
#   Defaults are available if working from within a git inited directory.
#
#   setup [username]            setup meur for given GitHub [username].
#                                Env vars saved to .gitconfig
#       -i --issuetracker       issue tracker
#                                   github          GitHub Issues
#       -k --key                access key
#                               default: config vars
#                                   [username].JIRA_API_TOKEN  Jira Cloud API
#                                   Token
#                                   [username].GH_PAT          GitHub Personal Access
#                                                         Token
#       -j --jurl               if using Jira, atlassian.net cloud instance URL
#                                cname - https://[jurl].atlassian.net
#                               default: env var
#                                   JIRA_URL
#
#   help                        display this help
#       --h --help              alias of help
#
#   version                     show installed meur version
#       -v --version            alias of version
#
#   [issue key]
#       -a --alter              Alters existing local and remote branch based
#                                on current issue title. Subsequent flags
#                                ignored.
#                               default: create new branch from issue key
#       -u --username           repo login name - http://github.com/[username]
#                               default: current origin username
#       -r --repo               repo name
#                               default: current origin repo name
#       -t --type               branch type
#                               default: feature
#       -b --branch             branch from current branch
#                               default: cut from default branch


