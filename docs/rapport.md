

# Partie 1 Mongo Standalone 

Creation du standalone avec un docker compose (standalone/docker-compose.yml) + Démarrage du docker avec : docker-compose up -d

test du docker avec : docker exec -it mongo-standalone mongosh -u admin -p MotDePasseTropSecure

db.createCollection("users")

db.users.insertOne({ name: "Alice", age: 30 })

db.users.insertMany([
  { name: "Bob", age: 25 },
  { name: "Charlie", age: 35 }
])

db.users.find() 
db.users.find({ age: { $gt: 30 } })


resultats : 


## Create


test> db.createCollection("users")
{ ok: 1 }


## Insert

test> db.users.insertOne({ name: "Alice", age: 30 })
{
  acknowledged: true,
  insertedId: ObjectId('68079b56e6ab9ca180d861e0')
}
test> db.users.insertMany([
...   { name: "Bob", age: 25 },
...   { name: "Charlie", age: 35 }
... ])
{
  acknowledged: true,
  insertedIds: {
    '0': ObjectId('68079b5ae6ab9ca180d861e1'),
    '1': ObjectId('68079b5ae6ab9ca180d861e2')
  }
}


## Find/Select


test> db.users.find()
[
  { _id: ObjectId('68079b56e6ab9ca180d861e0'), name: 'Alice', age: 30 },
  { _id: ObjectId('68079b5ae6ab9ca180d861e1'), name: 'Bob', age: 25 },
  {
    _id: ObjectId('68079b5ae6ab9ca180d861e2'),
    name: 'Charlie',
    age: 35
  }
]
test> db.users.find({ age: { $gt: 30 } })
[
  {
    _id: ObjectId('68079b5ae6ab9ca180d861e2'),
    name: 'Charlie',
    age: 35
  }
]


## UPDATE


 db.users.updateOne(
...   { name: "Bob" },
...   { $set: { age: 26 } }
... )
{
  acknowledged: true,
  insertedId: null,
  matchedCount: 1,
  modifiedCount: 1,
  upsertedCount: 0
}



## Delete

test> db.users.deleteOne({ name: "Charlie" })
{ acknowledged: true, deletedCount: 1 }



# Partie 2 Replica Set


Creation des replica avec un docker compose (replicaset/docker-compose.yml) + Démarrage du docker avec : docker-compose up -d

test du docker avec : docker exec -it mongo-standalone mongosh -u admin -p MotDePasseTropSecure


rs.initiate({
  _id: "rs0",
  members: [
    { _id: 0, host: "mongo1:27017" },
    { _id: 1, host: "mongo2:27017" },
    { _id: 2, host: "mongo3:27017" }
  ]
})


## Initiate


test> rs.initiate({
...   _id: "rs0",
...   members: [
...     { _id: 0, host: "mongo1:27017" },
...     { _id: 1, host: "mongo2:27017" },
...     { _id: 2, host: "mongo3:27017" }
...   ]
... })
{
  ok: 1,
  '$clusterTime': {
    clusterTime: Timestamp({ t: 1745329620, i: 1 }),
    signature: {
      hash: Binary.createFromBase64('AAAAAAAAAAAAAAAAAAAAAAAAAAA=', 0),
      keyId: Long('0')
    }
  },
  operationTime: Timestamp({ t: 1745329620, i: 1 })
}


## Status 

rs.status()

