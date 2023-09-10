
DATA=$(curl https://api.covidtracking.com/v1/us/current.json)
POSITIVE=$(echo $DATA | jq '.[0].positive')
NEGATIVE=$(echo $DATA | jq '.[0].negative')
PENDING=$(echo $DATA | jq '.[0].pending')
DEATHINCREASE=$(echo $DATA | jq '.[0].deathIncrease')

TODAY=$(date)

echo "On $TODAY, there were $POSITIVE positive COVID cases and $NEGATIVE negative cases. The death toll increased by $DEATHINCREASE and there remain $PENDING tests pending"
