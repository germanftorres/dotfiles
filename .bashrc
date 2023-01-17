#
# ~/.bashrc
#

# If not running interactively, don't do anything
[[ $- != *i* ]] && return

alias ls='ls --color=auto'
PS1='[\u@\h \W]\$ '
alias config='/usr/bin/git --git-dir=/home/german/dotfiles --work-tree=/home/german'

EDITOR=nvim


# nnn settings
export NNN_FIFO="/tmp/nnn.fifo"
export NNN_PLUG="p:preview-tui"