rs0 [direct: secondary] test> rs.status()
{
  set: 'rs0',
  date: ISODate('2025-04-22T13:47:15.216Z'),
  myState: 1,
  term: Long('1'),
  syncSourceHost: '',
  syncSourceId: -1,
  heartbeatIntervalMillis: Long('2000'),
  majorityVoteCount: 2,
  writeMajorityCount: 2,
  votingMembersCount: 3,
  writableVotingMembersCount: 3,
  optimes: {
    lastCommittedOpTime: { ts: Timestamp({ t: 1745329631, i: 16 }), t: Long('1') },
    lastCommittedWallTime: ISODate('2025-04-22T13:47:11.236Z'),
    readConcernMajorityOpTime: { ts: Timestamp({ t: 1745329631, i: 16 }), t: Long('1') },
    appliedOpTime: { ts: Timestamp({ t: 1745329631, i: 16 }), t: Long('1') },
    durableOpTime: { ts: Timestamp({ t: 1745329631, i: 16 }), t: Long('1') },
    writtenOpTime: { ts: Timestamp({ t: 1745329631, i: 16 }), t: Long('1') },
    lastAppliedWallTime: ISODate('2025-04-22T13:47:11.236Z'),
    lastDurableWallTime: ISODate('2025-04-22T13:47:11.236Z'),
    lastWrittenWallTime: ISODate('2025-04-22T13:47:11.236Z')
  },
  lastStableRecoveryTimestamp: Timestamp({ t: 1745329620, i: 1 }),
  electionCandidateMetrics: {
    lastElectionReason: 'electionTimeout',
    lastElectionDate: ISODate('2025-04-22T13:47:11.063Z'),
    electionTerm: Long('1'),
    lastCommittedOpTimeAtElection: { ts: Timestamp({ t: 1745329620, i: 1 }), t: Long('-1') },
    lastSeenWrittenOpTimeAtElection: { ts: Timestamp({ t: 1745329620, i: 1 }), t: Long('-1') },
    lastSeenOpTimeAtElection: { ts: Timestamp({ t: 1745329620, i: 1 }), t: Long('-1') },
    numVotesNeeded: 2,
    priorityAtElection: 1,
    electionTimeoutMillis: Long('10000'),
    numCatchUpOps: Long('0'),
    newTermStartDate: ISODate('2025-04-22T13:47:11.130Z'),
    wMajorityWriteAvailabilityDate: ISODate('2025-04-22T13:47:11.585Z')
  },
  members: [
    {
      _id: 0,
      name: 'mongo1:27017',
      health: 1,
      state: 1,
      stateStr: 'PRIMARY',
      uptime: 37,
      optime: { ts: Timestamp({ t: 1745329631, i: 16 }), t: Long('1') },
      optimeDate: ISODate('2025-04-22T13:47:11.000Z'),
      optimeWritten: { ts: Timestamp({ t: 1745329631, i: 16 }), t: Long('1') },
      optimeWrittenDate: ISODate('2025-04-22T13:47:11.000Z'),
      lastAppliedWallTime: ISODate('2025-04-22T13:47:11.236Z'),
      lastDurableWallTime: ISODate('2025-04-22T13:47:11.236Z'),
      lastWrittenWallTime: ISODate('2025-04-22T13:47:11.236Z'),
      syncSourceHost: '',
      syncSourceId: -1,
      infoMessage: 'Could not find member to sync from',
      electionTime: Timestamp({ t: 1745329631, i: 1 }),
      electionDate: ISODate('2025-04-22T13:47:11.000Z'),
      configVersion: 1,
      configTerm: 1,
      self: true,
      lastHeartbeatMessage: ''
    },
    {
      _id: 1,
      name: 'mongo2:27017',
      health: 1,
      state: 2,
      stateStr: 'SECONDARY',
      uptime: 14,
      optime: { ts: Timestamp({ t: 1745329631, i: 16 }), t: Long('1') },
      optimeDurable: { ts: Timestamp({ t: 1745329631, i: 16 }), t: Long('1') },
      optimeWritten: { ts: Timestamp({ t: 1745329631, i: 16 }), t: Long('1') },
      optimeDate: ISODate('2025-04-22T13:47:11.000Z'),
      optimeDurableDate: ISODate('2025-04-22T13:47:11.000Z'),
      optimeWrittenDate: ISODate('2025-04-22T13:47:11.000Z'),
      lastAppliedWallTime: ISODate('2025-04-22T13:47:11.236Z'),
      lastDurableWallTime: ISODate('2025-04-22T13:47:11.236Z'),
      lastWrittenWallTime: ISODate('2025-04-22T13:47:11.236Z'),
      lastHeartbeat: ISODate('2025-04-22T13:47:15.081Z'),
      lastHeartbeatRecv: ISODate('2025-04-22T13:47:14.080Z'),
      pingMs: Long('0'),
      lastHeartbeatMessage: '',
      syncSourceHost: 'mongo1:27017',
      syncSourceId: 0,
      infoMessage: '',
      configVersion: 1,
      configTerm: 1
    },
    {
      _id: 2,
      name: 'mongo3:27017',
      health: 1,
      state: 2,
      stateStr: 'SECONDARY',
      uptime: 14,
      optime: { ts: Timestamp({ t: 1745329631, i: 16 }), t: Long('1') },
      optimeDurable: { ts: Timestamp({ t: 1745329631, i: 16 }), t: Long('1') },
      optimeWritten: { ts: Timestamp({ t: 1745329631, i: 16 }), t: Long('1') },
      optimeDate: ISODate('2025-04-22T13:47:11.000Z'),
      optimeDurableDate: ISODate('2025-04-22T13:47:11.000Z'),
      optimeWrittenDate: ISODate('2025-04-22T13:47:11.000Z'),
      lastAppliedWallTime: ISODate('2025-04-22T13:47:11.236Z'),
      lastDurableWallTime: ISODate('2025-04-22T13:47:11.236Z'),
      lastWrittenWallTime: ISODate('2025-04-22T13:47:11.236Z'),
      lastHeartbeat: ISODate('2025-04-22T13:47:15.081Z'),
      lastHeartbeatRecv: ISODate('2025-04-22T13:47:14.081Z'),
      pingMs: Long('0'),
      lastHeartbeatMessage: '',
      syncSourceHost: 'mongo1:27017',
      syncSourceId: 0,
      infoMessage: '',
      configVersion: 1,
      configTerm: 1
    }
  ],
  ok: 1,
  '$clusterTime': {
    clusterTime: Timestamp({ t: 1745329631, i: 16 }),
    signature: {
      hash: Binary.createFromBase64('AAAAAAAAAAAAAAAAAAAAAAAAAAA=', 0),
      keyId: Long('0')
    }
  },
  operationTime: Timestamp({ t: 1745329631, i: 16 })
}


uri = "mongodb://mongo1:27017,mongo2:27017,mongo3:27017/?replicaSet=rs0"




## Insert 


rs0 [direct: primary] test> db.users.insertOne({ name: "Replica Robert", age: 40 })
{
  acknowledged: true,
  insertedId: ObjectId('68079ea2a113a22462d861e1')
}
rs0 [direct: primary] test>


## Changement de replica et find 

docker exec -it mongo2 mongosh --host mongo2:27017
db.users.find()

rs0 [direct: secondary] test> db.users.find()
[
  {
    _id: ObjectId('68079e93a113a22462d861e0'),
    name: 'Replica Alice',
    age: 40
  },
  {
    _id: ObjectId('68079ea2a113a22462d861e1'),
    name: 'Replica Robert',
    age: 40
  }
]

# Partie 3 

## Dependance utilisé : 
pip install pymongo

URL avec mot de passe et identifiant pour une connexion sécurisé 


## Selectionne la db et la collection 


db = client["testdb"]
collection = db["users"]


## Insert et print 

collection.insert_one({"name": "Alice", "age": 30})
print(list(collection.find()))