if [ -z $UPSTREAM_REPO ]
then
  echo "Cloning main Repository"
  git clone https://github.com/BLVCK-ANGEL/File-Donor-Bot.git /File-Donor-Bot
else
  echo "Cloning Custom Repo from $UPSTREAM_REPO "
  git clone $UPSTREAM_REPO /UP
fi
cd /File-Donor-Bot
pip3 install -U -r requirements.txt
echo "Starting UP...."
python3 bot.py
