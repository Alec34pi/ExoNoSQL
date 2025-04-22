# Mise en place du projet Mongo Replica + Intégration Python

## Lancement des services

1. **Démarrer l'instance standalone :**  
   ```bash
   cd standalone
   docker-compose up -d
   ```

2. **Démarrer le replicaset :**  
   ```bash
   cd ../replicaset
   docker-compose up -d
   ```

---

## Initialisation du Replica Set

3. **Se connecter au container Mongo principal :**  
   ```bash
   docker exec -it mongo1 mongosh
   ```

4. **Lancer l'initialisation du replica set :**  
   ```javascript
   rs.initiate({
     _id: "rs0",
     members: [
       { _id: 0, host: "mongo1:27017" },
       { _id: 1, host: "mongo2:27017" },
       { _id: 2, host: "mongo3:27017" }
     ]
   })
   ```

5. **Vérifier que tout fonctionne correctement :**  
   ```javascript
   rs.status()
   ```

---

## Lancer l’intégration Python

6. **Exécuter l’application :**  
   ```bash
   cd ../integrations
   python app.py
   ```

---

## En cas de doute

Va jeter un œil ici :  
`docs/rapport.md` (❁´◡`❁)

---

## Petit mot de la fin

Testé sur Windows, bonne chance sur Linux ❤️  
(et que la force du `rs.status()` soit avec toi)
