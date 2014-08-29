#Loging to ssh and run command on actual terminal:
#Example: ssh and cd after
HOST=$1
DIR=$2
ssh $HOST -t cd $DIR"; bash --login"



