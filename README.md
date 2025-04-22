Comment faire fonctionner le tout : 

aller dans standalone faire un docker-compose up -d
faire pareil dans replicaset

faire un docker exec -it mongo1 mongosh

faire 
rs.initiate({
  _id: "rs0",
  members: [
    { _id: 0, host: "mongo1:27017" },
    { _id: 1, host: "mongo2:27017" },
    { _id: 2, host: "mongo3:27017" }
  ]
});


puis rs.status() pour verifier que ça a bien fonctionner 

puis dans integrations faire un python app.py



Je suis sur windows, bonne chance sur Linux ❤️