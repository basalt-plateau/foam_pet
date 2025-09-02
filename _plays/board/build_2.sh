


#
#	. /Metro/_plays/build_2.sh
#



deactivate
. /Metro/.venv/bin/activate


git config --global --add safe.directory /Metro/Frontend_Vercel


export PATH="/root/.local/bin:$PATH"

#\
#	
#	Bun
#
#export PATH=$PATH:~/.bun/bin
#
#/

export PATH=$PATH:/Metro/vehicles/octave_nexus/__glossary

#
#
#

. /root/.bashrc

cd /Metro/estate